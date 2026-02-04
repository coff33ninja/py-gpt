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
Safe file I/O operations with retry logic.

This module provides utilities for safe file operations that handle common
issues like file locking, permission errors, and transient failures through
automatic retry logic with exponential backoff.

Example usage:
    from pygpt_net.core.filesystem.safe_io import SafeFileIO
    
    # Safe file reading with retry
    content = SafeFileIO.safe_read('/path/to/file.txt')
    
    # Safe file writing with retry
    SafeFileIO.safe_write('/path/to/file.txt', 'content')
    
    # Create temporary audio file
    temp_file = SafeFileIO.create_temp_audio_file(suffix='.mp3')
"""

import os
import time
import tempfile
from contextlib import contextmanager
from typing import Optional


class SafeFileIO:
    """
    Safe file I/O operations with retry logic and error handling.
    
    This class provides static methods for performing file operations with
    automatic retry logic to handle transient failures like file locking
    or temporary permission issues.
    """
    
    @staticmethod
    @contextmanager
    def safe_open(
        filepath: str,
        mode: str = 'r',
        max_retries: int = 3,
        retry_delay: float = 0.1,
        encoding: Optional[str] = None
    ):
        """
        Safely open file with retry logic for handling file locking issues
        
        :param filepath: Path to file
        :param mode: File open mode ('r', 'w', 'rb', 'wb', etc.)
        :param max_retries: Maximum retry attempts
        :param retry_delay: Delay between retries in seconds
        :param encoding: File encoding (for text mode)
        :raises: FileOperationError if all retries fail
        """
        last_error = None
        
        for attempt in range(max_retries):
            try:
                kwargs = {}
                if encoding and 'b' not in mode:
                    kwargs['encoding'] = encoding
                
                file_handle = open(filepath, mode, **kwargs)
                try:
                    yield file_handle
                finally:
                    try:
                        file_handle.close()
                    except Exception:
                        pass
                return
                
            except (PermissionError, OSError) as e:
                last_error = e
                if attempt < max_retries - 1:
                    # Exponential backoff
                    time.sleep(retry_delay * (2 ** attempt))
                continue
            except Exception:
                # Unexpected error - don't retry, re-raise
                raise
        
        # All retries failed
        from pygpt_net.core.exceptions import FileOperationError
        raise FileOperationError(
            f"Failed to open {filepath} after {max_retries} attempts: {last_error}"
        )
    
    @staticmethod
    def create_temp_audio_file(suffix: str = '.mp3', prefix: str = 'pygpt_audio_') -> str:
        """
        Create unique temporary audio file
        
        :param suffix: File extension (e.g., '.mp3', '.wav')
        :param prefix: Filename prefix
        :return: Path to temporary file
        """
        fd, path = tempfile.mkstemp(suffix=suffix, prefix=prefix)
        os.close(fd)  # Close file descriptor immediately to avoid locking
        return path
    
    @staticmethod
    def safe_remove(filepath: str, max_retries: int = 3, retry_delay: float = 0.1) -> bool:
        """
        Safely remove file with retry logic
        
        :param filepath: Path to file
        :param max_retries: Maximum retry attempts
        :param retry_delay: Delay between retries in seconds
        :return: True if file was removed, False otherwise
        """
        if not os.path.exists(filepath):
            return True
        
        for attempt in range(max_retries):
            try:
                os.remove(filepath)
                return True
            except (PermissionError, OSError):
                if attempt < max_retries - 1:
                    time.sleep(retry_delay * (2 ** attempt))
                continue
            except Exception:
                # Unexpected error - don't retry
                break
        
        return False
    
    @staticmethod
    def safe_write(
        filepath: str,
        content: str,
        encoding: str = 'utf-8',
        max_retries: int = 3
    ) -> bool:
        """
        Safely write content to file with retry logic
        
        :param filepath: Path to file
        :param content: Content to write
        :param encoding: File encoding
        :param max_retries: Maximum retry attempts
        :return: True if successful, False otherwise
        """
        try:
            with SafeFileIO.safe_open(
                filepath,
                mode='w',
                encoding=encoding,
                max_retries=max_retries
            ) as f:
                f.write(content)
            return True
        except Exception:  # noqa: S110
            # Broad exception catch is intentional - we want to return False for any write failure
            return False
    
    @staticmethod
    def safe_read(
        filepath: str,
        encoding: str = 'utf-8',
        max_retries: int = 3
    ) -> Optional[str]:
        """
        Safely read content from file with retry logic
        
        :param filepath: Path to file
        :param encoding: File encoding
        :param max_retries: Maximum retry attempts
        :return: File content or None if failed
        """
        try:
            with SafeFileIO.safe_open(
                filepath,
                mode='r',
                encoding=encoding,
                max_retries=max_retries
            ) as f:
                return f.read()
        except Exception:  # noqa: S110
            # Broad exception catch is intentional - we want to return None for any read failure
            return None
    
    @staticmethod
    def ensure_directory(dirpath: str) -> bool:
        """
        Ensure directory exists, create if necessary
        
        :param dirpath: Path to directory
        :return: True if directory exists or was created
        """
        try:
            os.makedirs(dirpath, exist_ok=True)
            return True
        except (OSError, PermissionError):
            # Failed to create directory due to permissions or OS error
            return False
