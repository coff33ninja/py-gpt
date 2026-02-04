# Google Gemini API Setup & Guide

Complete guide to setting up and using Google's Gemini models in PyGPT, including Gemini 2.5 Flash and Flash Live.

## 📋 Quick Facts

| Aspect | Details |
|--------|---------|
| **Provider** | Google AI |
| **Popular Models** | Gemini 2.5 Flash, 2.5 Flash Live |
| **Free Tier** | ✅ Yes (60 requests/minute) |
| **Setup Time** | ⚡ 2 minutes |
| **Best For** | Fast responses, multi-modal, cost-effective |
| **API Endpoint** | generativelanguage.googleapis.com |

---

## 🚀 Getting Started

### Step 1: Create/Access Google Account
- Have a Google account (Gmail, Google Cloud, etc.)
- Or create one at [accounts.google.com](https://accounts.google.com)

### Step 2: Get API Key (Easiest Way)

#### Option A: Google AI Studio (Recommended for Beginners)
1. Visit [aistudio.google.com](https://aistudio.google.com)
2. Click **"Get API Key"** (top right or in welcome dialog)
3. Click **"Create API key in new project"**
4. Copy the generated API key
5. ✅ Done! Use immediately

**Pros**: Instant, no configuration needed  
**Cons**: Limited to free tier, no billing setup

#### Option B: Google Cloud Console (For Production)
1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create or select a project
3. Enable **Google Generative AI API**:
   - Search "Generative AI"
   - Click and select "Enable"
4. Go to **APIs & Services** → **Credentials**
5. Click **Create Credentials** → **API Key**
6. Copy the key
7. ✅ Ready to use

**Pros**: Full control, can set billing limits  
**Cons**: More steps, need credit card for extended use

---

## 🔌 Adding Gemini to PyGPT

### Method 1: Through PyGPT UI (Easiest)

1. **Open PyGPT**
2. **Settings** (⚙️ icon)
3. Find **"API Keys"** section
4. Locate **"Google API key"** field
5. **Paste your API key**
6. Click **"Save"** or **"Test Connection"**
7. ✅ Success! Green checkmark appears

### Method 2: Configuration File

**File location:**
- Windows: `%APPDATA%\pygpt\config.json`
- Linux: `~/.pygpt/config.json`
- macOS: `~/Library/Application Support/pygpt/config.json`

**Add this line:**
```json
"api_key_google": "your_api_key_here"
```

### Method 3: Environment Variable

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY = "your_api_key_here"
pygpt
```

**Linux/macOS (Bash):**
```bash
export GOOGLE_API_KEY="your_api_key_here"
pygpt
```

---

## 🤖 Gemini Models Explained

### Gemini 2.5 Series (Latest & Recommended)

#### 🚀 Gemini 2.5 Flash
- **Use for**: Most conversations, fast responses
- **Speed**: Very fast ⚡
- **Cost**: Low 💰
- **Quality**: Excellent for most tasks
- **Size**: Optimized for efficiency
- **Best for**: Chat, coding, general questions

```
Recommended settings:
- Model: gemini-2.5-flash
- Temperature: 0.7
- Max tokens: 2048
```

#### 🎤 Gemini 2.5 Flash Live
- **Use for**: Real-time conversations with audio
- **Features**: Native audio input/output
- **Speed**: Real-time streaming
- **Best for**: Voice conversations, interactive discussions
- **Requires**: Audio input device (microphone)

```
Recommended settings:
- Model: gemini-2.5-flash-live
- Enable audio mode in PyGPT
- Configure microphone device
```

#### 🖼️ Gemini 2.5 Flash Image
- **Use for**: Image analysis and understanding
- **Multimodal**: Understands images, text, and context
- **Best for**: Photo analysis, diagram explanation, OCR

```
Recommended settings:
- Model: gemini-2.5-flash-image
- Upload images in chat
```

#### 🖥️ Gemini 2.5 Computer Use
- **Use for**: Automation and computer control
- **Capabilities**: Screen capture, mouse/keyboard control
- **Best for**: Task automation, taking actions on your computer

---

### Gemini 3 Series (Experimental/Preview)

- `gemini-3-flash-preview` - Preview of next generation
- `gemini-3-pro-preview` - More capable but slower
- `gemini-3-pro-image-preview` - Image capabilities preview

⚠️ **Note**: Preview models may change or disappear

---

### Legacy Models (Still Available)

- `gemini-2.0-flash-exp` - Previous fast model
- `gemini-1.5-pro` - Previous advanced model
- Others...

---

## 💬 Using Gemini in PyGPT

### Select Gemini Model
1. Main chat window, find **Model** dropdown
2. Search for "gemini"
3. Select desired model:
   - `gemini-2.5-flash` (recommended)
   - `gemini-2.5-flash-live` (for audio)
   - `gemini-2.5-flash-image` (for images)
4. Start chatting!

### Basic Chat
```
You: What are the benefits of renewable energy?
Gemini: Renewable energy offers several benefits...
```

### Code Generation
```
You: Write a Python function to calculate factorial
Gemini: def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
```

### Image Analysis
```
1. Click image/attachment button
2. Upload image
3. Ask: "What's in this image?"
4. Gemini analyzes and responds
```

### With Web Search
```
You: What are today's top news stories?
Gemini: [Uses web search if enabled] Today's headlines are...
```

---

## ⚙️ Advanced Configuration

### Native API Configuration

PyGPT supports Google's native GenAI SDK for advanced features:

**Settings → Google Native API Settings:**

```
- Use native API SDK: [Toggle]
- Use VertexAI: [Toggle] (for enterprise)
- Cloud Project: [Project ID]
- Cloud Location: [e.g., us-central1]
- Application Credentials: [Path to service account JSON]
```

### API Endpoint Configuration
If you need a custom endpoint:

Settings → **API Endpoint (Google)**
```
Default: https://generativelanguage.googleapis.com/v1beta/openai
```

### Rate Limiting
- **Free tier**: 60 requests/minute
- **Paid tier**: Depends on quota

---

## 💰 Pricing & Free Tier

### Free Tier (Google AI Studio)
- ✅ 60 requests per minute
- ✅ Access to latest models
- ✅ No credit card required
- ⚠️ Limited capacity during peak times
- ⚠️ No SLA/guaranteed availability

### Paid Tier (Google Cloud)
- 💵 Pay-per-use pricing
- ✅ Higher rate limits
- ✅ SLA/support included
- ✅ Set spending limits
- Visit [ai.google.dev/pricing](https://ai.google.dev/pricing)

**Estimated costs:**
- Chat: $0.075 per million input tokens
- Images: ~$2-10 per 1M images
- Free tier covers most casual use

---

## 🎯 Use Cases & Examples

### Use Case 1: Content Creation
```
Model: gemini-2.5-flash
Temperature: 0.8 (more creative)

Prompt: "Write a blog post about AI trends"
Response: Well-written blog post with current insights
```

### Use Case 2: Code Help
```
Model: gemini-2.5-flash
Temperature: 0.3 (more deterministic)

Prompt: "Debug this Python code: [code]"
Response: Identifies errors and fixes
```

### Use Case 3: Document Analysis
```
Model: gemini-2.5-flash-image
Upload: PDF or document image
Prompt: "Summarize this document"
```

### Use Case 4: Real-time Discussion
```
Model: gemini-2.5-flash-live
Audio enabled
Speak naturally, get real-time responses
```

---

## 🔒 Security & Best Practices

### API Key Safety
- ✅ Never share your API key
- ✅ Don't commit to GitHub
- ✅ Store in environment variables or config files
- ✅ Regenerate if accidentally exposed
- ✅ Use read-only permissions when possible

### Rate Limiting
- Implement delays for batch operations
- Monitor usage in Google Cloud Console
- Set billing alerts/caps

### Data Privacy
- Conversations sent to Google's servers
- Review [Google AI Privacy](https://ai.google.dev/privacy)
- Data may be used for improvement (can opt-out)

---

## 🐛 Troubleshooting

### Issue: "Invalid API Key"
**Solutions:**
- ✓ Copy full key with no spaces
- ✓ Key must be from recent generation (recent keys only)
- ✓ Regenerate key if very old
- ✓ Check you're using the right key

### Issue: "Quota Exceeded"
**Solutions:**
- ✓ Wait for quota reset (1 hour for free tier)
- ✓ Upgrade to paid tier
- ✓ Reduce request frequency
- ✓ Check Google Cloud Console for limits

### Issue: "Model Not Found"
**Solutions:**
- ✓ Verify model name spelling
- ✓ Some preview models have limited availability
- ✓ Try `gemini-2.5-flash` as fallback
- ✓ Update PyGPT to get latest models

### Issue: Audio Not Working (Flash Live)
**Solutions:**
- ✓ Check microphone permissions
- ✓ Select correct audio input device
- ✓ Test microphone in system settings
- ✓ Try different browser if web version

### Issue: Image Analysis Fails
**Solutions:**
- ✓ Ensure image is <20MB
- ✓ Use common formats (JPEG, PNG, WebP, GIF)
- ✓ Check image displays correctly
- ✓ Try different image

---

## 📊 Comparing Models

| Feature | Flash | Flash Live | Flash Image | 3 Pro |
|---------|-------|-----------|------------|-------|
| **Speed** | ⚡ Very Fast | ⚡⚡ Real-time | ⚡ Fast | 🐢 Slower |
| **Cost** | 💰 Low | 💰 Low | 💰 Low | 💵 Higher |
| **Quality** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Code** | ✅ Good | ✅ Good | ✅ Good | ✅ Excellent |
| **Images** | ⚠️ Limited | ⚠️ Limited | ✅ Optimized | ✅ Excellent |
| **Audio** | ❌ No | ✅ Yes | ❌ No | ✅ Yes |
| **General** | ✅ Best | ⚠️ Specific | ⚠️ Specific | ✅ Excellent |

**Recommendation for most users**: Start with `gemini-2.5-flash`

---

## 🔗 Useful Resources

- 📖 [Gemini API Docs](https://ai.google.dev)
- 🤖 [Model List](https://ai.google.dev/models/gemini)
- 💰 [Pricing](https://ai.google.dev/pricing)
- 🔑 [API Key Setup](https://aistudio.google.com)
- 📚 [Documentation](https://ai.google.dev/docs)

---

## ✅ Quick Checklist

- [ ] ✅ API key obtained from AI Studio or Cloud Console
- [ ] ✅ Added to PyGPT Settings
- [ ] ✅ Tested connection (green checkmark)
- [ ] ✅ Selected model (gemini-2.5-flash recommended)
- [ ] ✅ Sent test message
- [ ] ✅ Received response

---

## Next Steps

- 🚀 [First Steps Guide](../getting-started/02-first-steps.md)
- 📘 [Advanced Configuration](../guides/07-advanced-settings.md)
- 🖼️ [Vision & Images](../features/vision-images.md)
- 🎤 [Audio & Voice](../guides/04-audio-voice.md)

---

**Happy chatting with Gemini!** 🚀
