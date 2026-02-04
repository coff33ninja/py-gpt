# OpenAI Provider Guide

Complete guide to using OpenAI models (GPT-4, GPT-4o, o1, o3) in PyGPT.

## 🎯 Quick Facts

| Aspect | Details |
|--------|---------|
| **Provider** | OpenAI |
| **Official Site** | [openai.com](https://openai.com) |
| **API Docs** | [platform.openai.com/docs](https://platform.openai.com/docs) |
| **Cost** | Paid (no free tier) |
| **Best For** | Most capable models, reasoning, code |
| **Speed** | Fast (GPT-4o), slower (o1/o3) |
| **Models** | GPT-4o, GPT-4 Turbo, o1, o3 |
| **Audio** | ✅ Yes (Voice API) |
| **Vision** | ✅ Yes (GPT-4V) |

---

## 🔧 Getting Started

### Step 1: Create OpenAI Account

1. Go to [openai.com/signup](https://openai.com/signup)
2. Enter email address
3. Verify email
4. Complete profile

### Step 2: Add Payment Method

1. Log in to account
2. Go to [Billing Overview](https://platform.openai.com/account/billing/overview)
3. Click "Billing" → "Payment Methods"
4. Add credit card
5. Set usage limits (optional but recommended)

⚠️ **Important**: No free tier - payment required immediately

### Step 3: Create API Key

1. Go to [API Keys page](https://platform.openai.com/api-keys)
2. Click "+ Create new secret key"
3. Name it (e.g., "PyGPT")
4. Copy the key (starts with `sk-proj-`)
5. **Never share this key!**

### Step 4: Add to PyGPT

**Method 1: UI**
1. Open PyGPT
2. Settings → API Keys
3. Find "OpenAI API Key"
4. Paste key
5. Click "Test"

**Method 2: Config File**
```json
{
  "api_key": "sk-proj-..."
}
```

**Method 3: Environment Variable**
```powershell
# Windows (PowerShell)
$env:OPENAI_API_KEY = "sk-proj-..."
pygpt

# Linux/macOS
export OPENAI_API_KEY="sk-proj-..."
pygpt
```

---

## 📊 Available Models

### GPT-4o (Recommended)

**What it is:** Optimized version of GPT-4, best for most tasks

| Feature | Details |
|---------|---------|
| **Speed** | Very fast |
| **Quality** | Excellent |
| **Cost** | ~$0.015 per 1K input |
| **Context** | 128K tokens |
| **Vision** | ✅ Yes |
| **Audio** | ✅ Yes |
| **Reasoning** | Good |

**Best for:** General use, chat, coding, analysis

**Example:**
```
User: "Explain quantum computing"
GPT-4o: [Fast, accurate response in ~2 seconds]
```

---

### o1 (Reasoning)

**What it is:** Advanced reasoning model, slower but more accurate

| Feature | Details |
|---------|---------|
| **Speed** | Slower (~5-30s) |
| **Quality** | Excellent reasoning |
| **Cost** | Higher (~$0.06 per 1K input) |
| **Context** | 128K tokens |
| **Vision** | ❌ No |
| **Reasoning** | Exceptional |

**Best for:** Complex problems, math, physics, logic

**Example:**
```
User: "Solve complex math problem"
o1: [Takes time but gives guaranteed correct answer]
```

---

### o3 (Next-Gen Reasoning)

**What it is:** Latest reasoning model (preview)

| Feature | Details |
|---------|---------|
| **Speed** | Varies by complexity mode |
| **Quality** | State-of-the-art |
| **Cost** | Premium |
| **Context** | 200K tokens |
| **Vision** | ❌ No (yet) |
| **Modes** | Low, Medium, High complexity |

**Note**: Limited availability during preview

---

### GPT-4 Turbo

**What it is:** Previous generation, still very capable

| Feature | Details |
|---------|---------|
| **Speed** | Fast |
| **Quality** | Excellent |
| **Cost** | $0.01 per 1K input |
| **Context** | 128K tokens |
| **Vision** | ✅ Yes |

**Use**: If GPT-4o unavailable or prefer previous version

---

### GPT-3.5-turbo

**What it is:** Fast budget option

| Feature | Details |
|---------|---------|
| **Speed** | Very fast |
| **Quality** | Good (not great) |
| **Cost** | Cheapest (~$0.0005 per 1K) |
| **Context** | 16K tokens |
| **Vision** | ❌ No |

**Use**: When cost is critical, or for simple tasks

---

## 💰 Pricing

### Cost Examples

```
GPT-4o (General Use)
- Input: 2000 tokens = $0.03
- Output: 500 tokens = $0.015
- Total: ~$0.045 per response

o1 (Reasoning)
- Input: 2000 tokens = $0.12
- Output: 500 tokens = $0.30
- Total: ~$0.42 per response (expensive but accurate)

GPT-3.5-turbo (Budget)
- Input: 2000 tokens = $0.001
- Output: 500 tokens = $0.0015
- Total: ~$0.0025 per response
```

### Reducing Costs

1. **Use GPT-4o** - Better value than GPT-4 Turbo
2. **Batch Processing** - Lower rate for batch requests (15% cheaper)
3. **Use Cheaper Models** - o1/o3 only when needed
4. **Reduce Context** - Shorter prompts = fewer tokens
5. **Monitor Usage** - Check dashboard weekly

---

## 🎯 Use Cases

### 1. General Chat
```
Model: gpt-4o
Speed: Fast
Cost: Low
Quality: High

Use: Everyday questions, brainstorming, general assistance
```

### 2. Code Generation & Debugging
```
Model: gpt-4o
Speed: Fast
Cost: Low-Medium
Quality: High

Use: Write, review, and debug code in any language
```

### 3. Complex Problem Solving
```
Model: o1
Speed: Slower
Cost: Medium
Quality: Best

Use: Math, physics, logic puzzles, advanced reasoning
```

### 4. Image Analysis
```
Model: gpt-4o (vision)
Speed: Medium
Cost: Low
Quality: High

Use: Describe images, extract text (OCR), analyze charts
```

### 5. Document Processing
```
Model: gpt-4o
Speed: Medium
Cost: Depends on length
Quality: High

Use: Summarize documents, extract information, analyze reports
```

### 6. Translation
```
Model: gpt-4o
Speed: Fast
Cost: Low
Quality: Good

Use: Translate text between languages
```

---

## ⚙️ Advanced Configuration

### Temperature (Creativity)

```
Temperature: 0 (deterministic)
└─→ Consistent, predictable responses
└─→ Use for: Technical tasks, code

Temperature: 0.5 (balanced)
└─→ Balanced creativity and consistency
└─→ Use for: Most tasks

Temperature: 1.0 (creative)
└─→ More varied, creative responses
└─→ Use for: Writing, brainstorming

Temperature: 2.0 (very creative)
└─→ Highly creative, sometimes nonsensical
└─→ Use for: Creative writing
```

### Top P (Nucleus Sampling)

```
top_p: 0.1 (conservative)
└─→ Only top 10% of likely tokens
└─→ More focused responses

top_p: 0.5 (balanced)
└─→ Top 50% of likely tokens

top_p: 1.0 (all)
└─→ All tokens considered
```

### Max Tokens (Response Length)

```
Max Tokens: 100 (short)
└─→ Brief responses, fast processing

Max Tokens: 500 (medium)
└─→ Normal responses

Max Tokens: 2000 (long)
└─→ Detailed responses, more cost
```

---

## 🔌 Integration Features

### Function Calling

Use AI to decide when to call functions:

```python
# PyGPT automatically handles this
# In chat, AI can trigger commands and tools
```

### Vision Processing

Analyze images in real-time:

1. Attach image to chat
2. Ask question about image
3. GPT-4o analyzes and responds

### Audio (Voice Mode)

Use with Voice API:
1. Switch to Audio mode
2. Speak your question
3. AI responds with speech

---

## 🆚 Comparison with Other Providers

| Feature | GPT-4o | Gemini | Claude | DeepSeek |
|---------|--------|--------|---------|----------|
| **Cost** | Medium | Low | Medium | Very Low |
| **Speed** | Fast | Very Fast | Medium | Very Fast |
| **Quality** | Excellent | Good | Excellent | Good |
| **Reasoning** | Good | Good | Good | Excellent |
| **Vision** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Audio** | ✅ Yes | ✅ Yes | ✅ Yes | ❌ No |
| **Free Tier** | ❌ No | ✅ Yes | ❌ No | ❌ No |

**Verdict**: GPT-4o best all-rounder; Gemini best value; Claude best reasoning; DeepSeek cheapest

---

## 🐛 Troubleshooting

### "Invalid API Key"
- Regenerate key at [API Keys](https://platform.openai.com/api-keys)
- Ensure no extra spaces
- Key should start with `sk-proj-`

### "Insufficient quota"
- Check billing: [Billing Overview](https://platform.openai.com/account/billing/overview)
- Add payment method
- Check spending limits

### "Rate limited"
- Wait 1-2 minutes
- Upgrade plan if frequently rate limited
- Spread requests out more

### "Model not available"
- Check [Model List](https://platform.openai.com/docs/models)
- Some models are limited availability
- Use `gpt-4o` if unsure

### "Connection timeout"
- Check internet connection
- Check OpenAI status page
- Try different model
- Wait and retry

---

## 📈 Monitoring Usage

### Dashboard
1. Go to [Usage](https://platform.openai.com/account/usage/overview)
2. View usage by model
3. See costs
4. Check trends

### Setting Alerts
1. Go to [Billing Overview](https://platform.openai.com/account/billing/overview)
2. Click "Usage limits"
3. Set maximum monthly spend
4. Get email alerts when approaching limit

### API Activity
1. Go to [API Reference](https://platform.openai.com/account/api-keys)
2. View recent API calls
3. See timestamps and usage

---

## 🔐 Security Best Practices

### Protecting Your Key

```
✅ DO:
- Store in environment variable
- Use separate key per machine
- Rotate keys regularly
- Use read-only keys when possible
- Monitor usage for suspicious activity

❌ DON'T:
- Commit key to GitHub
- Share key in emails
- Store in plain text files
- Use production key for development
- Leave key in browser history
```

### If Key Compromised

1. Go to [API Keys](https://platform.openai.com/api-keys)
2. Delete compromised key immediately
3. Create new key
4. Update all applications
5. Monitor usage for suspicious activity

---

## 📚 Resources

- **Official Docs**: [platform.openai.com/docs](https://platform.openai.com/docs)
- **Model List**: [platform.openai.com/docs/models](https://platform.openai.com/docs/models)
- **Pricing**: [openai.com/pricing](https://openai.com/pricing)
- **Status**: [status.openai.com](https://status.openai.com)
- **Community**: [Community Forum](https://community.openai.com)

---

## ✅ Quick Checklist

- [ ] Created OpenAI account
- [ ] Added payment method
- [ ] Generated API key
- [ ] Copied key to PyGPT
- [ ] Tested connection
- [ ] Selected GPT-4o model
- [ ] Sent test message
- [ ] Set usage limits
- [ ] Bookmarked dashboard

---

**Next Steps:**
- [All Providers Guide](../guides/02-api-key-setup.md)
- [Chat Modes](../guides/01-chat-modes.md)
- [Troubleshooting](../reference/troubleshooting.md)

---

**Last Updated:** 2025
