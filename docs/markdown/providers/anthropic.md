# Anthropic Claude Provider Guide

Complete guide to using Claude models from Anthropic in PyGPT.

## 🎯 Quick Facts

| Aspect | Details |
|--------|---------|
| **Provider** | Anthropic |
| **Official Site** | [anthropic.com](https://anthropic.com) |
| **API Docs** | [docs.anthropic.com](https://docs.anthropic.com) |
| **Cost** | Paid (no free tier) |
| **Best For** | Reasoning, analysis, safety-focused |
| **Speed** | Medium (fast thinking mode) |
| **Models** | Claude 3 Opus, Sonnet, Haiku |
| **Audio** | ✅ Yes (partial) |
| **Vision** | ✅ Yes |

---

## 🔧 Getting Started

### Step 1: Create Anthropic Account

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Click "Sign up"
3. Enter email and create password
4. Verify email address

### Step 2: Add Payment Method

1. Go to [Billing](https://console.anthropic.com/account/billing)
2. Click "Add payment method"
3. Enter credit card details
4. Set usage limits (recommended)

### Step 3: Create API Key

1. Go to [API Keys](https://console.anthropic.com/account/keys)
2. Click "Create Key"
3. Name it (e.g., "PyGPT")
4. Copy key (starts with `sk-ant-`)
5. **Keep it secret!**

### Step 4: Add to PyGPT

**Method 1: UI**
1. Settings → API Keys
2. Find "Anthropic API Key"
3. Paste key
4. Click "Test"

**Method 2: Config File**
```json
{
  "api_key_anthropic": "sk-ant-..."
}
```

**Method 3: Environment Variable**
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-..."
pygpt
```

---

## 📊 Available Models

### Claude 3 Opus

**Most capable model**

| Feature | Details |
|---------|---------|
| **Speed** | Medium |
| **Quality** | Best reasoning |
| **Cost** | $15/1M input tokens |
| **Context** | 200K tokens |
| **Vision** | ✅ Yes |

**Best for:** Complex reasoning, analysis, creative writing

### Claude 3 Sonnet

**Best balance**

| Feature | Details |
|---------|---------|
| **Speed** | Fast |
| **Quality** | Excellent |
| **Cost** | $3/1M input tokens |
| **Context** | 200K tokens |
| **Vision** | ✅ Yes |

**Best for:** General use, most tasks

### Claude 3 Haiku

**Fast & cheap**

| Feature | Details |
|---------|---------|
| **Speed** | Very fast |
| **Quality** | Good |
| **Cost** | $0.25/1M input tokens |
| **Context** | 200K tokens |
| **Vision** | ✅ Yes |

**Best for:** Quick tasks, cost-sensitive work

---

## 💰 Pricing

```
Claude 3 Opus:
- Input: $15 per 1M tokens ($0.015 per 1K)
- Output: $75 per 1M tokens ($0.075 per 1K)

Claude 3 Sonnet:
- Input: $3 per 1M tokens ($0.003 per 1K)
- Output: $15 per 1M tokens ($0.015 per 1K)

Claude 3 Haiku:
- Input: $0.25 per 1M tokens ($0.00025 per 1K)
- Output: $1.25 per 1M tokens ($0.00125 per 1K)
```

**Typical conversation:** 2000 input + 500 output tokens
- Opus: ~$0.04
- Sonnet: ~$0.013
- Haiku: ~0.002

---

## 🎯 Use Cases

### Research & Analysis
```
Model: Claude 3 Opus
Speed: Medium
Cost: Medium
Quality: Best

Use: Deep research, complex analysis, academic work
```

### General Chat
```
Model: Claude 3 Sonnet
Speed: Fast
Cost: Low
Quality: Excellent

Use: Everyday questions, brainstorming, general assistance
```

### Quick Queries
```
Model: Claude 3 Haiku
Speed: Very Fast
Cost: Very Low
Quality: Good

Use: Quick answers, summarization, simple tasks
```

---

## 🆚 Claude vs Other Providers

| Feature | Claude | GPT-4o | Gemini |
|---------|--------|--------|--------|
| **Reasoning** | Excellent | Excellent | Good |
| **Speed** | Medium | Fast | Very Fast |
| **Cost** | Medium | Medium | Low |
| **Vision** | Yes | Yes | Yes |
| **Context** | 200K | 128K | Large |
| **Safety** | Excellent | Good | Good |

---

## 🐛 Troubleshooting

### "Invalid API Key"
- Regenerate key at [API Keys](https://console.anthropic.com/account/keys)
- Ensure key starts with `sk-ant-`
- Check for extra spaces

### "Insufficient credits"
- Check [Billing](https://console.anthropic.com/account/billing)
- Add payment method
- Set spending limits

### "Model not available"
- Check [Models Documentation](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- Some models may be limited access
- Try `claude-3-sonnet` as default

---

## 📚 Resources

- **API Docs**: [docs.anthropic.com](https://docs.anthropic.com)
- **Models**: [Available Models](https://docs.anthropic.com/claude/reference/getting-started-with-the-api)
- **Pricing**: [anthropic.com/pricing](https://anthropic.com/pricing)
- **Status**: [status.anthropic.com](https://status.anthropic.com)

---

**Next:** [All Providers](../guides/02-api-key-setup.md) →
