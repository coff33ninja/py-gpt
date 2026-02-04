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
Centralized error handling system.

This module provides a centralized error handler that manages all errors
throughout the application, providing consistent error logging, user
notifications, and error recovery strategies.

Example usage:
    from pygpt_net.core.error_handler import ErrorHandler, ErrorSeverity
    
    handler = ErrorHandler(window)
    
    try:
        # Some operation
        pass
    except Exception as e:
        handler.handle(
            e,
            severity=ErrorSeverity.ERROR,
            context="File operation",
            user_message="Failed to save file",
            recoverable=True
        )
"""

import traceback
from enum import Enum
from typing import Optional, Callable, List, Dict, Any


class ErrorSeverity(Enum):
    """
    Error severity levels.
    
    Defines the severity of errors for appropriate handling and logging.
    """
    DEBUG = 1      # Debug information, not shown to users
    INFO = 2       # Informational messages
    WARNING = 3    # Warning messages, operation continues
    ERROR = 4      # Error messages, operation may fail
    CRITICAL = 5   # Critical errors, application may need to restart


class ErrorHandler:
    """
    Centralized error handling system.
    
    Provides consistent error handling across the application with:
    - Structured error logging
    - User notifications
    - Error callbacks
    - Recovery strategies
    """
    
    def __init__(self, window=None):
        """
        Initialize error handler.
        
        :param window: Window instance for UI integration
        """
        self.window = window
        self.error_callbacks: List[Callable] = []
        self.error_history: List[Dict[str, Any]] = []
        self.max_history = 100
        self.suppress_dialogs = False  # For testing or batch operations
        
    def handle(
        self,
        error: Exception,
        severity: ErrorSeverity = ErrorSeverity.ERROR,
        context: Optional[str] = None,
        user_message: Optional[str] = None,
        recoverable: bool = True,
        show_dialog: bool = None,
        log_traceback: bool = True
    ) -> bool:
        """
        Handle an error with appropriate logging and user notification.
        
        :param error: The exception that occurred
        :param severity: Error severity level
        :param context: Context where error occurred (e.g., "Camera initialization")
        :param user_message: User-friendly error message
        :param recoverable: Whether the application can continue
        :param show_dialog: Override dialog display (None = auto based on severity)
        :param log_traceback: Whether to log full traceback
        :return: True if error was handled successfully
        """
        # Build error record
        error_record = {
            'error': error,
            'severity': severity,
            'context': context or 'Unknown context',
            'user_message': user_message,
            'recoverable': recoverable,
            'error_type': type(error).__name__,
            'error_message': str(error),
        }
        
        # Add to history
        self._add_to_history(error_record)
        
        # Log the error
        self._log_error(error, severity, context, log_traceback)
        
        # Show user notification if needed
        if show_dialog is None:
            show_dialog = severity >= ErrorSeverity.WARNING and not self.suppress_dialogs
        
        if show_dialog and user_message:
            self._notify_user(user_message, severity)
        
        # Call registered callbacks
        self._call_callbacks(error_record)
        
        # Handle critical errors
        if not recoverable:
            self._handle_critical_error(error, context)
            return False
        
        return True
    
    def _log_error(
        self,
        error: Exception,
        severity: ErrorSeverity,
        context: Optional[str],
        log_traceback: bool
    ):
        """
        Log error with full context.
        
        :param error: The exception
        :param severity: Error severity
        :param context: Error context
        :param log_traceback: Whether to log traceback
        """
        error_type = type(error).__name__
        error_msg = str(error)
        context_str = context or 'Unknown context'
        
        log_msg = f"[{severity.name}] {context_str}: {error_type}: {error_msg}"
        
        if self.window and hasattr(self.window.core, 'debug'):
            self.window.core.debug.log(log_msg)
            
            # Log full traceback for errors and critical issues
            if log_traceback and severity >= ErrorSeverity.ERROR:
                tb = traceback.format_exc()
                self.window.core.debug.log(f"Traceback:\n{tb}")
        else:
            # Fallback to print if debug system not available
            print(log_msg)
            if log_traceback and severity >= ErrorSeverity.ERROR:
                traceback.print_exc()
    
    def _notify_user(self, message: str, severity: ErrorSeverity):
        """
        Show user-friendly notification.
        
        :param message: User message
        :param severity: Error severity
        """
        if not self.window or not hasattr(self.window, 'ui'):
            return
        
        try:
            if severity == ErrorSeverity.CRITICAL:
                # Show modal dialog for critical errors
                if hasattr(self.window.ui, 'dialogs'):
                    self.window.ui.dialogs.alert(message)
            elif severity == ErrorSeverity.ERROR:
                # Show error in status bar or notification
                if hasattr(self.window.ui, 'status'):
                    self.window.ui.status(f"Error: {message}")
            elif severity == ErrorSeverity.WARNING:
                # Show warning in status bar
                if hasattr(self.window.ui, 'status'):
                    self.window.ui.status(f"Warning: {message}")
        except Exception as e:
            # Don't let notification errors crash the app
            print(f"Failed to show user notification: {e}")
    
    def _call_callbacks(self, error_record: Dict[str, Any]):
        """
        Call registered error callbacks.
        
        :param error_record: Error information
        """
        for callback in self.error_callbacks:
            try:
                callback(error_record)
            except Exception as e:
                # Don't let callback errors crash the app
                print(f"Error in error callback: {e}")
    
    def _handle_critical_error(self, error: Exception, context: Optional[str]):
        """
        Handle unrecoverable critical errors.
        
        :param error: The exception
        :param context: Error context
        """
        # Log critical error
        print(f"CRITICAL ERROR in {context or 'unknown context'}: {error}")
        traceback.print_exc()
        
        # Try to save application state
        if self.window:
            try:
                self._save_emergency_state()
            except Exception as e:
                print(f"Failed to save emergency state: {e}")
        
        # Show critical error dialog
        if self.window and hasattr(self.window.ui, 'dialogs'):
            try:
                self.window.ui.dialogs.alert(
                    f"Critical error: {error}\n\n"
                    f"The application may need to restart.\n"
                    f"Please check the logs for details."
                )
            except Exception:
                pass
    
    def _save_emergency_state(self):
        """Save application state during critical error."""
        if not self.window:
            return
        
        try:
            # Try to save current context
            if hasattr(self.window.core, 'ctx'):
                self.window.core.ctx.save()
            
            # Try to save configuration
            if hasattr(self.window.core, 'config'):
                self.window.core.config.save()
        except Exception as e:
            print(f"Failed to save emergency state: {e}")
    
    def _add_to_history(self, error_record: Dict[str, Any]):
        """
        Add error to history.
        
        :param error_record: Error information
        """
        import datetime
        error_record['timestamp'] = datetime.datetime.now()
        
        self.error_history.append(error_record)
        
        # Trim history if too large
        if len(self.error_history) > self.max_history:
            self.error_history = self.error_history[-self.max_history:]
    
    def register_callback(self, callback: Callable):
        """
        Register an error callback.
        
        :param callback: Callback function that receives error_record dict
        """
        if callback not in self.error_callbacks:
            self.error_callbacks.append(callback)
    
    def unregister_callback(self, callback: Callable):
        """
        Unregister an error callback.
        
        :param callback: Callback function to remove
        """
        if callback in self.error_callbacks:
            self.error_callbacks.remove(callback)
    
    def get_recent_errors(
        self,
        count: int = 10,
        severity: Optional[ErrorSeverity] = None
    ) -> List[Dict[str, Any]]:
        """
        Get recent errors from history.
        
        :param count: Number of errors to return
        :param severity: Filter by severity (None = all)
        :return: List of error records
        """
        errors = self.error_history
        
        if severity:
            errors = [e for e in errors if e['severity'] == severity]
        
        return errors[-count:]
    
    def clear_history(self):
        """Clear error history."""
        self.error_history.clear()
    
    def set_suppress_dialogs(self, suppress: bool):
        """
        Suppress error dialogs (useful for testing or batch operations).
        
        :param suppress: Whether to suppress dialogs
        """
        self.suppress_dialogs = suppress


class ErrorContext:
    """
    Context manager for error handling.
    
    Provides a convenient way to handle errors in a specific context.
    
    Example:
        with ErrorContext(handler, "File operation", "Failed to save file"):
            # Code that might raise exceptions
            save_file()
    """
    
    def __init__(
        self,
        handler: ErrorHandler,
        context: str,
        user_message: str,
        severity: ErrorSeverity = ErrorSeverity.ERROR,
        recoverable: bool = True
    ):
        """
        Initialize error context.
        
        :param handler: ErrorHandler instance
        :param context: Context description
        :param user_message: User-friendly message
        :param severity: Error severity
        :param recoverable: Whether errors are recoverable
        """
        self.handler = handler
        self.context = context
        self.user_message = user_message
        self.severity = severity
        self.recoverable = recoverable
    
    def __enter__(self):
        """Enter context."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit context and handle any exceptions.
        
        :param exc_type: Exception type
        :param exc_val: Exception value
        :param exc_tb: Exception traceback
        :return: True if exception was handled
        """
        if exc_type is not None:
            self.handler.handle(
                exc_val,
                severity=self.severity,
                context=self.context,
                user_message=self.user_message,
                recoverable=self.recoverable
            )
            return self.recoverable  # Suppress exception if recoverable
        return False
