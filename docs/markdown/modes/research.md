# Research Mode

Deep web searching and research with specialized AI models.

## 🔍 Overview

Research mode is designed for in-depth web searching and research tasks using specialized models:
- **Perplexity Sonar models** - Real-time web search and synthesis
- **OpenAI deep-research models** - Comprehensive research analysis
- **DeepSeek R1** - Advanced reasoning and research

**Key Features:**
- Real-time web access
- Source citations
- Deep analysis
- Multi-source synthesis
- Research-focused responses

## 🆚 vs Regular Chat with Web Search

### Research Mode
- ✅ Specialized research models
- ✅ Deep web analysis
- ✅ Multiple source synthesis
- ✅ Academic-style citations
- ✅ Comprehensive coverage
- ✅ Research-optimized prompts

### Chat Mode + Web Search Plugin
- Basic web search
- Single-source focus
- General-purpose models
- Simple citations
- Quick answers

## 🚀 Getting Started

### Prerequisites

1. **API Key**
   - **Perplexity:** Get from [perplexity.ai](https://perplexity.ai)
   - **OpenAI:** For deep-research models
   - Configure in `Config → Settings → API Keys`

2. **Supported Models**
   - Perplexity: `sonar`, `sonar-pro`, `sonar-reasoning`
   - OpenAI: `o3-deep-research`, `o4-mini-deep-research`
   - DeepSeek: `deepseek-r1`

### Enable Research Mode

1. Launch PyGPT
2. Select mode: **Research**
3. Choose a research model
4. Start your research query

## 🎯 Use Cases

### Academic Research
```
"Summarize recent advances in quantum computing from 2024-2026"
"What are the latest findings on climate change mitigation?"
"Compare different approaches to machine learning interpretability"
```

### Market Research
```
"Analyze the current state of the EV market"
"What are emerging trends in fintech?"
"Compare pricing strategies of major SaaS companies"
```

### Technical Research
```
"What are the best practices for microservices architecture in 2026?"
"Compare different approaches to database sharding"
"Latest developments in WebAssembly"
```

### News & Current Events
```
"What happened in tech news this week?"
"Summarize recent developments in AI regulation"
"Latest updates on space exploration"
```

## ⚙️ Configuration

### Settings Location
`Config → Settings → Research`

### Research Settings

**Search Depth**
- `Quick` - Fast, surface-level search
- `Standard` - Balanced depth and speed
- `Deep` - Comprehensive, slower search
- Default: Standard

**Max Sources**
- Number of sources to analyze
- Range: 5-50
- Default: 10
- More sources = better coverage, slower

**Citation Style**
- `Inline` - Citations in text
- `Footnotes` - Numbered references
- `Bibliography` - End of response
- Default: Inline

**Time Range**
- `Any time` - All available sources
- `Past year` - Recent information
- `Past month` - Very recent
- `Past week` - Latest news
- Default: Any time

## 🔧 Supported Models

### Perplexity Sonar Models

**sonar**
- Fast research
- Real-time web access
- Good for quick queries
- Cost-effective

**sonar-pro**
- Deep research
- Multiple source analysis
- Better synthesis
- Higher quality

**sonar-reasoning**
- Advanced reasoning
- Complex queries
- Multi-step analysis
- Best quality

**Configuration:**
```
Mode: Research
Model: sonar-pro
Provider: Perplexity
```

### OpenAI Deep Research Models

**o3-deep-research**
- Comprehensive analysis
- Multi-source synthesis
- Academic-quality research
- Slower but thorough

**o4-mini-deep-research**
- Faster research
- Good quality
- Cost-effective
- Balanced approach

**Configuration:**
```
Mode: Research
Model: o3-deep-research
Provider: OpenAI
```

### DeepSeek R1

**deepseek-r1**
- Advanced reasoning
- Research-focused
- Cost-effective
- Good for complex queries

**Configuration:**
```
Mode: Research
Model: deepseek-r1
Provider: DeepSeek
```

## 📋 Research Features

### Real-Time Web Access

Models search the web in real-time for current information.

**Benefits:**
- Latest information
- Current events
- Recent developments
- Up-to-date data

**Example:**
```
Query: "Latest AI breakthroughs in 2026"
Result: [Searches web, finds recent articles, synthesizes findings]
```

### Source Citations

All information includes source citations.

**Citation Formats:**
- **Inline:** "According to [Source Name](URL)..."
- **Footnotes:** "Recent studies show...[1]"
- **Bibliography:** Full list at end

**Example:**
```
"Recent research from MIT [1] shows that quantum computers 
can now solve certain problems 1000x faster than classical 
computers. This builds on earlier work from Google [2]..."

[1] MIT Technology Review - https://...
[2] Google AI Blog - https://...
```

### Multi-Source Synthesis

Combines information from multiple sources.

**Process:**
1. Search multiple sources
2. Extract relevant information
3. Cross-reference facts
4. Synthesize coherent response
5. Cite all sources

**Benefits:**
- Comprehensive coverage
- Balanced perspective
- Fact-checked information
- Multiple viewpoints

### Deep Analysis

Goes beyond surface-level information.

**Features:**
- Multi-step reasoning
- Context analysis
- Trend identification
- Pattern recognition
- Critical evaluation

## 🎨 Examples

### Example 1: Technology Research
```
User: "What are the latest developments in AI agents?"

AI: "Recent developments in AI agents (2026) include:

1. **Autonomous Planning** [1]
   - Agents can now plan multi-step tasks
   - Improved goal decomposition
   - Better error recovery

2. **Tool Integration** [2]
   - Native tool calling in most models
   - Broader tool ecosystem
   - Better tool selection

3. **Multi-Agent Systems** [3]
   - Agents collaborating on tasks
   - Specialized agent roles
   - Improved coordination

Sources:
[1] OpenAI Blog - https://...
[2] Anthropic Research - https://...
[3] Google DeepMind - https://..."
```

### Example 2: Market Analysis
```
User: "Analyze the current state of the electric vehicle market"

AI: "Electric Vehicle Market Analysis (2026):

**Market Size**
- Global EV sales: 18M units (2025) [1]
- Projected growth: 25% YoY [2]
- Market value: $500B [1]

**Key Players**
1. Tesla - 20% market share [3]
2. BYD - 18% market share [3]
3. VW Group - 12% market share [3]

**Trends**
- Battery costs down 40% since 2023 [4]
- Charging infrastructure expanding [5]
- Government incentives increasing [6]

**Challenges**
- Supply chain constraints [7]
- Charging infrastructure gaps [8]
- Price competition [9]

[Sources listed...]"
```

### Example 3: Academic Research
```
User: "Summarize recent research on climate change mitigation"

AI: "Recent Climate Change Mitigation Research (2024-2026):

**Carbon Capture**
- Direct air capture costs down 60% [1]
- New materials improve efficiency [2]
- Pilot projects showing promise [3]

**Renewable Energy**
- Solar efficiency reaches 30% [4]
- Wind power costs at record low [5]
- Grid storage improving [6]

**Policy Developments**
- 50+ countries commit to net-zero [7]
- Carbon pricing expanding [8]
- Green technology incentives [9]

**Emerging Technologies**
- Green hydrogen production [10]
- Advanced nuclear designs [11]
- Sustainable aviation fuel [12]

[Detailed citations...]"
```

## 🐛 Troubleshooting

### No Search Results
**Problem:** Model returns no results

**Solutions:**
- Check internet connection
- Verify API key is valid
- Try different search terms
- Check API quota/limits

### Outdated Information
**Problem:** Results seem old

**Solutions:**
- Set time range to "Past month"
- Use more specific date in query
- Try different model
- Verify model has web access

### Poor Quality Results
**Problem:** Results not comprehensive

**Solutions:**
- Increase max sources
- Use deeper search setting
- Try sonar-pro or deep-research model
- Refine query to be more specific

### Missing Citations
**Problem:** No source links provided

**Solutions:**
- Enable citations in settings
- Use research-specific model
- Check citation format setting
- Verify model supports citations

## 💡 Best Practices

### Write Clear Queries
```
❌ "AI stuff"
✅ "Latest developments in large language models in 2026"

❌ "Market info"
✅ "Current state of the smartphone market with market share data"
```

### Specify Time Range
```
✅ "Recent advances in quantum computing (2024-2026)"
✅ "What happened in tech news this week?"
✅ "Latest research on..."
```

### Request Specific Information
```
✅ "Compare pricing strategies with specific examples"
✅ "Include market share data and growth rates"
✅ "Provide citations from academic sources"
```

### Use Follow-Up Questions
```
Initial: "Overview of renewable energy trends"
Follow-up: "Focus on solar energy specifically"
Follow-up: "What are the cost trends?"
```

## 🔗 Related Features

- [Web Search Plugin](../features/04-web-search.md) - Basic web search
- [Chat Mode](../guides/01-chat-modes.md) - General chat
- [Agents](../features/06-agents-automation.md) - Autonomous research

## 📚 Additional Resources

- [Perplexity API Documentation](https://docs.perplexity.ai/)
- [OpenAI Research Models](https://platform.openai.com/docs/)
- [Research Best Practices](../guides/07-advanced-settings.md)

## ⚠️ Limitations

- **Internet required** - Real-time web access needed
- **API costs** - Research queries use more tokens
- **Speed** - Deep research takes longer
- **Source availability** - Limited to publicly accessible sources
- **Language** - Best results in English

## 💰 Cost Considerations

Research mode typically costs more than regular chat:
- More tokens per query
- Multiple API calls
- Web search costs
- Longer responses

**Cost-saving tips:**
- Use standard depth for most queries
- Limit max sources
- Use quick search when appropriate
- Choose cost-effective models

## 🆘 Need Help?

- Check [Web Search Guide](../features/04-web-search.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Experts Mode](./experts.md) →
