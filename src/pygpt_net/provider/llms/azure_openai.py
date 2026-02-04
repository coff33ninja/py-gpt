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

from typing import Optional, List, Dict

from llama_index.core.llms.llm import BaseLLM as LlamaBaseLLM
from llama_index.core.base.embeddings.base import BaseEmbedding

from pygpt_net.core.types import MODE_LLAMA_INDEX
from pygpt_net.provider.llms.base_provider import StandardLLMProvider
from pygpt_net.item.model import ModelItem


class AzureOpenAILLM(StandardLLMProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            provider_id="azure_openai",
            provider_name="Azure OpenAI",
            supported_modes=[MODE_LLAMA_INDEX, "embeddings"],
            api_key_config="api_key",
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
        Create Azure OpenAI LLM instance.

        :param args: Prepared arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: AzureOpenAI LLM instance
        """
        from llama_index.llms.azure_openai import AzureOpenAI as LlamaAzureOpenAI
        return LlamaAzureOpenAI(**args)

    def completion(
            self,
            window,
            model: ModelItem,
            stream: bool = False
    ):
        """
        Return LLM provider instance for completion

        :param window: window instance
        :param model: model instance
        :param stream: stream mode
        :return: LLM provider instance
        """
        pass

    def chat(
            self,
            window,
            model: ModelItem,
            stream: bool = False
    ):
        """
        Return LLM provider instance for chat

        :param window: window instance
        :param model: model instance
        :param stream: stream mode
        :return: LLM provider instance
        """
        pass

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
        from llama_index.embeddings.azure_openai import AzureOpenAIEmbedding
        args = {}
        if config is not None:
            args = self.parse_args({
                "args": config,
            }, window)
        if "api_key" not in args:
            args["api_key"] = window.core.config.get("api_key", "")
        if "model" in args and "model_name" not in args:
            args["model_name"] = args.pop("model")
        args = self.inject_llamaindex_http_clients(args, window.core.config)
        return AzureOpenAIEmbedding(**args)
