# Realtime + Audio Mode

Native real-time audio communication with AI models.

## 🎤 Overview

Realtime + Audio mode provides native support for audio input and output using Realtime and Live APIs. Audio is processed directly by the model without external plugins, enabling:
- Faster audio communication
- Better audio understanding
- Natural conversation flow
- Real-time responses
- Voice-to-voice interaction

**Status:** Beta  
**Supported Providers:** OpenAI (Realtime API), Google (Live API), xAI (Grok)

## 🆚 vs Regular Audio Mode

### Realtime + Audio Mode
- ✅ Native audio processing
- ✅ Faster response times
- ✅ Better audio understanding
- ✅ Streaming audio output
- ✅ Natural conversation flow
- ✅ No transcription delay

### Regular Audio Mode (Plugins)
- Uses Whisper for transcription
- Uses TTS for speech synthesis
- Two-step process (transcribe → respond → synthesize)
- Higher latency
- More flexible provider options

## 🚀 Getting Started

### Prerequisites

1. **Supported Model**
   - OpenAI: `gpt-realtime`, `gpt-4o-realtime-preview`
   - Google: `gemini-2.5-flash-preview-native-audio-dialog`
   - xAI: Grok models with audio support

2. **API Key**
   - Configure in `Config → Settings → API Keys`

3. **Microphone**
   - Working microphone
   - Proper permissions granted

4. **Audio Output**
   - Speakers or headphones
   - System audio configured

### Enable Realtime + Audio Mode

1. Launch PyGPT
2. Select mode: **Realtime + Audio**
3. Choose a compatible model
4. Click microphone icon to start

## 🎯 Use Cases

### Voice Conversations
```
Natural back-and-forth dialogue:
- Ask questions verbally
- Get spoken responses
- Interrupt and clarify
- Natural conversation flow
```

### Language Learning
```
Practice speaking:
- Pronunciation feedback
- Conversation practice
- Real-time corrections
- Natural dialogue
```

### Hands-Free Operation
```
Use while:
- Driving (safely)
- Cooking
- Exercising
- Working with hands
```

### Accessibility
```
For users who:
- Prefer voice interaction
- Have visual impairments
- Have mobility limitations
- Find typing difficult
```

## ⚙️ Configuration

### Settings Location
`Config → Settings → Audio`

### Audio Input Settings

**Input Device**
- Select microphone
- Default: System default
- Test before use

**Input Volume**
- Adjust sensitivity
- Default: 100%
- Reduce if too sensitive

**Voice Activation**
- Auto-detect speech
- Manual push-to-talk
- Configurable threshold

### Audio Output Settings

**Output Device**
- Select speakers/headphones
- Default: System default
- Test audio playback

**Output Volume**
- Adjust volume
- Default: 100%
- Independent from system

**Voice Selection**
- Choose AI voice (if supported)
- Male/female options
- Language-specific voices

### Realtime Settings

**Loop Mode**
- Automatic turn handling
- Continuous conversation
- No manual microphone enable
- Default: Disabled

**Auto-Response**
- AI responds immediately
- No confirmation needed
- Natural flow

**Interrupt Handling**
- Allow interruptions
- Stop AI when user speaks
- More natural dialogue

## 🎨 Features

### Loop Mode

Enables continuous conversation without manually enabling the microphone each time.

**How it works:**
1. Enable Loop Mode
2. Start conversation
3. AI listens continuously
4. Responds automatically
5. Listens for next input
6. Repeats indefinitely

**Use cases:**
- Extended conversations
- Hands-free operation
- Natural dialogue flow

**Enable Loop Mode:**
```
Config → Settings → Audio → Loop Mode: Enabled
```

### Voice Activity Detection

Automatically detects when you're speaking.

**Features:**
- Auto-start recording
- Auto-stop when silent
- Configurable sensitivity
- Background noise filtering

**Configuration:**
```
Config → Settings → Audio → Voice Activation
- Threshold: Adjust sensitivity
- Silence Duration: Time before stopping
```

### Mute/Unmute

Control audio output during conversation.

**How to mute:**
- Click audio icon in toolbar
- Press configured hotkey
- Mutes AI voice output
- Continues listening

**Use cases:**
- Temporary silence
- Private moments
- Reduce distractions

## 🔧 Supported Models

### OpenAI Realtime API

**Models:**
- `gpt-realtime` (latest)
- `gpt-4o-realtime-preview`

**Features:**
- Low latency
- Natural voices
- Streaming audio
- Function calling support

**Configuration:**
```
Mode: Realtime + Audio
Model: gpt-realtime
Provider: OpenAI
```

### Google Live API

**Models:**
- `gemini-2.5-flash-preview-native-audio-dialog`

**Features:**
- Fast responses
- Multiple languages
- Natural conversation
- Context awareness

**Configuration:**
```
Mode: Realtime + Audio
Model: gemini-2.5-flash-preview-native-audio-dialog
Provider: Google
```

### xAI Grok

**Models:**
- Grok models with audio support

**Features:**
- Real-time processing
- Natural dialogue
- Context retention

**Configuration:**
```
Mode: Realtime + Audio
Model: grok-audio (or compatible)
Provider: xAI
```

## 📋 Audio Providers

### Input Providers

**OpenAI Whisper**
- High accuracy
- 50+ languages
- Cloud-based

**Google Speech Recognition**
- Fast processing
- Good accuracy
- Cloud-based

**Microsoft Speech Recognition**
- Windows integration
- Good accuracy
- Cloud-based

### Output Providers

**OpenAI TTS**
- Natural voices
- Multiple languages
- High quality

**Google TTS**
- Fast synthesis
- Many voices
- Good quality

**Microsoft Azure TTS**
- Natural voices
- Many languages
- High quality

**Eleven Labs**
- Most natural voices
- Premium quality
- Requires separate API key

## 🎨 Examples

### Example 1: Simple Conversation
```
User: [Speaks] "What's the weather like today?"
AI: [Speaks] "I don't have access to real-time weather data, 
     but I can help you find that information. Would you like 
     me to search for the weather in your location?"
User: [Speaks] "Yes, please"
AI: [Speaks] "I'll need to know your location. What city 
     are you in?"
```

### Example 2: Language Learning
```
User: [Speaks in Spanish] "¿Cómo estás?"
AI: [Speaks in Spanish] "¡Estoy bien, gracias! ¿Y tú? 
     Your pronunciation is good. Would you like to 
     practice more Spanish conversation?"
User: [Speaks] "Yes, let's continue in Spanish"
AI: [Speaks in Spanish] "Perfecto. ¿Qué hiciste hoy?"
```

### Example 3: Hands-Free Coding
```
User: [Speaks] "Create a Python function to calculate 
       the Fibonacci sequence"
AI: [Speaks] "I'll create that function for you. 
     Here's a Python function that calculates the 
     Fibonacci sequence..." [Shows code]
User: [Speaks] "Add error handling for negative numbers"
AI: [Speaks] "Good idea. I'll add that now..." [Updates code]
```

## 🐛 Troubleshooting

### No Audio Input
**Problem:** Microphone not working

**Solutions:**
- Check microphone permissions
- Select correct input device
- Test microphone in system settings
- Restart PyGPT

### No Audio Output
**Problem:** Can't hear AI responses

**Solutions:**
- Check speaker/headphone connection
- Select correct output device
- Adjust volume in settings
- Test system audio

### Poor Audio Quality
**Problem:** Distorted or unclear audio

**Solutions:**
- Check microphone quality
- Reduce background noise
- Adjust input volume
- Use better microphone

### High Latency
**Problem:** Slow responses

**Solutions:**
- Check internet connection
- Use faster model
- Reduce audio quality
- Close other applications

### Audio Cutting Out
**Problem:** Audio stops mid-sentence

**Solutions:**
- Check internet stability
- Increase buffer size
- Reduce audio quality
- Restart connection

## 💡 Best Practices

### Speak Clearly
```
✅ Clear, moderate pace
✅ Proper pronunciation
✅ Minimal background noise
❌ Mumbling or too fast
❌ Noisy environment
```

### Use Natural Language
```
✅ "Can you help me with this code?"
✅ "What's the capital of France?"
❌ "help code"
❌ "capital france"
```

### Wait for Response
```
✅ Let AI finish speaking
✅ Pause before next question
❌ Interrupt mid-sentence
❌ Rapid-fire questions
```

### Optimize Environment
```
✅ Quiet room
✅ Good microphone
✅ Stable internet
❌ Noisy background
❌ Poor connection
```

## 🔗 Related Features

- [Audio & Voice Guide](../guides/04-audio-voice.md) - Audio setup
- [Chat Mode](../guides/01-chat-modes.md) - Text-based chat
- [Accessibility](../reference/accessibility.md) - Accessibility features

## 📚 Additional Resources

- [OpenAI Realtime API](https://platform.openai.com/docs/guides/realtime)
- [Google Live API](https://ai.google.dev/gemini-api/docs/live-api)
- [Audio Configuration Guide](../guides/04-audio-voice.md)

## ⚠️ Limitations

- **Internet required** - Cloud-based processing
- **Latency** - Slight delay in responses
- **Language support** - Varies by provider
- **Cost** - API usage charges apply
- **Quality** - Depends on microphone/connection

## 🆘 Need Help?

- Check [Audio & Voice Guide](../guides/04-audio-voice.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Research Mode](./research.md) →
