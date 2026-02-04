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

from typing import Optional, Dict, List

from llama_index.core.base.embeddings.base import BaseEmbedding
from llama_index.core.llms.llm import BaseLLM as LlamaBaseLLM

from pygpt_net.core.types import MODE_LLAMA_INDEX
from pygpt_net.provider.llms.base_provider import StandardLLMProvider
from pygpt_net.item.model import ModelItem


class OpenRouterLLM(StandardLLMProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            provider_id="open_router",
            provider_name="OpenRouter",
            supported_modes=[MODE_LLAMA_INDEX, "embeddings"],
            api_key_config="api_key_open_router",
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
        Create OpenRouter LLM instance using OpenAILike.

        :param args: Prepared arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: OpenAILike LLM instance
        """
        from llama_index.llms.openai_like import OpenAILike

        # Set OpenRouter-specific API base
        if "api_base" not in args:
            args["api_base"] = window.core.config.get("api_endpoint_open_router", "")

        # Set chat model flags
        if "is_chat_model" not in args:
            args["is_chat_model"] = True
        if "is_function_calling_model" not in args:
            args["is_function_calling_model"] = model.tool_calls

        # Get OpenRouter-specific model name
        if model:
            args["model"] = window.core.models.get_openrouter_model(model)

        return OpenAILike(**args)

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
        from llama_index.embeddings.openai_like import OpenAILikeEmbedding
        args = {}
        if config is not None:
            args = self.parse_args({
                "args": config,
            }, window)
        if "api_key" not in args:
            args["api_key"] = window.core.config.get("api_key_open_router", "")
        if "api_base" not in args:
            args["api_base"] = window.core.config.get("api_endpoint_open_router", "")
        if "model" in args and "model_name" not in args:
            args["model_name"] = args.pop("model")
        args = self.inject_llamaindex_http_clients(args, window.core.config)
        return OpenAILikeEmbedding(**args)

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
