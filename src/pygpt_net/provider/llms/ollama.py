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
import nest_asyncio


class OllamaLLM(StandardLLMProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            provider_id="ollama",
            provider_name="Ollama",
            supported_modes=[MODE_LLAMA_INDEX, "embeddings"],
            api_key_config="",  # No API key needed for Ollama
            *args,
            **kwargs
        )

    def _ensure_api_key(self, args: Dict, window) -> Dict:
        """
        Override to skip API key requirement for Ollama.

        :param args: Arguments dict
        :param window: Window instance
        :return: Unchanged arguments dict
        """
        # Ollama doesn't need API keys
        return args

    def _create_llm_instance(
            self,
            args: Dict,
            window,
            model: ModelItem
    ) -> LlamaBaseLLM:
        """
        Create Ollama LLM instance with custom configuration.

        :param args: Prepared arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: Ollama LLM instance
        """
        from .ollama_custom import Ollama

        # Apply nest_asyncio for Ollama
        nest_asyncio.apply()

        # Set default request timeout
        if "request_timeout" not in args:
            args["request_timeout"] = 300

        # Use OLLAMA_API_BASE environment variable if set
        if 'OLLAMA_API_BASE' in os.environ:
            if "base_url" not in args:
                args["base_url"] = os.environ['OLLAMA_API_BASE']

        return Ollama(**args)

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
        from llama_index.embeddings.ollama import OllamaEmbedding
        args = {}
        if config is not None:
            args = self.parse_args({
                "args": config,
            }, window)
        if 'OLLAMA_API_BASE' in os.environ:
            if "base_url" not in args:
                args["base_url"] = os.environ['OLLAMA_API_BASE']
        if "model" in args and "model_name" not in args:
            args["model_name"] = args.pop("model")
        return OllamaEmbedding(**args)

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
        super(OllamaLLM, self).init_embeddings(window, env)

        # === FIX FOR LOCAL EMBEDDINGS ===
        # if there is no OpenAI api key then set fake key to prevent empty key Llama-index error
        if ('OPENAI_API_KEY' not in os.environ
                and (window.core.config.get('api_key') is None or window.core.config.get('api_key') == "")):
            os.environ['OPENAI_API_KEY'] = "_"
