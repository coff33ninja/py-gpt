# Perplexity Provider

Setup and use Perplexity AI's Sonar models in PyGPT.

## 🔍 Overview

Perplexity AI specializes in research and information retrieval with real-time web access. Sonar models are optimized for searching, analyzing, and synthesizing information from the web.

**Key Features:**
- Real-time web search
- Source citations
- Research-focused
- Fast responses
- Competitive pricing

**Provider:** Perplexity AI  
**Website:** https://perplexity.ai

## 📋 Available Models

### Sonar

**Standard research model**
- Real-time web access
- Good performance
- Source citations
- Cost-effective

**Specifications:**
```
Context: 127K tokens
Output: 4K tokens
Training: Real-time web data
```

**Best for:**
- Quick research
- Fact-checking
- Current events
- General queries

### Sonar Pro

**Advanced research model**
- Deep web analysis
- Multiple sources
- Better synthesis
- Higher quality

**Specifications:**
```
Context: 127K tokens
Output: 4K tokens
Training: Real-time web data
```

**Best for:**
- Comprehensive research
- Academic queries
- Market analysis
- In-depth investigation

### Sonar Reasoning

**Advanced reasoning model**
- Complex analysis
- Multi-step reasoning
- Deep understanding
- Best quality

**Specifications:**
```
Context: 127K tokens
Output: 4K tokens
Training: Real-time web data
```

**Best for:**
- Complex problems
- Technical analysis
- Research papers
- Critical thinking

### Sonar Chat

**Conversational model**
- Natural dialogue
- Context retention
- Follow-up questions
- Interactive research

**Specifications:**
```
Context: 127K tokens
Output: 4K tokens
Training: Real-time web data
```

**Best for:**
- Interactive research
- Exploratory queries
- Learning sessions
- Iterative investigation

## 🔑 Getting API Key

### Step 1: Create Perplexity Account

1. Visit https://perplexity.ai
2. Click "Sign Up"
3. Create account with email
4. Verify email address

### Step 2: Access API Settings

1. Go to https://perplexity.ai/settings
2. Navigate to "API" section
3. Or visit https://perplexity.ai/settings/api
4. Review API documentation

### Step 3: Generate API Key

1. Click "Generate API Key"
2. Name your key (e.g., "PyGPT")
3. Copy the key immediately
4. Store securely (won't be shown again)

### Step 4: Configure in PyGPT

1. Open PyGPT
2. Go to `Config → Settings → API Keys`
3. Select "Perplexity" tab
4. Paste your API key
5. Click "Save"

## ⚙️ Configuration

### Basic Setup

**API Key:**
```
Config → Settings → API Keys → Perplexity
API Key: [Your Perplexity API key]
```

**Model Selection:**
```
Model dropdown → Filter by Perplexity
Select: sonar, sonar-pro, sonar-reasoning
```

**Endpoint:**
```
Default: https://api.perplexity.ai
Custom: [Your endpoint if different]
```

### Research Mode

**Enable Research Mode:**
```
Mode: Research
Model: sonar-pro or sonar-reasoning
```

**Research Settings:**
```
Search depth: Standard / Deep
Max sources: 10-50
Citation style: Inline / Footnotes
Time range: Any / Recent
```

### Advanced Settings

**Search Parameters:**
```
Region: US / UK / Global
Language: en / es / etc.
Safe search: Off / Moderate / Strict
```

**Response Settings:**
```
Temperature: 0.0-1.0 (default: 0.2)
Max tokens: 1000-4000
Top P: 0.9
```

**Citation Format:**
```
Include sources: Yes
Citation style: Inline / Footnotes / Bibliography
Show URLs: Yes
```

## 🎯 Use Cases

### Real-Time Research

```
You: "What are the latest developments in quantum computing?"

Sonar: [Searches web in real-time]

"Recent developments in quantum computing (2026):

1. **IBM's 1000-qubit processor** [1]
   - Announced January 2026
   - Error correction breakthrough
   - Commercial applications

2. **Google's quantum advantage** [2]
   - Solved optimization problem
   - 1000x faster than classical
   - Published in Nature

3. **New quantum algorithms** [3]
   - Drug discovery applications
   - Financial modeling
   - Climate simulation

Sources:
[1] IBM Research Blog - https://...
[2] Nature - https://...
[3] MIT Technology Review - https://..."
```

### Market Analysis

```
You: "Analyze the current state of the EV market"

Sonar Pro: [Deep web analysis]

"Electric Vehicle Market Analysis (2026):

**Market Size**
- Global sales: 18M units (2025) [1]
- Market value: $500B [2]
- Growth rate: 25% CAGR [3]

**Key Players**
1. Tesla - 20% market share [4]
2. BYD - 18% market share [4]
3. VW Group - 12% market share [4]

**Trends**
- Battery costs down 40% [5]
- Charging infrastructure expanding [6]
- Government incentives increasing [7]

**Challenges**
- Supply chain constraints [8]
- Infrastructure gaps [9]
- Price competition [10]

[Detailed sources listed...]"
```

### Academic Research

```
You: "Summarize recent research on climate change mitigation"

Sonar Reasoning: [Comprehensive analysis]

"Climate Change Mitigation Research (2024-2026):

**Carbon Capture**
- Direct air capture costs reduced 60% [1]
- New materials improve efficiency by 40% [2]
- Pilot projects in 15 countries [3]

**Renewable Energy**
- Solar efficiency reaches 30% [4]
- Wind power costs at record low [5]
- Grid storage capacity doubled [6]

**Policy Developments**
- 50+ countries commit to net-zero [7]
- Carbon pricing expanding globally [8]
- Green technology incentives [9]

**Emerging Technologies**
- Green hydrogen production [10]
- Advanced nuclear designs [11]
- Sustainable aviation fuel [12]

[Academic sources with DOIs...]"
```

### Fact Checking

```
You: "Is it true that AI can now pass the Turing test?"

Sonar: [Searches and analyzes]

"Based on recent sources:

**Current Status:**
- Several AI models claim to pass [1]
- Debate continues in AI community [2]
- No universal agreement on criteria [3]

**Recent Developments:**
- GPT-4 passed in some tests [4]
- Claude 3 showed human-like responses [5]
- Gemini demonstrated reasoning [6]

**Expert Opinions:**
- Some experts say yes [7]
- Others argue test is outdated [8]
- New benchmarks proposed [9]

**Conclusion:**
Depends on test definition and criteria.
Modern AI shows human-like capabilities
but debate continues on true understanding.

[Sources with credibility ratings...]"
```

## 🔧 Features

### Real-Time Web Access

**Always Current:**
- No training cutoff
- Live web search
- Latest information
- Recent sources

**Search Quality:**
- Multiple sources
- Credible sites
- Academic papers
- News articles

### Source Citations

**Automatic Citations:**
```
Every fact cited
Source URLs provided
Publication dates
Author information
```

**Citation Formats:**

**Inline:**
```
"According to MIT [1], quantum computers..."
```

**Footnotes:**
```
"Quantum computers are advancing rapidly.[1]

[1] MIT Technology Review, 2026-01-15"
```

**Bibliography:**
```
Sources:
1. MIT Technology Review - "Quantum Breakthrough"
   https://... (2026-01-15)
2. Nature - "Quantum Computing Advances"
   https://... (2026-01-10)
```

### Multi-Source Analysis

**Comprehensive Research:**
```
1. Search multiple sources
2. Cross-reference facts
3. Identify consensus
4. Note disagreements
5. Synthesize findings
```

**Source Diversity:**
- Academic papers
- News articles
- Official reports
- Expert blogs
- Industry publications

### Research Depth

**Quick Search (Sonar):**
```
5-10 sources
Fast results
Surface-level
Good for quick facts
```

**Deep Research (Sonar Pro):**
```
10-30 sources
Comprehensive
In-depth analysis
Better synthesis
```

**Advanced Analysis (Sonar Reasoning):**
```
30+ sources
Multi-step reasoning
Critical analysis
Academic quality
```

## 💰 Pricing

### API Costs

**Sonar:**
```
Input: $0.20 per 1M tokens
Output: $0.20 per 1M tokens
Searches: Included
```

**Sonar Pro:**
```
Input: $1.00 per 1M tokens
Output: $1.00 per 1M tokens
Searches: Included
```

**Sonar Reasoning:**
```
Input: $5.00 per 1M tokens
Output: $5.00 per 1M tokens
Searches: Included
```

**Sonar Chat:**
```
Input: $0.20 per 1M tokens
Output: $0.20 per 1M tokens
Searches: Included
```

### Cost Optimization

**Tips:**
- Use Sonar for simple queries
- Reserve Pro for complex research
- Batch similar queries
- Cache frequent searches
- Monitor usage

**Example Costs:**
```
Simple query (500 tokens): $0.0001
Research task (5K tokens): $0.001
Deep analysis (20K tokens): $0.004
```

## 🐛 Troubleshooting

### No Search Results

**Problem:** Search returns nothing

**Solutions:**
- Check internet connection
- Verify API key valid
- Try different keywords
- Check API quota
- Review error message

### Poor Quality Results

**Problem:** Irrelevant information

**Solutions:**
- Use more specific queries
- Try Sonar Pro or Reasoning
- Add context to query
- Specify time range
- Filter by source type

### Rate Limits

**Problem:** Too many requests

**Solutions:**
- Check rate limits
- Implement delays
- Upgrade plan
- Batch requests
- Monitor usage

### Outdated Information

**Problem:** Old results

**Solutions:**
- Specify recent time range
- Use "latest" in query
- Check source dates
- Try different search terms

## 💡 Best Practices

### Effective Queries

```
❌ "AI"
✅ "Latest developments in large language models in 2026"

❌ "weather"
✅ "Current weather forecast and climate trends for New York"

❌ "stocks"
✅ "Tesla stock performance and analyst predictions for Q1 2026"
```

### Research Strategy

```
✅ Start with broad query
✅ Refine based on results
✅ Cross-reference sources
✅ Check publication dates
✅ Verify credibility
❌ Single query only
❌ Ignore sources
```

### Model Selection

```
✅ Sonar: Quick facts, current events
✅ Sonar Pro: Comprehensive research
✅ Sonar Reasoning: Complex analysis
✅ Sonar Chat: Interactive exploration
❌ Always using most expensive
```

### Cost Management

```
✅ Use appropriate model
✅ Optimize query length
✅ Cache results
✅ Monitor usage
❌ Wasteful queries
❌ Ignore costs
```

## 🔗 Related Features

- [Research Mode](../modes/research.md) - Research-focused mode
- [Web Search](../features/04-web-search.md) - Web search plugin
- [Agents](../features/06-agents-automation.md) - Automated research

## 📚 Additional Resources

- [Perplexity Documentation](https://docs.perplexity.ai/)
- [Perplexity API Reference](https://docs.perplexity.ai/reference)
- [Perplexity Pricing](https://perplexity.ai/pricing)
- [Perplexity Blog](https://blog.perplexity.ai/)

## ⚠️ Limitations

- **Internet required** - Real-time search needs connection
- **Rate limits** - Varies by plan
- **Source availability** - Limited to public sources
- **Language support** - Best in English
- **Cost** - API charges apply

## 🆘 Need Help?

- Check [Research Mode Guide](../modes/research.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Provider Comparison](./comparison.md) →
