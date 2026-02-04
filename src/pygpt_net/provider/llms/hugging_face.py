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


class HuggingFaceLLM(StandardLLMProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            provider_id="huggingface",
            provider_name="HuggingFace (Local Transformers)",
            supported_modes=[MODE_LLAMA_INDEX, "embeddings"],
            api_key_config="",  # No API key needed for local models
            *args,
            **kwargs
        )

    def _ensure_api_key(self, args: Dict, window) -> Dict:
        """
        Override to skip API key requirement for local HuggingFace models.

        :param args: Arguments dict
        :param window: Window instance
        :return: Unchanged arguments dict
        """
        # Local HuggingFace models don't need API keys
        return args

    def _create_llm_instance(
            self,
            args: Dict,
            window,
            model: ModelItem
    ) -> LlamaBaseLLM:
        """
        Create local HuggingFace LLM instance using transformers.

        :param args: Prepared arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: HuggingFaceLLM instance
        """
        from llama_index.llms.huggingface import HuggingFaceLLM as LlamaHuggingFaceLLM

        # Use model_name instead of model for HuggingFace
        if "model" in args and "model_name" not in args:
            args["model_name"] = args.pop("model")

        # Set default device_map if not specified
        if "device_map" not in args:
            args["device_map"] = "auto"

        return LlamaHuggingFaceLLM(**args)

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
        Return provider instance for embeddings (local sentence-transformers)

        :param window: window instance
        :param config: config keyword arguments list
        :return: Embedding provider instance
        """
        from llama_index.embeddings.huggingface import HuggingFaceEmbedding

        args = {}
        if config is not None:
            args = self.parse_args({
                "args": config,
            }, window)

        # Use model_name instead of model for HuggingFace
        if "model" in args and "model_name" not in args:
            args["model_name"] = args.pop("model")

        return HuggingFaceEmbedding(**args)

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
        super(HuggingFaceLLM, self).init_embeddings(window, env)

        # === FIX FOR LOCAL EMBEDDINGS ===
        # if there is no OpenAI api key then set fake key to prevent empty key Llama-index error
        if ('OPENAI_API_KEY' not in os.environ
                and (window.core.config.get('api_key') is None or window.core.config.get('api_key') == "")):
            os.environ['OPENAI_API_KEY'] = "_"
