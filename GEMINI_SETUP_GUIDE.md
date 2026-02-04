# PyGPT Gemini API Setup Guide

## Overview
PyGPT supports Google Gemini models including **Gemini 2.5 Flash** and **Gemini 2.5 Flash Live** through the Google GenAI SDK integration.

## Getting Your Google API Key

### Step 1: Create a Google Cloud Account
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Create a new project or select an existing one
3. Enable the **Google Generative AI API**

### Step 2: Generate an API Key
1. In Google Cloud Console, navigate to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **API Key**
3. Copy the generated API key
4. ⚠️ **Important**: Keep this key private and secure!

### Step 3: Alternative - Google AI Studio (Simpler)
For quick setup without Google Cloud account:
1. Go to [Google AI Studio](https://aistudio.google.com)
2. Click **Get API Key** or navigate to **Get API key in Google Cloud**
3. Follow the guided setup
4. Copy your API key

## Configuring Gemini in PyGPT

### Method 1: Through PyGPT Settings UI

1. **Launch PyGPT**
2. Open **Settings** (usually in menu or preferences)
3. Navigate to **API Keys** or **Models**
4. Find the **Google API Key** field
5. Paste your API key
6. Save settings

### Method 2: Configuration File
PyGPT stores configuration in:
- **Windows**: `%APPDATA%\pygpt` or `~\.pygpt`
- **Linux**: `~/.pygpt`
- **macOS**: `~/Library/Application Support/pygpt`

Edit the configuration file and add:
```
api_key_google = your_api_key_here
```

### Method 3: Environment Variable
Set the environment variable before launching PyGPT:
```bash
# Windows (PowerShell)
$env:GOOGLE_API_KEY = "your_api_key_here"

# Linux/macOS (Bash)
export GOOGLE_API_KEY="your_api_key_here"
```

## Available Gemini Models

### Gemini 2.5 Series (Latest)
- **`gemini-2.5-flash`** - Fast, multi-modal, optimized for speed
- **`gemini-2.5-flash-live`** - Real-time audio interaction model
- **`gemini-2.5-flash-image`** - Optimized for image analysis
- **`gemini-2.5-flash-image-preview`** - Image capabilities preview
- **`gemini-2.5-flash-preview-native-audio-dialog`** - Native audio dialog
- **`gemini-2.5-flash-native-audio-latest`** - Latest audio model
- **`gemini-2.5-computer-use-preview-10-2025`** - Computer use/automation

### Gemini 3 Series (Experimental)
- `gemini-3-flash-preview`
- `gemini-3-pro-preview`
- `gemini-3-pro-image-preview`

### Legacy Models
- `gemini-2.0-flash-exp`
- `gemini-1.5-pro`
- And others

## Using Gemini in PyGPT

### 1. Selecting the Model
1. Open PyGPT
2. Look for the **Model** dropdown in the chat interface
3. Search for and select your desired Gemini model (e.g., `gemini-2.5-flash`)
4. Start chatting!

### 2. Recommended Configurations

#### For Fast Chat Responses
- **Model**: `gemini-2.5-flash`
- **Temperature**: 0.7 (default)
- **Max Tokens**: 2048

#### For Real-time Audio Conversation
- **Model**: `gemini-2.5-flash-live`
- Enable **Audio Mode** in settings
- Configure microphone input device

#### For Image Analysis
- **Model**: `gemini-2.5-flash-image` or `gemini-2.5-flash`
- Upload images in the chat
- Gemini will automatically analyze them

#### For Vision/Computer Use
- **Model**: `gemini-2.5-computer-use-preview-10-2025`
- Enable appropriate permissions for screen capture
- Use for automation tasks

## Key Features with Gemini

### Supported Capabilities
- ✅ **Chat & Conversations** - Full multi-turn dialogue
- ✅ **Vision/Image Analysis** - Analyze uploaded images
- ✅ **Real-time Audio** - Using `gemini-2.5-flash-live`
- ✅ **Code Generation** - Generate and explain code
- ✅ **File Processing** - Process various file types
- ✅ **Web Grounding** - Search the internet for context
- ✅ **Function Calling** - Execute tools and commands
- ✅ **Token Counting** - Built-in token calculation

### LlamaIndex Integration
PyGPT integrates Gemini with LlamaIndex for:
- **Chat with Files**: Analyze documents, PDFs, and data
- **Vector Store Integration**: Embed and query your own documents
- **Multi-modal RAG**: Retrieve and generate with images and text

## Native API SDK Configuration

PyGPT also supports using **VertexAI** for enterprise deployments:

### Enable VertexAI
1. In Settings, find **Google Native API Settings**
2. Enable **Use native API SDK** and **Use VertexAI**
3. Configure:
   - **Google Cloud Project**: Your project ID
   - **Google Cloud Location**: (e.g., `us-central1`)
   - **Application Credentials**: Path to service account JSON

## Troubleshooting

### Issue: "Invalid API Key"
- ✓ Verify key is copied correctly (no extra spaces)
- ✓ Check key has API enabled in Google Cloud Console
- ✓ Ensure key hasn't been regenerated

### Issue: "Model not found"
- ✓ Verify model name is correct
- ✓ Some preview models may have limited availability
- ✓ Try `gemini-2.5-flash` as a stable fallback

### Issue: "Quota Exceeded"
- ✓ Check your Google Cloud Console for quota limits
- ✓ Upgrade your billing account if necessary
- ✓ Consider rate limiting in PyGPT settings

### Issue: "Permission Denied"
- ✓ Regenerate API key in Google AI Studio or Cloud Console
- ✓ Ensure key is not restricted to specific APIs
- ✓ Check firewall/proxy settings if behind corporate network

## Best Practices

1. **Security**
   - Never share your API key
   - Use environment variables instead of hardcoding
   - Regularly rotate keys in production

2. **Cost Optimization**
   - Use `gemini-2.5-flash` for most tasks (faster, cheaper)
   - Reserve larger models for complex reasoning
   - Monitor token usage in PyGPT debug settings

3. **Performance**
   - Enable streaming for faster response display
   - Use appropriate model for task complexity
   - Configure context window based on your needs

4. **Integration**
   - Enable LlamaIndex for document analysis
   - Use embeddings for better search quality
   - Configure plugins for extended functionality

## Pricing
Visit [Google AI Pricing](https://ai.google.dev/pricing) for current rates.
- Generally affordable with free tier available
- Pay-as-you-go for higher volumes
- Includes image and video analysis capabilities

## Additional Resources

- [Google Generative AI Documentation](https://ai.google.dev)
- [Gemini Models Guide](https://ai.google.dev/models/gemini)
- [PyGPT Documentation](https://pygpt.readthedocs.io/)
- [PyGPT GitHub](https://github.com/szczyglis-dev/py-gpt)

## Quick Start Summary

1. Get API key from [Google AI Studio](https://aistudio.google.com)
2. Paste in PyGPT Settings under "Google API key"
3. Select `gemini-2.5-flash` or `gemini-2.5-flash-live` from Models
4. Start using Gemini immediately!

Happy chatting with Gemini! 🚀
