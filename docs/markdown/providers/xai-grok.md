# xAI Grok Provider

Setup and use xAI's Grok models in PyGPT.

## 🚀 Overview

xAI's Grok models offer unique capabilities with real-time data access and novel approaches to AI reasoning. Grok is designed to be helpful, harmless, and honest.

**Key Features:**
- Real-time information access
- Advanced reasoning
- Multimodal capabilities
- Audio support
- Competitive pricing

**Provider:** xAI  
**Website:** https://x.ai

## 📋 Available Models

### Grok-2

**Latest flagship model**
- Most capable
- Real-time data access
- Advanced reasoning
- Multimodal support

**Specifications:**
```
Context: 128K tokens
Output: 4K tokens
Training: Up to Dec 2024
```

**Best for:**
- Complex reasoning
- Real-time information
- Research tasks
- General use

### Grok-2 Mini

**Faster, cost-effective variant**
- Good performance
- Lower cost
- Faster responses
- Real-time access

**Specifications:**
```
Context: 128K tokens
Output: 4K tokens
Training: Up to Dec 2024
```

**Best for:**
- Quick queries
- Cost-sensitive tasks
- High-volume use
- Simple tasks

### Grok Vision

**Multimodal model**
- Image understanding
- Visual reasoning
- OCR capabilities
- Chart analysis

**Specifications:**
```
Context: 128K tokens
Images: Multiple per request
Training: Up to Dec 2024
```

**Best for:**
- Image analysis
- Visual Q&A
- Document processing
- Chart interpretation

### Grok Audio

**Audio-capable models**
- Voice input
- Audio output
- Real-time audio
- Natural conversation

**Specifications:**
```
Input: Audio streams
Output: Audio/text
Latency: Low
```

**Best for:**
- Voice interaction
- Audio transcription
- Real-time conversation
- Accessibility

## 🔑 Getting API Key

### Step 1: Create xAI Account

1. Visit https://x.ai
2. Click "Sign Up" or "Get Started"
3. Create account or sign in with X (Twitter)
4. Verify email

### Step 2: Access API Dashboard

1. Go to https://console.x.ai
2. Navigate to API section
3. Accept terms of service
4. Access API dashboard

### Step 3: Generate API Key

1. Click "Create API Key"
2. Name your key (e.g., "PyGPT")
3. Copy the key immediately
4. Store securely (won't be shown again)

### Step 4: Configure in PyGPT

1. Open PyGPT
2. Go to `Config → Settings → API Keys`
3. Select "xAI" tab
4. Paste your API key
5. Click "Save"

## ⚙️ Configuration

### Basic Setup

**API Key:**
```
Config → Settings → API Keys → xAI
API Key: [Your xAI API key]
```

**Model Selection:**
```
Model dropdown → Filter by xAI
Select: grok-2, grok-2-mini, etc.
```

**Endpoint (Optional):**
```
Default: https://api.x.ai/v1
Custom: [Your endpoint if different]
```

### Advanced Settings

**Native SDK:**
```
Use xAI SDK: Enabled (recommended)
Fallback: OpenAI-compatible API
```

**Timeout:**
```
Request timeout: 60 seconds
Adjust for long responses
```

**Retry Logic:**
```
Max retries: 3
Retry delay: 1 second
Exponential backoff: Yes
```

## 🎯 Use Cases

### Real-Time Information

```
You: "What's happening in tech news today?"

Grok: [Accesses real-time data]
"Here are today's top tech stories:
1. [Latest news with sources]
2. [Recent developments]
3. [Breaking updates]"
```

### Advanced Reasoning

```
You: "Explain quantum entanglement and its implications"

Grok: [Deep reasoning]
"Quantum entanglement is a phenomenon where...
[Detailed explanation with examples]
Implications include:
- Quantum computing
- Secure communication
- Fundamental physics"
```

### Multimodal Tasks

```
You: [Uploads chart image]
"Analyze this sales chart"

Grok: [Analyzes image]
"This chart shows:
- Upward trend in Q4
- Peak in December
- 25% growth YoY
Recommendations: ..."
```

### Voice Interaction

```
[Enable audio mode]

You: [Speaks] "Tell me about AI developments"

Grok: [Speaks response]
"Recent AI developments include..."
```

## 🔧 Features

### Real-Time Data Access

**Automatic Updates:**
- Current events
- Latest news
- Real-time data
- Recent developments

**No Cutoff Date:**
- Always current
- Live information
- Up-to-date facts
- Recent sources

### Remote Tools

**Available Tools:**
- Web search
- Real-time data
- Code execution
- File operations

**Configuration:**
```
Settings → Remote Tools → xAI
Enable: Web search, Code execution
```

### Multimodal Support

**Image Input:**
```
Upload images
Analyze visuals
Extract text
Understand charts
```

**Audio Input/Output:**
```
Voice commands
Spoken responses
Real-time audio
Natural conversation
```

### Streaming Responses

**Real-time Output:**
```
See response as generated
Stop anytime
Faster perceived speed
Better UX
```

## 💰 Pricing

### API Costs

**Grok-2:**
```
Input: $2.00 per 1M tokens
Output: $10.00 per 1M tokens
```

**Grok-2 Mini:**
```
Input: $0.50 per 1M tokens
Output: $1.50 per 1M tokens
```

**Grok Vision:**
```
Input: $2.00 per 1M tokens
Output: $10.00 per 1M tokens
Images: $0.01 per image
```

**Grok Audio:**
```
Input: $0.10 per minute
Output: $0.20 per minute
```

### Cost Optimization

**Tips:**
- Use Grok-2 Mini for simple tasks
- Batch requests when possible
- Optimize prompt length
- Cache frequent queries
- Monitor usage

**Example Costs:**
```
Simple query (100 tokens): $0.0002
Medium task (1000 tokens): $0.002
Complex task (10K tokens): $0.02
```

## 🐛 Troubleshooting

### API Key Issues

**Problem:** Invalid API key

**Solutions:**
- Verify key copied correctly
- Check for extra spaces
- Regenerate key if needed
- Verify account active

### Rate Limits

**Problem:** Too many requests

**Solutions:**
- Check rate limits
- Implement delays
- Upgrade plan
- Batch requests

### Model Not Available

**Problem:** Model not found

**Solutions:**
- Check model name spelling
- Verify API access
- Update model list
- Check account tier

### Slow Responses

**Problem:** Long wait times

**Solutions:**
- Use Grok-2 Mini
- Reduce context length
- Check internet connection
- Try different time

## 💡 Best Practices

### Model Selection

```
✅ Grok-2: Complex reasoning, research
✅ Grok-2 Mini: Quick queries, high volume
✅ Grok Vision: Image analysis
✅ Grok Audio: Voice interaction
❌ Always using most expensive model
```

### Prompt Engineering

```
✅ Clear, specific questions
✅ Provide context
✅ Use examples
✅ Structured requests
❌ Vague queries
❌ No context
```

### Cost Management

```
✅ Monitor usage
✅ Use appropriate model
✅ Optimize prompts
✅ Cache results
❌ Ignore costs
❌ Wasteful usage
```

## 🔗 Related Features

- [Realtime + Audio Mode](../modes/realtime-audio.md) - Audio features
- [Research Mode](../modes/research.md) - Real-time research
- [Vision & Images](../guides/05-vision-images.md) - Image analysis

## 📚 Additional Resources

- [xAI Documentation](https://docs.x.ai/)
- [xAI API Reference](https://docs.x.ai/api)
- [xAI Pricing](https://x.ai/pricing)
- [xAI Blog](https://x.ai/blog)

## ⚠️ Limitations

- **API access required** - No free tier
- **Rate limits** - Varies by plan
- **Regional availability** - May vary
- **Beta features** - Some features in beta

## 🆘 Need Help?

- Check [xAI Documentation](https://docs.x.ai/)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Perplexity Provider](./perplexity.md) →
