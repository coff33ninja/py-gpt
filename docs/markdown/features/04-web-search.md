# Web Search

Search the internet and access real-time information.

## 🔍 Overview

Web Search enables AI models to search the internet for current information, news, data, and resources. Access real-time information beyond the model's training data.

**Key Features:**
- Multiple search providers
- Real-time results
- Source citations
- Content extraction
- Link following
- Result filtering

**Plugin:** Web Search (built-in)

## 🚀 Getting Started

### Enable Web Search

1. **Open Plugins**
   ```
   Menu → Plugins → Web Search
   ```

2. **Enable Plugin**
   - Toggle switch to ON
   - Select search provider
   - Configure settings

3. **Start Searching**
   - Ask AI to search
   - Results retrieved automatically
   - Sources cited

### Your First Search

```
You: What are the latest AI developments in 2026?

AI: Let me search for that...

[Searches web]

Based on recent sources:

1. GPT-5 was released in January 2026 [1]
2. Quantum AI breakthrough announced [2]
3. New regulations proposed in EU [3]

Sources:
[1] OpenAI Blog - https://...
[2] Nature - https://...
[3] EU Commission - https://...
```

## 🎯 Use Cases

### Current Events
```
"What happened in tech news today?"
"Latest developments in AI regulation"
"Recent breakthroughs in quantum computing"
```

### Real-Time Data
```
"Current weather in New York"
"Latest stock price for AAPL"
"Today's exchange rate USD to EUR"
```

### Research
```
"Recent studies on climate change"
"Latest research papers on LLMs"
"Current best practices for React"
```

### Fact Checking
```
"Verify this claim: ..."
"Is this information accurate: ..."
"Find sources for: ..."
```

### Product Information
```
"Latest iPhone specifications"
"Compare prices for laptops"
"Reviews for product X"
```

## ⚙️ Configuration

### Settings Location
`Plugins → Web Search → Settings`

### Search Providers

**DuckDuckGo**
- Privacy-focused
- No API key required
- Good general results
- Free

**Google**
- Most comprehensive
- Requires API key
- Best results
- Paid (free tier available)

**Microsoft Bing**
- Good results
- Requires API key
- Integration with Microsoft services
- Paid (free tier available)

**Configuration:**
```
Provider: DuckDuckGo / Google / Bing
API Key: [Your key if required]
Region: US / UK / etc.
Language: en / es / etc.
```

### Search Settings

**Max Results:**
```
Number of results: 5-50
Default: 10
More results = better coverage, slower
```

**Safe Search:**
```
Off: All results
Moderate: Filter explicit content
Strict: Maximum filtering
```

**Time Range:**
```
Any time
Past hour
Past 24 hours
Past week
Past month
Past year
```

**Result Type:**
```
All: Everything
News: News articles only
Images: Images only
Videos: Videos only
```

## 🔧 Features

### Automatic Search

AI decides when to search.

**Triggers:**
- Current events questions
- Real-time data requests
- "Search for..." commands
- Unknown information

**Example:**
```
You: What's the weather like today?

AI: [Automatically searches]
"Currently 72°F and sunny in [your location]"
```

### Manual Search

Explicitly request a search.

**Commands:**
```
"Search for Python tutorials"
"Look up latest AI news"
"Find information about quantum computing"
"Google best practices for React"
```

### Source Citations

All information includes sources.

**Citation Formats:**

**Inline:**
```
According to OpenAI [1], GPT-5 was released...
```

**Footnotes:**
```
GPT-5 was released in January 2026.[1]

[1] OpenAI Blog - https://...
```

**Bibliography:**
```
Sources:
1. OpenAI Blog - https://...
2. TechCrunch - https://...
3. The Verge - https://...
```

### Content Extraction

Extract content from search results.

**What's Extracted:**
- Page title
- Main content
- Publication date
- Author (if available)
- Summary

**Use Cases:**
- Read full articles
- Extract specific information
- Analyze content
- Compare sources

### Link Following

Follow links for more information.

**How it Works:**
1. Initial search
2. Find relevant link
3. Follow link
4. Extract content
5. Synthesize information

**Example:**
```
You: "Find and summarize the latest OpenAI blog post"

AI:
1. Searches for OpenAI blog
2. Finds latest post
3. Follows link
4. Reads content
5. Provides summary
```

### Result Filtering

Filter search results by criteria.

**Filters:**
- Domain (e.g., .edu, .gov)
- Date range
- Content type
- Language
- Region

**Example:**
```
"Search for Python tutorials from .edu sites"
"Find news from the past week"
"Look for academic papers on AI"
```

## 🎨 Advanced Features

### Multi-Query Search

Search multiple queries and combine results.

**Example:**
```
You: "Compare Python and JavaScript for web development"

AI:
1. Searches "Python web development"
2. Searches "JavaScript web development"
3. Searches "Python vs JavaScript"
4. Combines and analyzes results
5. Provides comparison
```

### Deep Research

Comprehensive multi-source research.

**Process:**
1. Initial broad search
2. Identify key topics
3. Deep dive into each
4. Cross-reference sources
5. Synthesize findings

**Use Cases:**
- Academic research
- Market analysis
- Technical investigation
- Comprehensive reports

### Real-Time Monitoring

Monitor topics for updates.

**Setup:**
```
"Monitor AI news and notify me of updates"
"Track mentions of [topic]"
"Alert me to new developments in [field]"
```

**Features:**
- Scheduled searches
- Change detection
- Notifications
- Summary reports

### Search History

Track and review past searches.

**Features:**
- View search history
- Repeat searches
- Compare results over time
- Export history

**Access:**
```
Tools → Web Search → Search History
```

## 🐛 Troubleshooting

### No Results Found
**Problem:** Search returns nothing

**Solutions:**
- Try different keywords
- Broaden search terms
- Check internet connection
- Verify API key (if required)
- Try different provider

### Slow Searches
**Problem:** Takes too long

**Solutions:**
- Reduce max results
- Use faster provider
- Check internet speed
- Disable content extraction
- Simplify query

### API Quota Exceeded
**Problem:** Hit API limits

**Solutions:**
- Wait for quota reset
- Upgrade API plan
- Switch to free provider (DuckDuckGo)
- Reduce search frequency

### Irrelevant Results
**Problem:** Results not relevant

**Solutions:**
- Use more specific keywords
- Add filters (date, domain)
- Try different search terms
- Use quotes for exact phrases
- Exclude terms with minus sign

### Access Denied
**Problem:** Can't access certain sites

**Solutions:**
- Check site availability
- Try different source
- Use VPN if region-blocked
- Check firewall settings

## 💡 Best Practices

### Effective Search Queries

```
❌ "AI"
✅ "Latest developments in large language models 2026"

❌ "weather"
✅ "Current weather forecast for New York City"

❌ "Python"
✅ "Python best practices for web scraping 2026"
```

### Source Evaluation

```
✅ Check multiple sources
✅ Verify publication dates
✅ Consider source credibility
✅ Cross-reference facts
❌ Trust single source
❌ Ignore dates
```

### Privacy

```
✅ Use DuckDuckGo for privacy
✅ Review search history
✅ Clear sensitive searches
✅ Be aware of tracking
❌ Search sensitive info without VPN
❌ Ignore privacy settings
```

### Efficiency

```
✅ Be specific in queries
✅ Use filters appropriately
✅ Limit result count
✅ Cache frequent searches
❌ Vague queries
❌ Always max results
```

## 🔗 Related Features

- [Research Mode](../modes/research.md) - Deep research
- [Agents](./06-agents-automation.md) - Automated research
- [File Operations](../guides/03-working-with-files.md) - Save results

## 📚 Additional Resources

- [DuckDuckGo Search Syntax](https://duckduckgo.com/duckduckgo-help-pages/results/syntax/)
- [Google Search Operators](https://support.google.com/websearch/answer/2466433)
- [Bing Search Tips](https://support.microsoft.com/en-us/topic/advanced-search-options-b92e25f1-0085-4271-bdf9-14aaea720930)

## ⚠️ Limitations

- **Internet required** - No offline search
- **API limits** - Quota restrictions
- **Result quality** - Varies by provider
- **Access restrictions** - Some sites block bots
- **Cost** - Paid APIs have charges
- **Privacy** - Searches may be tracked

## 💰 Cost Considerations

**Free Options:**
- DuckDuckGo: Completely free
- Google: Free tier available
- Bing: Free tier available

**Paid Options:**
- Google Custom Search: $5 per 1000 queries
- Bing Search API: Pay per query
- Premium features: Additional cost

**Cost-Saving Tips:**
- Use DuckDuckGo when possible
- Limit max results
- Cache frequent searches
- Monitor API usage

## 🆘 Need Help?

- Check [Research Mode](../modes/research.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Vector Store & RAG](./05-vector-store-rag.md) →
