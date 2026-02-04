#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.11 14:00:00                  #
# ================================================== #

from PySide6.QtCore import QRunnable, Slot, QObject, Signal


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            self.fn(*self.args, **self.kwargs)
        except (OSError, RuntimeError, PermissionError) as e:
            from pygpt_net.core.error_handler import ErrorSeverity
            if hasattr(self, 'window') and self.window and hasattr(self.window.core, 'error_handler'):
                self.window.core.error_handler.handle(
                    e,
                    severity=ErrorSeverity.ERROR,
                    context="Worker execution",
                    recoverable=True,
                    show_dialog=False
                )
        except Exception as e:
            from pygpt_net.core.error_handler import ErrorSeverity
            if hasattr(self, 'window') and self.window and hasattr(self.window.core, 'error_handler'):
                self.window.core.error_handler.handle(
                    e,
                    severity=ErrorSeverity.ERROR,
                    context="Worker execution - unexpected error",
                    recoverable=True,
                    show_dialog=False
                )
        finally:
            self.cleanup()

    def cleanup(self):
        """Cleanup resources after worker execution."""
        sig = self.signals
        self.signals = None
        if sig is not None:
            try:
                sig.deleteLater()
            except RuntimeError:
                pass


class WorkerSignals(QObject):
    updated = Signal(object)
    finished = Signal(object)
