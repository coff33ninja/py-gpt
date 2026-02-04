#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2026.02.04 00:00:00                  #
# ================================================== #

from typing import List, Dict, Optional

from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.core.llms.llm import BaseLLM as LlamaBaseLLM

from pygpt_net.core.types import MODE_LLAMA_INDEX, MODE_CHAT
from pygpt_net.provider.llms.base_provider import StandardLLMProvider
from pygpt_net.item.model import ModelItem


class AnthropicLLM(StandardLLMProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            provider_id="anthropic",
            provider_name="Anthropic",
            supported_modes=[MODE_LLAMA_INDEX, "embeddings"],
            api_key_config="api_key_anthropic",
            *args,
            **kwargs
        )

    def _create_llm_instance(
            self,
            args: Dict,
            window,
            model: ModelItem
    ) -> LlamaBaseLLM:
        """
        Create Anthropic LLM instance with custom proxy support.

        :param args: Prepared arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: Anthropic LLM instance
        """
        from llama_index.llms.anthropic import Anthropic

        cfg = window.core.config
        proxy = cfg.get("api_proxy", None)
        if not cfg.get("api_proxy.enabled", False):
            proxy = None

        # Custom proxy wrapper for Anthropic
        class AnthropicWithProxy(Anthropic):
            def __init__(self, *args, proxy: str = None, **kwargs):
                super().__init__(*args, **kwargs)
                if not proxy:
                    return

                # sync
                from anthropic import DefaultHttpxClient
                self._client = self._client.with_options(
                    http_client=DefaultHttpxClient(proxy=proxy)
                )

                # async
                import httpx
                try:
                    async_http = httpx.AsyncClient(proxy=proxy)  # httpx >= 0.28
                except TypeError:
                    async_http = httpx.AsyncClient(proxies=proxy)  # httpx <= 0.27

                self._aclient = self._aclient.with_options(http_client=async_http)

        return AnthropicWithProxy(**args, proxy=proxy)

    def _setup_remote_tools(
            self,
            args: Dict,
            window,
            model: ModelItem
    ) -> Dict:
        """
        Setup Anthropic remote server tools (e.g., web_search_20250305).

        :param args: Arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: Updated arguments dict
        """
        try:
            remote_tools = window.core.api.anthropic.tools.build_remote_tools(model=model) or []
        except Exception as e:
            window.core.debug.log(e)
            remote_tools = []

        if remote_tools:
            # Merge with any user-supplied 'tools' (avoid duplicates by (type, name))
            existing = args.get("tools") or []
            if isinstance(existing, list):
                def _key(d: dict) -> str:
                    return f"{d.get('type')}::{d.get('name')}"
                index = {_key(t): True for t in existing if isinstance(t, dict)}
                for t in remote_tools:
                    k = _key(t) if isinstance(t, dict) else None
                    if k and k not in index:
                        existing.append(t)
                args["tools"] = existing
            else:
                # Defensive: if 'tools' was something unexpected, overwrite safely
                args["tools"] = list(remote_tools)

        return args

    def get_embeddings_model(
            self,
            window,
            config: Optional[List[Dict]] = None
    ) -> BaseEmbedding:
        """
        Return provider instance for embeddings

        :param window: window instance
        :param config: config keyword arguments list
        :return: Embedding provider instance
        """
        from .voyage import VoyageEmbeddingWithProxy
        args = {}
        if config is not None:
            args = self.parse_args({
                "args": config,
            }, window)
        if "api_key" in args:
            args["voyage_api_key"] = args.pop("api_key")
        if "voyage_api_key" not in args or args["voyage_api_key"] == "":
            args["voyage_api_key"] = window.core.config.get("api_key_voyage", "")
        if "model" in args and "model_name" not in args:
            args["model_name"] = args.pop("model")

        timeout = window.core.config.get("api_native_voyage.timeout")
        max_retries = window.core.config.get("api_native_voyage.max_retries")
        proxy = window.core.config.get("api_proxy")
        if not window.core.config.get("api_proxy.enabled", False):
            proxy = ""
        return VoyageEmbeddingWithProxy(
            **args,
            proxy=proxy,
            timeout=timeout,
            max_retries=max_retries,
        )

    def get_models(
            self,
            window,
    ) -> List[Dict]:
        """
        Return list of models for the provider

        :param window: window instance
        :return: list of models
        """
        model = ModelItem()
        model.provider = "anthropic"
        client = window.core.api.anthropic.get_client(MODE_CHAT, model)
        models_list = client.models.list()
        items = []
        if models_list.data:
            for item in models_list.data:
                items.append({
                    "id": item.id,
                    "name": item.id,
                })
        return items
