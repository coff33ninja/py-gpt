# API Key Setup Guide for All Providers

Master guide to setting up API keys for all supported AI providers in PyGPT.

## 🎯 Quick Comparison

| Provider | Free? | Setup | Popular Models |
|----------|-------|-------|-----------------|
| **🔵 Google Gemini** | ✅ Yes | 2 min | Gemini 2.5 Flash |
| **🟠 OpenAI** | ❌ Paid | 5 min | GPT-4, GPT-4o, o1 |
| **🟣 Anthropic** | ❌ Paid | 5 min | Claude 3 Opus |
| **🟦 DeepSeek** | ❌ Paid | 5 min | DeepSeek-V3 |
| **🟩 Mistral** | ❌ Paid | 5 min | Mistral Large |
| **🟨 Local (Ollama)** | ✅ Free | 10 min | Llama 3, Mistral |
| **🟪 HuggingFace** | ✅ Free | 5 min | Any model |
| **🟥 xAI** | ❌ Paid | 5 min | Grok |

## ✅ Provider Guides

### 🌟 Recommended: Google Gemini

**Why start here?**
- Free tier available
- Fast setup
- Excellent models
- No credit card required

[→ Full Gemini Setup Guide](./gemini.md)

**Quick start:**
1. Go to [aistudio.google.com](https://aistudio.google.com)
2. Click "Get API Key"
3. Copy key
4. Paste in PyGPT Settings → Google API key

---

### 🟠 OpenAI (ChatGPT, GPT-4)

**What you get:**
- Best for reasoning
- GPT-4o, o1, o3 models
- Industry standard

**Cost:** Paid (no free tier, but affordable)

**Setup:**
1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up or log in
3. Add credit card (required)
4. Go to API Keys
5. Create new key
6. Paste in PyGPT Settings → OpenAI API key

**Recommended model:** `gpt-4o` (best value)

[→ More OpenAI Details](./openai.md)

---

### 🟣 Anthropic Claude

**What you get:**
- Great reasoning
- Safe and reliable
- Good for analysis

**Cost:** Paid

**Setup:**
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up
3. Add payment method
4. Go to API Keys
5. Create key
6. Paste in PyGPT Settings → Anthropic API key

**Recommended model:** `claude-3-opus`

[→ More Anthropic Details](./anthropic.md)

---

### 🟦 DeepSeek

**What you get:**
- Advanced reasoning (R1)
- Fast models (V3)
- Competitive pricing

**Setup:**
1. Go to [platform.deepseek.com](https://platform.deepseek.com)
2. Register account
3. Add credit card
4. Go to API Keys
5. Create new key
6. Paste in PyGPT Settings → DeepSeek API key

**Recommended model:** `deepseek-chat` or `deepseek-reasoner`

[→ More DeepSeek Details](./deepseek.md)

---

### 🟩 Mistral AI

**What you get:**
- Fast models
- Open source friendly
- Good value

**Setup:**
1. Go to [console.mistral.ai](https://console.mistral.ai)
2. Register
3. Add billing info
4. Create API key
5. Paste in PyGPT Settings → Mistral API key

**Recommended model:** `mistral-large`

[→ More Mistral Details](./mistral.md)

---

### 🟨 Local Models (Ollama) - FREE!

**What you get:**
- Run AI locally on your computer
- Completely free
- Privacy (no data sent to servers)
- Works offline

**Setup:**
1. Download [Ollama](https://ollama.ai)
2. Install and run
3. Download model: `ollama pull llama2`
4. Select in PyGPT → Model dropdown

**Popular models:**
- `llama2` - Great general purpose
- `mistral` - Fast and capable
- `neural-chat` - Optimized for chat

**Requirements:** 8GB+ RAM recommended

[→ More Ollama Details](./ollama.md)

---

### 🟪 HuggingFace

**What you get:**
- Access to thousands of models
- Many free options
- Community driven

**Setup:**
1. Go to [huggingface.co](https://huggingface.co)
2. Create account
3. Go to Settings → Access Tokens
4. Create new token
5. Paste in PyGPT Settings → HuggingFace API key

**Popular models:**
- `meta-llama/Llama-2-7b`
- `mistralai/Mistral-7B`
- `NousResearch/Nous-Hermes-2`

[→ More HuggingFace Details](./huggingface.md)

---

### 🟥 xAI Grok

**What you get:**
- Cutting-edge reasoning
- Real-time internet access
- Novel approaches

**Setup:**
1. Go to [console.x.ai](https://console.x.ai)
2. Register with X/Twitter
3. Add payment method
4. Create API key
5. Paste in PyGPT Settings → xAI API key

**Model:** `grok-beta` or latest

[→ More xAI Details](./xai-grok.md)

---

## 🔧 Adding API Keys in PyGPT

### Method 1: UI (Easiest)
```
1. Open PyGPT
2. Click ⚙️ Settings
3. Find "API Keys" section
4. Find provider's API key field
5. Paste key
6. Click "Save" or "Test"
```

### Method 2: Configuration File

**Location:**
- Windows: `%APPDATA%\pygpt\config.json`
- Linux: `~/.pygpt/config.json`
- macOS: `~/Library/Application Support/pygpt/config.json`

**Add to config:**
```json
{
  "api_key": "openai_key_here",
  "api_key_google": "google_key_here",
  "api_key_anthropic": "anthropic_key_here",
  "api_key_deepseek": "deepseek_key_here"
}
```

### Method 3: Environment Variables

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY = "your_key"
$env:GOOGLE_API_KEY = "your_key"
pygpt
```

**Linux/macOS:**
```bash
export OPENAI_API_KEY="your_key"
export GOOGLE_API_KEY="your_key"
pygpt
```

---

## 🔍 Troubleshooting API Keys

### Issue: "Invalid API Key"
**Causes:**
- Key has extra spaces
- Wrong key copied
- Key from different service
- Key expired or regenerated

**Fix:**
- Copy key again carefully (no spaces)
- Verify it's from correct service
- Regenerate key if old
- Check formatting

### Issue: "Authentication Failed"
**Causes:**
- API key doesn't have permissions
- Account has no credits
- Key restricted to certain IPs
- Service down

**Fix:**
- Check account dashboard
- Add payment method / credits
- Verify key settings
- Try testing key on provider's website

### Issue: "Rate Limited"
**Causes:**
- Too many requests
- Quota exceeded
- Free tier limits

**Fix:**
- Wait for quota reset
- Upgrade to paid tier
- Slow down requests
- Check provider dashboard

### Issue: "Connection Timeout"
**Causes:**
- Internet connection issue
- Provider server down
- Firewall blocking

**Fix:**
- Check internet connection
- Try different API
- Check provider status page
- Configure proxy if behind firewall

---

## 💰 Cost Comparison

| Provider | Pricing Model | Typical Cost |
|----------|---------------|--------------|
| **OpenAI GPT-4o** | Per token | ~$0.015 per 1K input |
| **Gemini** | Per token | ~$0.00075 per 1K input |
| **Claude 3** | Per token | ~$0.003 per 1K input |
| **DeepSeek** | Per token | Very cheap (~$0.00014) |
| **Mistral** | Per token | Cheap (~$0.00015) |
| **Ollama (Local)** | Free | 0 (your electricity) |
| **HuggingFace** | Free/Paid | Many free options |

**Recommendation for beginners:** Start with Gemini free tier or Ollama

---

## 🆕 Adding Multiple Providers

You can use multiple APIs simultaneously!

### Add Multiple Keys
1. Settings → API Keys
2. Add key for OpenAI
3. Add key for Google
4. Add key for Anthropic
5. etc.

### Switch Between Models
1. In chat, find Model dropdown
2. Select different provider's model
3. Conversation continues (may lose some context)

### Example Setup
- OpenAI GPT-4 for complex tasks
- Gemini 2.5 Flash for speed
- Claude for analysis
- Local Ollama as backup

---

## 🔐 Security Best Practices

### Protecting Your Keys
- ✅ Store in environment variables
- ✅ Use config files (not git)
- ✅ Never share keys
- ✅ Regenerate if leaked
- ✅ Use read-only tokens when available

### Monitoring
- ✅ Check provider dashboard regularly
- ✅ Set spending alerts
- ✅ Review recent API calls
- ✅ Report suspicious activity

---

## 📊 Choosing the Right Provider

### For Beginners
→ Start with **Gemini** (free, fast setup)

### For Best Quality
→ **OpenAI GPT-4** (most capable)

### For Budget Conscious
→ **Gemini** or **DeepSeek** (cheapest paid options)

### For Private/Offline Use
→ **Ollama** (local, free)

### For Experimentation
→ **HuggingFace** (many free options)

### For All-Around Best Value
→ **Gemini 2.5 Flash** (fast, cheap, high quality)

---

## 🆘 Getting Help

If you're stuck:

1. **Check provider documentation** - Most have setup guides
2. **Check provider dashboard** - View recent API calls
3. **Test on provider's website** - Verify key works there
4. **Check PyGPT logs** - Help debug issues
5. **Ask community** - [Discord](https://pygpt.net/discord)

---

## Quick Links

| Provider | Website | Docs | API Keys |
|----------|---------|------|----------|
| **Google** | [ai.google.dev](https://ai.google.dev) | [Docs](https://ai.google.dev/docs) | [Get key](https://aistudio.google.com) |
| **OpenAI** | [openai.com](https://openai.com) | [Docs](https://platform.openai.com/docs) | [Get key](https://platform.openai.com/api-keys) |
| **Anthropic** | [anthropic.com](https://anthropic.com) | [Docs](https://docs.anthropic.com) | [Get key](https://console.anthropic.com) |
| **DeepSeek** | [deepseek.com](https://deepseek.com) | [Docs](https://platform.deepseek.com/docs) | [Get key](https://platform.deepseek.com) |
| **Mistral** | [mistral.ai](https://mistral.ai) | [Docs](https://docs.mistral.ai) | [Get key](https://console.mistral.ai) |
| **Ollama** | [ollama.ai](https://ollama.ai) | [Docs](https://github.com/ollama/ollama) | N/A (local) |
| **HuggingFace** | [huggingface.co](https://huggingface.co) | [Docs](https://huggingface.co/docs) | [Get key](https://huggingface.co/settings/tokens) |
| **xAI** | [x.ai](https://x.ai) | [Docs](https://console.x.ai/docs) | [Get key](https://console.x.ai) |

---

**Next:** [Choose your provider guide](#provider-guides) →
