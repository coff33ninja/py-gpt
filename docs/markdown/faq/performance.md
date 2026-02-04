# Performance FAQ

Common questions about PyGPT performance and optimization.

## 🚀 Speed & Performance

### Q: Why are responses slow?

**A:** Several factors affect response speed:

**Model Speed:**
- GPT-4: Slower but higher quality
- GPT-3.5/Gemini Flash: Much faster
- Local models: Depends on hardware

**Solutions:**
```
✅ Use faster models (GPT-3.5, Gemini Flash)
✅ Reduce max tokens
✅ Shorter prompts
✅ Disable unnecessary plugins
✅ Check internet connection
```

### Q: How can I make PyGPT faster?

**A:** Optimization strategies:

**1. Model Selection:**
```
Fast models:
- Gemini Flash (fastest)
- GPT-3.5-turbo
- Mistral models
- DeepSeek
```

**2. Settings:**
```
- Reduce max tokens: 512-1024
- Lower temperature: 0.3-0.5
- Disable streaming if not needed
- Enable caching
```

**3. Plugins:**
```
- Disable unused plugins
- Limit tool calls
- Optimize plugin settings
```

**4. System:**
```
- Close other applications
- Good internet connection
- Sufficient RAM
- SSD storage
```

### Q: Why is the interface laggy?

**A:** UI performance issues:

**Causes:**
- Large conversation history
- Many contexts loaded
- Heavy plugins active
- Insufficient system resources

**Solutions:**
```
✅ Clear old contexts
✅ Reduce loaded contexts
✅ Disable heavy plugins
✅ Use compact mode
✅ Reduce font size
✅ Disable animations
```

### Q: Code execution is slow

**A:** Code Interpreter optimization:

**For Local Execution:**
```
- Use faster Python interpreter
- Optimize code
- Reduce library imports
- Cache results
```

**For Docker:**
```
- Use local execution instead
- Allocate more resources
- Use faster base image
- Keep container running
```

## 💾 Memory & Resources

### Q: PyGPT uses too much RAM

**A:** Memory optimization:

**Causes:**
- Many contexts in memory
- Large conversation history
- Heavy plugins
- Memory leaks

**Solutions:**
```
✅ Close unused contexts
✅ Clear old conversations
✅ Disable heavy plugins
✅ Restart PyGPT regularly
✅ Use 64-bit version
✅ Increase system RAM
```

**Memory Usage:**
```
Minimal: ~200MB
Normal: ~500MB
Heavy use: ~1-2GB
With local models: 4-16GB+
```

### Q: High CPU usage

**A:** CPU optimization:

**Causes:**
- Streaming responses
- Syntax highlighting
- Multiple plugins
- Background tasks

**Solutions:**
```
✅ Disable streaming
✅ Reduce syntax highlighting
✅ Disable unused plugins
✅ Close other applications
✅ Update to latest version
```

### Q: Disk space issues

**A:** Storage management:

**What Uses Space:**
```
- Context database: 10MB-1GB+
- Vector indexes: 100MB-10GB+
- Cache files: 10-100MB
- Logs: 1-10MB
- Backups: Varies
```

**Solutions:**
```
✅ Delete old contexts
✅ Clear vector indexes
✅ Clear cache
✅ Rotate logs
✅ Remove old backups
✅ Use external storage
```

## 🌐 Network & API

### Q: API calls are slow

**A:** Network optimization:

**Check:**
```
1. Internet speed
2. API endpoint location
3. Provider status
4. Rate limits
5. Firewall/proxy
```

**Solutions:**
```
✅ Use closer endpoint
✅ Check provider status
✅ Upgrade internet
✅ Use VPN if blocked
✅ Batch requests
```

### Q: Frequent timeouts

**A:** Timeout handling:

**Causes:**
- Slow internet
- Large requests
- Provider issues
- Firewall blocking

**Solutions:**
```
✅ Increase timeout: 60-120s
✅ Reduce request size
✅ Check provider status
✅ Use different provider
✅ Enable retries
```

### Q: Rate limit errors

**A:** Rate limit management:

**Understanding Limits:**
```
OpenAI: 60 req/min (varies by tier)
Google: Varies by model
Anthropic: Varies by plan
```

**Solutions:**
```
✅ Implement delays
✅ Batch requests
✅ Upgrade API plan
✅ Use multiple keys
✅ Monitor usage
```

## 🔍 Search & Indexing

### Q: Vector search is slow

**A:** Index optimization:

**Causes:**
- Large index
- Slow vector store
- Many documents
- Poor configuration

**Solutions:**
```
✅ Use faster vector store (Qdrant, Pinecone)
✅ Reduce chunk size
✅ Limit top K results
✅ Enable caching
✅ Use local embeddings
```

### Q: Indexing takes forever

**A:** Indexing optimization:

**Speed Up:**
```
✅ Batch documents
✅ Use faster embedding model
✅ Reduce chunk overlap
✅ Parallel processing
✅ Use local embeddings
```

**Time Estimates:**
```
100 pages: 1-5 minutes
1000 pages: 10-30 minutes
10000 pages: 1-3 hours
```

### Q: Web search is slow

**A:** Search optimization:

**Causes:**
- Many results requested
- Slow provider
- Content extraction
- Network latency

**Solutions:**
```
✅ Reduce max results: 5-10
✅ Use faster provider (DuckDuckGo)
✅ Disable content extraction
✅ Use cached results
```

## 🤖 Agent Performance

### Q: Agents are too slow

**A:** Agent optimization:

**Causes:**
- Many steps
- Complex tasks
- Tool calls
- Evaluation enabled

**Solutions:**
```
✅ Reduce max steps: 20-30
✅ Simplify tasks
✅ Disable evaluation
✅ Use faster model
✅ Limit tool calls
```

### Q: Agent gets stuck

**A:** Agent troubleshooting:

**Causes:**
- Infinite loops
- Unclear goals
- Tool failures
- Timeout issues

**Solutions:**
```
✅ Set lower max steps
✅ Clearer instructions
✅ Enable timeout
✅ Monitor progress
✅ Stop and restart
```

## 💻 Local Models

### Q: Ollama is very slow

**A:** Local model optimization:

**Hardware Requirements:**
```
Minimum:
- 8GB RAM
- 4 CPU cores
- SSD storage

Recommended:
- 16GB+ RAM
- 8+ CPU cores
- GPU (NVIDIA)
- NVMe SSD
```

**Optimization:**
```
✅ Use GPU acceleration
✅ Smaller models (7B vs 70B)
✅ Reduce context length
✅ Quantized models
✅ Optimize system
```

**Model Sizes:**
```
7B: Fast, good quality
13B: Balanced
30B: Slower, better quality
70B: Very slow, best quality
```

### Q: GPU not being used

**A:** GPU acceleration:

**Check:**
```
1. GPU drivers installed
2. CUDA/ROCm installed
3. Ollama configured for GPU
4. Model supports GPU
```

**Enable GPU:**
```
Ollama: Automatic if available
Check: nvidia-smi (NVIDIA)
Check: rocm-smi (AMD)
```

## 📊 Monitoring

### Q: How to monitor performance?

**A:** Performance monitoring:

**Built-in Tools:**
```
- Token counter
- Response time
- API usage stats
- Debug logs
```

**System Tools:**
```
- Task Manager (Windows)
- Activity Monitor (Mac)
- htop (Linux)
- Network monitor
```

**Metrics to Watch:**
```
- Response time
- Token usage
- Memory usage
- CPU usage
- Network speed
- API costs
```

## 🔧 Optimization Checklist

### Quick Wins

```
☑ Use faster models
☑ Reduce max tokens
☑ Disable unused plugins
☑ Clear old contexts
☑ Enable caching
☑ Good internet connection
☑ Close other apps
☑ Update PyGPT
```

### Advanced Optimization

```
☑ Optimize prompts
☑ Batch operations
☑ Use local models
☑ Configure vector store
☑ Tune model parameters
☑ Monitor usage
☑ Profile performance
☑ Hardware upgrade
```

## 🔗 Related Resources

- [Advanced Settings](../guides/07-advanced-settings.md)
- [Troubleshooting](../reference/troubleshooting.md)
- [Configuration Reference](../reference/config-reference.md)

## 🆘 Still Having Issues?

- Check [Troubleshooting Guide](../reference/troubleshooting.md)
- Visit [General FAQ](./general.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Last Updated:** February 2026
