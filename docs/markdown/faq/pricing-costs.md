# Pricing & Costs FAQ

Understanding API costs and budgeting for PyGPT usage.

## 💰 Token Pricing Explained

### What are Tokens?

Tokens are units of text that AI models process:
- 1 token ≈ 4 characters
- 1 token ≈ 0.75 words
- Both input and output count toward cost

### Example

```
Input: "What is AI?"
≈ 4 tokens

Output: "Artificial Intelligence (AI) is..."
≈ 10 tokens

Total: 14 tokens billable
```

---

## 📊 Provider Pricing Comparison

### FREE Options

**Google Gemini (Free Tier)**
- Limits: 15 req/min, 1M tokens/day
- Cost: $0
- Best for: Learning, testing, light use

**Ollama (Local)**
- Cost: $0 (your electricity only)
- Best for: Complete privacy, offline

### PAID Options (Cheapest First)

**DeepSeek**
```
Most affordable paid option:
- DeepSeek-V3: ~$0.00014 per 1K input
- DeepSeek-R1: ~$0.00165 per 1K input
```

**Mistral**
```
Fast and cheap:
- Mistral Large: ~$0.00015 per 1K input
```

**Google Gemini (Paid)**
```
After free tier:
- Gemini 2.5 Flash: ~$0.00075 per 1K input
- Still very affordable
```

**Claude (Anthropic)**
```
Moderate cost:
- Claude 3 Haiku: ~$0.00025 per 1K input
- Claude 3 Sonnet: ~$0.003 per 1K input
- Claude 3 Opus: ~$0.015 per 1K input
```

**OpenAI**
```
Industry standard pricing:
- GPT-3.5: ~$0.0005 per 1K input
- GPT-4o: ~$0.015 per 1K input
- o1: ~$0.06 per 1K input
```

---

## 📈 Typical Usage Costs

### Scenario 1: Casual User (10 messages/day)

```
Typical message:
- Input: 2000 tokens
- Output: 500 tokens
- Total: 2500 tokens per message

Cost per message:
- GPT-4o: ~$0.05
- Gemini: ~$0.002
- Claude Haiku: ~$0.001
- DeepSeek: ~0.0004

Monthly (30 days × 10 messages):
- OpenAI: ~$15
- Gemini: ~$0.60
- Claude: ~$0.30
- DeepSeek: ~$0.12
```

### Scenario 2: Power User (50 messages/day)

```
Monthly (30 days × 50 messages):
- OpenAI GPT-4o: ~$75
- Gemini: ~$3
- Claude Haiku: ~$1.50
- DeepSeek: ~$0.60
```

### Scenario 3: Heavy Developer (200 messages/day)

```
Monthly (30 days × 200 messages):
- OpenAI GPT-4o: ~$300
- Gemini: ~$12
- Claude Sonnet: ~$18
- DeepSeek: ~$2.40
```

---

## 🎯 Cost Reduction Strategies

### Strategy 1: Use Free Tier

**Gemini Free Tier**
- 15 requests/minute
- 1 million tokens/day
- Perfect for learning
- Upgrade when needed

### Strategy 2: Use Cheaper Models

```
For general chat:
- Don't use: GPT-4 ($0.015/1K input)
- Use instead: Gemini Flash ($0.00075/1K)
- Save: 95% reduction

For reasoning:
- Don't use: o1 ($0.06/1K input)
- Use instead: DeepSeek R1 ($0.00165/1K)
- Save: 97% reduction
```

### Strategy 3: Reduce Context

```
Every 1000 input tokens cost money

Tips:
1. Clear old messages before starting new topic
2. Use shorter prompts
3. Ask focused questions
4. Don't paste full documents
5. Use summaries instead
```

### Strategy 4: Use Local Ollama

```
Completely free:
- Run on your computer
- No API calls
- No costs
- Perfect for private use
- Good for development

Trade-off:
- Slower responses
- Requires decent hardware
- Less capable models
```

### Strategy 5: Batch Operations

```
Many providers offer batch discounts:
- Process multiple requests together
- Usually 50% cost reduction
- Perfect for bulk processing
```

---

## 💡 Cost Optimization Examples

### Example 1: Research Project

```
Problem: Using GPT-4o for research costs $50/day

Solution:
1. Switch to Gemini Flash: $0.24/day (95% save)
2. Keep local Ollama for drafting: $0 for ideas
3. Use GPT-4o only for final polish
Total: ~$1/day (98% save!)
```

### Example 2: Code Development

```
Problem: Using GPT-4o for coding costs $200/month

Solution:
1. Use DeepSeek for most tasks: $1/month
2. Use GPT-4o for complex reasoning: $5/month
3. Use local models for testing: $0
Total: ~$6/month (97% save!)
```

### Example 3: Content Creation

```
Problem: Multiple Claude calls for content = $20/day

Solution:
1. Use Gemini Flash for drafting: $0.10/day
2. Use Claude for refinement: $2/day
3. Batch similar requests: save 50%
Total: ~$0.50/day (97% save!)
```

---

## 📊 Budget Planning

### Set Monthly Budget

**For Each Provider:**

1. OpenAI: [Dashboard](https://platform.openai.com/account/billing/limits)
   - Go to Usage Limits
   - Set maximum spend

2. Google: [Billing](https://console.cloud.google.com/billing)
   - Set budget alert
   - Monitor usage

3. Anthropic: [Billing](https://console.anthropic.com/account/billing)
   - Add spending limit

### Track Usage

1. Check provider dashboard weekly
2. Monitor token usage in PyGPT
3. Adjust if necessary
4. Review invoices monthly

---

## 🆚 Choosing by Budget

### Ultra Budget ($0/month)

→ **Gemini Free Tier** + **Ollama**
- Free tier for testing
- Local models for work
- Upgrade only when needed

### Budget Conscious ($0.50-$5/month)

→ **DeepSeek** or **Gemini Paid**
- Very affordable
- Good quality
- Scalable costs

### Moderate ($10-$50/month)

→ **Mix of providers**
- Gemini for general use
- Claude for analysis
- Local Ollama for development

### No Budget Limit ($100+/month)

→ **Premium providers**
- OpenAI GPT-4o
- Claude 3 Opus
- Multiple providers
- High-end models

---

## ⚠️ Avoiding Unexpected Charges

### Common Pitfalls

1. **Leaving app running**
   - Idle connections don't charge
   - But API errors could retry

2. **Large file uploads**
   - Each token costs money
   - Large files = many tokens
   - Check before uploading

3. **Long conversations**
   - Entire history sent each time
   - Clear old messages
   - Save and start new chat

4. **Expensive model selection**
   - Accidentally using GPT-4
   - Check model before use
   - Use cheaper alternative

### Prevention

1. **Set usage alerts** in provider dashboard
2. **Monitor token counter** in PyGPT
3. **Check default model** is cheapest
4. **Review bills** monthly
5. **Set spending limits** on accounts

---

## 💳 Payment Methods

### Accepted by Providers

- Credit cards (Visa, Mastercard, Amex)
- Debit cards
- PayPal (some providers)
- Business accounts (invoicing)

### Tips

- Use separate card for APIs
- Enable fraud alerts
- Use virtual card numbers if available
- Keep receipts for tax purposes

---

## 📞 Billing Support

**Need help with charges?**

- OpenAI: [support.openai.com](https://support.openai.com)
- Google: [support.google.com](https://support.google.com)
- Anthropic: [support.anthropic.com](https://support.anthropic.com)

---

**See Also:**
- [API Key Setup](../guides/02-api-key-setup.md)
- [FAQ - General](./general.md)

---

**Last Updated:** 2025
