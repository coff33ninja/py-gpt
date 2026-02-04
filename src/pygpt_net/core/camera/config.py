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
Camera configuration validation.

This module provides utilities for validating and sanitizing camera configuration
values, ensuring that all camera parameters have valid values with appropriate
defaults and bounds checking.

Example usage:
    from pygpt_net.core.camera.config import CameraConfig
    
    # Get validated camera configuration
    config = CameraConfig.get_validated_config(window)
    
    # Access validated values
    camera_idx = config['idx']
    width = config['width']
    height = config['height']
"""


class CameraConfig:
    """
    Camera configuration with validation and defaults.
    
    This class provides static methods for validating camera configuration
    values and ensuring they fall within acceptable ranges. Invalid values
    are automatically replaced with sensible defaults.
    """
    
    # Default values
    DEFAULT_IDX = 0
    DEFAULT_WIDTH = 640
    DEFAULT_HEIGHT = 480
    DEFAULT_FPS = 30
    
    # Constraints
    MIN_WIDTH = 320
    MAX_WIDTH = 3840
    MIN_HEIGHT = 240
    MAX_HEIGHT = 2160
    MIN_FPS = 1
    MAX_FPS = 60
    
    @staticmethod
    def get_validated_config(window) -> dict:
        """
        Get validated camera configuration with fallback to defaults
        
        :param window: Window instance
        :return: Dictionary with validated camera configuration
        """
        config = window.core.config
        
        return {
            'idx': CameraConfig._validate_int(
                config.get('vision.capture.idx'),
                CameraConfig.DEFAULT_IDX,
                min_val=0
            ),
            'width': CameraConfig._validate_int(
                config.get('vision.capture.width'),
                CameraConfig.DEFAULT_WIDTH,
                min_val=CameraConfig.MIN_WIDTH,
                max_val=CameraConfig.MAX_WIDTH
            ),
            'height': CameraConfig._validate_int(
                config.get('vision.capture.height'),
                CameraConfig.DEFAULT_HEIGHT,
                min_val=CameraConfig.MIN_HEIGHT,
                max_val=CameraConfig.MAX_HEIGHT
            ),
            'fps': CameraConfig._validate_int(
                config.get('vision.capture.fps'),
                CameraConfig.DEFAULT_FPS,
                min_val=CameraConfig.MIN_FPS,
                max_val=CameraConfig.MAX_FPS
            ),
        }
    
    @staticmethod
    def _validate_int(
        value,
        default: int,
        min_val: int = None,
        max_val: int = None
    ) -> int:
        """
        Validate integer configuration value with bounds checking
        
        :param value: Value to validate
        :param default: Default value if validation fails
        :param min_val: Minimum allowed value
        :param max_val: Maximum allowed value
        :return: Validated integer value
        """
        try:
            # Convert to int
            val = int(value) if value is not None else default
            
            # Check bounds
            if min_val is not None and val < min_val:
                return default
            if max_val is not None and val > max_val:
                return default
            
            return val
        except (ValueError, TypeError):
            return default
