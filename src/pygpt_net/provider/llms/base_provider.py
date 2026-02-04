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

"""
Standard LLM Provider Base Class

Provides common functionality for LLM providers to reduce code duplication.
Implements template method pattern for llama() with hooks for customization.
"""

from abc import abstractmethod
from typing import Dict, List
from llama_index.core.llms.llm import BaseLLM as LlamaBaseLLM
from pygpt_net.provider.llms.base import BaseLLM
from pygpt_net.item.model import ModelItem


class StandardLLMProvider(BaseLLM):
    """
    Standard LLM provider with common functionality.
    
    Reduces code duplication by providing:
    - Standardized initialization
    - Common API key management
    - Automatic model ID setting
    - Proxy configuration via inherited inject_llamaindex_http_clients()
    - Template method for llama() with customization hooks
    
    Subclasses only need to:
    1. Call super().__init__() with provider details
    2. Implement _create_llm_instance() to create provider-specific LLM
    3. Optionally override _setup_remote_tools() for remote tools support
    4. Optionally override _ensure_api_key() for custom API key logic
    """
    
    def __init__(
        self,
        provider_id: str,
        provider_name: str,
        supported_modes: List[str],
        api_key_config: str,
        *args,
        **kwargs
    ):
        """
        Initialize standard LLM provider.
        
        :param provider_id: Provider ID (e.g., "anthropic", "openai")
        :param provider_name: Display name (e.g., "Anthropic", "OpenAI")
        :param supported_modes: List of supported modes (e.g., [MODE_LLAMA_INDEX, "embeddings"])
        :param api_key_config: Config key for API key (e.g., "api_key_anthropic")
        """
        super().__init__(*args, **kwargs)
        self.id = provider_id
        self.name = provider_name
        self.type = supported_modes
        self._api_key_config = api_key_config
    
    def llama(
        self,
        window,
        model: ModelItem,
        stream: bool = False
    ) -> LlamaBaseLLM:
        """
        Return LLM provider instance for llama index.
        
        Template method that handles common setup:
        1. Parse args from model config
        2. Ensure API key is set
        3. Ensure model ID is set
        4. Setup proxy via inject_llamaindex_http_clients()
        5. Setup remote tools (if supported)
        6. Create provider-specific LLM instance
        
        :param window: Window instance
        :param model: Model instance
        :param stream: Stream mode
        :return: LLM provider instance
        """
        # 1. Parse args from model config
        args = self.parse_args(model.llama_index, window)
        
        # 2. Ensure API key is set
        args = self._ensure_api_key(args, window)
        
        # 3. Ensure model ID is set
        if "model" not in args:
            args["model"] = model.id
        
        # 4. Setup proxy (uses inherited method)
        args = self.inject_llamaindex_http_clients(args, window.core.config)
        
        # 5. Setup remote tools (hook for subclasses)
        args = self._setup_remote_tools(args, window, model)
        
        # 6. Create provider-specific instance
        return self._create_llm_instance(args, window, model)
    
    def _ensure_api_key(self, args: Dict, window) -> Dict:
        """
        Ensure API key is set from config.
        
        Override this method for custom API key logic.
        
        :param args: Arguments dict
        :param window: Window instance
        :return: Updated arguments dict
        """
        if "api_key" not in args or args["api_key"] == "":
            args["api_key"] = window.core.config.get(self._api_key_config, "")
        return args
    
    def _setup_remote_tools(self, args: Dict, window, model: ModelItem) -> Dict:
        """
        Setup remote/built-in tools for provider.
        
        Override this method in subclasses that support remote tools.
        Default implementation does nothing.
        
        :param args: Arguments dict
        :param window: Window instance
        :param model: Model instance
        :return: Updated arguments dict
        """
        return args
    
    @abstractmethod
    def _create_llm_instance(self, args: Dict, window, model: ModelItem) -> LlamaBaseLLM:
        """
        Create provider-specific LLM instance.
        
        Subclasses must implement this to create their specific LLM.
        All common setup (API key, model ID, proxy, remote tools) is already done.
        
        :param args: Prepared arguments dict with API key, model ID, proxy, etc.
        :param window: Window instance
        :param model: Model instance
        :return: Provider-specific LLM instance
        """
        pass
