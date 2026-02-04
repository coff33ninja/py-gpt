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

import os
from typing import Optional, List, Dict

from llama_index.core.llms.llm import BaseLLM as LlamaBaseLLM
from llama_index.core.base.embeddings.base import BaseEmbedding

from pygpt_net.core.types import MODE_LLAMA_INDEX
from pygpt_net.provider.llms.base_provider import StandardLLMProvider
from pygpt_net.item.model import ModelItem


class HuggingFaceApiLLM(StandardLLMProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            provider_id="huggingface_api",
            provider_name="HuggingFace API",
            supported_modes=[MODE_LLAMA_INDEX, "embeddings"],
            api_key_config="api_key_hugging_face",
            *args,
            **kwargs
        )

    def _ensure_api_key(self, args: Dict, window) -> Dict:
        """
        Override to handle token/api_key aliasing for HuggingFace.

        :param args: Arguments dict
        :param window: Window instance
        :return: Updated arguments dict
        """
        # HuggingFace uses 'token' instead of 'api_key'
        if "token" not in args:
            if "api_key" in args and args["api_key"]:
                args["token"] = args.pop("api_key")
            else:
                args["token"] = window.core.config.get("api_key_hugging_face", "")
        return args

    def _create_llm_instance(
            self,
            args: Dict,
            window,
            model: ModelItem
    ) -> LlamaBaseLLM:
        """
        Create HuggingFace Inference API LLM instance with custom proxy support.

        :param args: Prepared arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: HuggingFaceInferenceAPI LLM instance
        """
        from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI as LIHF

        cfg = window.core.config

        # Set Inference Endpoint / router if configured
        base_url = cfg.get("api_endpoint_hugging_face", "").strip()
        if base_url and "base_url" not in args:
            args["base_url"] = base_url

        # Get proxy and trust_env settings
        proxy = cfg.get("api_proxy") or cfg.get("api_native_hf.proxy")
        if not cfg.get("api_proxy.enabled", False):
            proxy = ""
        trust_env = cfg.get("api_native_hf.trust_env", False)

        # Custom proxy wrapper for HuggingFace Inference API
        class HuggingFaceInferenceAPIWithProxy(LIHF):
            def __init__(self, *, proxy=None, trust_env=None, **kwargs):
                """
                proxy: str or dict compatible with huggingface_hub
                trust_env: for AsyncInferenceClient (default False)
                """
                # alias: api_key -> token (already handled in _ensure_api_key)
                if "api_key" in kwargs and "token" not in kwargs:
                    kwargs["token"] = kwargs.pop("api_key")

                super().__init__(**kwargs)

                if proxy is None and trust_env is None:
                    return

                if isinstance(proxy, str):
                    hf_proxies = {"http": proxy, "https": proxy}
                else:
                    hf_proxies = proxy

                base_kwargs = {}
                if hasattr(self, "_get_inference_client_kwargs"):
                    try:
                        base_kwargs = self._get_inference_client_kwargs()
                    except Exception:
                        base_kwargs = {}

                # fallback
                if not base_kwargs:
                    for src in ["model", "token", "timeout", "headers", "cookies", "base_url", "task"]:
                        if hasattr(self, src):
                            val = getattr(self, src)
                            if val not in (None, ""):
                                base_kwargs[src] = val

                from huggingface_hub import InferenceClient, AsyncInferenceClient

                sync_kwargs = dict(base_kwargs)
                async_kwargs = dict(base_kwargs)
                if hf_proxies is not None:
                    sync_kwargs["proxies"] = hf_proxies
                    async_kwargs["proxies"] = hf_proxies
                if trust_env is not None:
                    async_kwargs["trust_env"] = trust_env

                sync_client = InferenceClient(**sync_kwargs)
                async_client = AsyncInferenceClient(**async_kwargs)

                for name, client in (("_client", sync_client), ("_sync_client", sync_client), ("client", sync_client)):
                    if hasattr(self, name):
                        setattr(self, name, client)
                for name, client in (("_aclient", async_client), ("_async_client", async_client)):
                    if hasattr(self, name):
                        setattr(self, name, client)

        return HuggingFaceInferenceAPIWithProxy(proxy=proxy, trust_env=trust_env, **args)

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
        from .hugging_face_embedding import (
            HuggingFaceInferenceAPIEmbeddingWithProxy as HFEmbed,
        )

        args: Dict = {}
        if config is not None:
            args = self.parse_args({"args": config}, window)

        # token / api_key
        if "token" not in args:
            if "api_key" in args:
                args["token"] = args.pop("api_key")
            else:
                args["token"] = window.core.config.get("api_key_hugging_face", "")

        # model_name alias
        if "model" in args and "model_name" not in args:
            args["model_name"] = args.pop("model")

        # Inference Endpoint / router
        base_url = window.core.config.get("api_endpoint_hugging_face", "").strip()
        if base_url and "base_url" not in args:
            args["base_url"] = base_url

        # proxy + trust_env (async)
        proxy = window.core.config.get("api_proxy") or window.core.config.get("api_native_hf.proxy")
        if not window.core.config.get("api_proxy.enabled", False):
            proxy = ""
        trust_env = window.core.config.get("api_native_hf.trust_env", False)

        return HFEmbed(proxy=proxy, trust_env=trust_env, **args)

    def init_embeddings(
            self,
            window,
            env: Optional[List[Dict]] = None
    ):
        """
        Initialize embeddings provider

        :param window: window instance
        :param env: ENV configuration list
        """
        super(HuggingFaceApiLLM, self).init_embeddings(window, env)

        # === FIX FOR LOCAL EMBEDDINGS ===
        # if there is no OpenAI api key then set fake key to prevent empty key Llama-index error
        if ('OPENAI_API_KEY' not in os.environ
                and (window.core.config.get('api_key') is None or window.core.config.get('api_key') == "")):
            os.environ['OPENAI_API_KEY'] = "_"
