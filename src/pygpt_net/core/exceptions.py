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
Custom exception hierarchy for PyGPT.

This module defines a hierarchy of custom exceptions used throughout the PyGPT
application. Using specific exception types instead of generic Exception allows
for better error handling, more informative error messages, and easier debugging.

Example usage:
    from pygpt_net.core.exceptions import CameraError
    
    if not camera.is_available():
        raise CameraError("No camera device found")
"""


class PyGPTException(Exception):
    """
    Base exception for PyGPT application.
    
    All custom exceptions in PyGPT should inherit from this base class.
    This allows catching all PyGPT-specific exceptions with a single except clause.
    """
    pass


class ConfigurationError(PyGPTException):
    """
    Configuration-related errors.
    
    Raised when there are issues with application configuration, such as:
    - Missing required configuration values
    - Invalid configuration format
    - Configuration file corruption
    """
    pass


class ProviderError(PyGPTException):
    """
    Provider/API errors.
    
    Raised when there are issues with external service providers, such as:
    - API authentication failures
    - API rate limiting
    - Invalid API responses
    - Provider service unavailability
    """
    pass


class AudioError(PyGPTException):
    """
    Audio input/output errors.
    
    Raised when there are issues with audio operations, such as:
    - Audio device not found
    - Audio format not supported
    - Audio file corruption
    - Audio playback/recording failures
    """
    pass


class CameraError(PyGPTException):
    """
    Camera/video capture errors.
    
    Raised when there are issues with camera operations, such as:
    - Camera device not found
    - Camera initialization failure
    - Invalid camera configuration
    - Frame capture errors
    """
    pass


class FileOperationError(PyGPTException):
    """
    File I/O errors.
    
    Raised when there are issues with file operations, such as:
    - File not found
    - Permission denied
    - File locking issues
    - Disk space errors
    """
    pass


class PluginError(PyGPTException):
    """
    Plugin-related errors.
    
    Raised when there are issues with plugins, such as:
    - Plugin initialization failure
    - Plugin configuration errors
    - Plugin dependency issues
    - Plugin execution errors
    """
    pass


class ModelError(PyGPTException):
    """
    Model-related errors.
    
    Raised when there are issues with AI models, such as:
    - Model not found
    - Model loading failure
    - Invalid model configuration
    - Model inference errors
    """
    pass


class IndexError(PyGPTException):
    """
    Indexing/vector store errors.
    
    Raised when there are issues with document indexing or vector stores, such as:
    - Index creation failure
    - Vector store connection errors
    - Document embedding errors
    - Query execution failures
    """
    pass


class NetworkError(PyGPTException):
    """
    Network/connectivity errors.
    
    Raised when there are issues with network operations, such as:
    - Connection timeout
    - DNS resolution failure
    - Proxy configuration errors
    - SSL/TLS errors
    """
    pass
