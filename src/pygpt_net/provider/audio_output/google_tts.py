#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.08.07 22:00:00                  #
# ================================================== #
import json
import os
import requests

from .base import BaseProvider


class GoogleTextToSpeech(BaseProvider):
    def __init__(self, *args, **kwargs):
        """
        Google Text to Speech provider

        :param args: args
        :param kwargs: kwargs
        """
        super(GoogleTextToSpeech, self).__init__(*args, **kwargs)
        self.plugin = kwargs.get("plugin")
        self.id = "google"
        self.name = "Google TTS"

    def init_options(self):
        """Initialize options"""
        url_api = {
            "API Key": "https://console.cloud.google.com/apis/library/texttospeech.googleapis.com",
        }
        self.plugin.add_option(
            "google_api_key",
            type="text",
            value="",
            label="Google Cloud Text-to-speech API Key",
            tab="google",
            description="You can obtain your own API key at: "
                        "https://console.cloud.google.com/apis/library/texttospeech.googleapis.com",
            tooltip="Google Text-to-speech API Key",
            secret=True,
            persist=True,
            urls=url_api,
        )
        self.plugin.add_option(
            "google_voice",
            type="text",
            value="en-US-Neural2-J",
            label="Voice",
            tab="google",
            description="Specify voice",
            tooltip="Voice name",
            urls={
                "Voices": "https://cloud.google.com/text-to-speech/docs/voices"
            },
        )
        self.plugin.add_option(
            "google_lang",
            type="text",
            value="en-US",
            label="Language code",
            tab="google",
            description="Specify language code",
            tooltip="Language code",
            urls={
                "Languages": "https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages"
            },
        )

    def speech(self, text: str) -> str:
        """
        Speech text to audio

        :param text: text to speech
        :return: path to generated audio file or None if audio playback is handled here
        """
        api_key = self.plugin.get_option_value("google_api_key")
        lang = self.plugin.get_option_value("google_lang")
        voice = self.plugin.get_option_value("google_voice")
        output_file = self.plugin.generate_audio_file()
        path = os.path.join(
            self.plugin.window.core.config.path,
            output_file,
        )
        url = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
        data = {
            "input": {
                "text": text,
            },
            "voice": {
                "name": voice,
                "languageCode": lang,
            },
            "audioConfig": {
                "audioEncoding": "MP3",
            }
        }
        headers = {
            "content-type": "application/json",
            "X-Goog-Api-Key": api_key,
        }

        r = requests.post(url=url, json=data, headers=headers)
        content = json.loads(r.content)
        
        from pygpt_net.core.filesystem.safe_io import SafeFileIO
        from pygpt_net.core.exceptions import AudioError
        from pygpt_net.core.error_handler import ErrorSeverity
        
        try:
            audio_content = content.get("audioContent")
            if not audio_content:
                error = AudioError("No audio content in response")
                self.window.core.error_handler.handle(
                    error,
                    severity=ErrorSeverity.ERROR,
                    context="Audio generation (Google TTS)",
                    user_message="Failed to generate audio - no content received",
                    recoverable=True
                )
                raise error
            
            # Decode base64 audio content
            import base64
            audio_bytes = base64.b64decode(audio_content)
            
            with SafeFileIO.safe_open(path, "wb", max_retries=3) as file:
                file.write(audio_bytes)
        except AudioError:
            raise  # Re-raise AudioError as-is
        except Exception as e:
            error = AudioError(f"Failed to write audio file {path}: {e}")
            self.window.core.error_handler.handle(
                error,
                severity=ErrorSeverity.ERROR,
                context="Audio file write (Google TTS)",
                user_message="Failed to save audio file",
                recoverable=True
            )
            raise error
        
        return str(path)

    def is_configured(self) -> bool:
        """
        Check if provider is configured

        :return: True if configured, False otherwise
        """
        api_key = self.plugin.get_option_value("google_api_key")
        return api_key is not None and api_key != ""

    def get_config_message(self) -> str:
        """
        Return message to display when provider is not configured

        :return: message
        """
        api_key = self.plugin.get_option_value("google_api_key")
        if api_key is None or api_key == "":
            return "Google API KEY is not set. Please set it in plugin settings."

