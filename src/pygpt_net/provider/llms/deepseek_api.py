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

from pygpt_net.core.types import MODE_LLAMA_INDEX
from pygpt_net.provider.llms.base_provider import StandardLLMProvider
from pygpt_net.item.model import ModelItem


class DeepseekApiLLM(StandardLLMProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            provider_id="deepseek_api",
            provider_name="Deepseek API",
            supported_modes=[MODE_LLAMA_INDEX, "embeddings"],
            api_key_config="api_key_deepseek",
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
        Create Deepseek LLM instance.

        :param args: Prepared arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: DeepSeek LLM instance
        """
        from llama_index.llms.deepseek import DeepSeek
        return DeepSeek(**args)

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
        items = []
        client = self.get_client(window)
        models_list = client.models.list()
        if models_list.data:
            for item in models_list.data:
                items.append({
                    "id": item.id,
                    "name": item.id,
                })
        return items
