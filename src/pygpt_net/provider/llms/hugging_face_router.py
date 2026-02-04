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
from llama_index.core.multi_modal_llms import MultiModalLLM as LlamaMultiModalLLM
from llama_index.core.base.embeddings.base import BaseEmbedding

from pygpt_net.core.types import MODE_CHAT, MODE_LLAMA_INDEX
from pygpt_net.provider.llms.base_provider import StandardLLMProvider
from pygpt_net.item.model import ModelItem


class HuggingFaceRouterLLM(StandardLLMProvider):
    def __init__(self, *args, **kwargs):
        super().__init__(
            provider_id="huggingface_router",
            provider_name="HuggingFace Router",
            supported_modes=[MODE_CHAT, MODE_LLAMA_INDEX, "embeddings"],
            api_key_config="api_key_hugging_face",
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
        Create HuggingFace Router LLM instance using OpenAILike.

        :param args: Prepared arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: OpenAILike LLM instance
        """
        from llama_index.llms.openai_like import OpenAILike
        return OpenAILike(**args)

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

    def llama_multimodal(
            self,
            window,
            model: ModelItem,
            stream: bool = False
    ) -> LlamaMultiModalLLM:
        """
        Return multimodal LLM provider instance for llama

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
