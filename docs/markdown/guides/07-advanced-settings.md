# Advanced Settings Guide

Master PyGPT's advanced configuration options.

## ⚙️ Overview

PyGPT offers extensive configuration options for power users. Fine-tune every aspect of the application to match your workflow and preferences.

**Key Areas:**
- Model parameters
- API configuration
- Performance tuning
- Interface customization
- Security settings
- Debug options

## 🚀 Accessing Settings

### Settings Window

**Open Settings:**
```
Config → Settings
Or: Ctrl + ,
```

**Settings Categories:**
- General
- API Keys
- Models
- Indexes / LlamaIndex
- Agents
- Experts
- Remote Tools
- Audio
- Personalization
- Developer

## 🎯 General Settings

### Application

**Language:**
```
Interface language
18+ languages supported
Restart required
```

**Theme:**
```
Light / Dark / Custom
Color schemes
Font settings
```

**Layout:**
```
Window size
Panel positions
Splitter sizes
Compact mode
```

**Startup:**
```
Auto-load last context
Restore window position
Check for updates
Show tips
```

### Context

**Auto-save:**
```
Save frequency: Every message
Backup interval: 5 minutes
Max backups: 10
```

**Context Window:**
```
Max tokens: Model dependent
Truncation: Oldest first
Summary: Auto-generate
```

**History:**
```
Max contexts: Unlimited
Auto-delete old: Never
Export format: JSON
```

## 🔑 API Configuration

### Provider Settings

**OpenAI:**
```
API Key: [Your key]
Organization ID: [Optional]
Endpoint: https://api.openai.com/v1
Timeout: 60 seconds
Max retries: 3
```

**Google:**
```
API Key: [Your key]
Project ID: [Optional]
Endpoint: Default
VertexAI: Enable/Disable
```

**Anthropic:**
```
API Key: [Your key]
Endpoint: https://api.anthropic.com
Version: Latest
```

**Custom Endpoints:**
```
Base URL: Custom endpoint
Headers: Custom headers
Auth: Bearer token / API key
```

### Rate Limiting

**Request Limits:**
```
Max requests/minute: 60
Max tokens/minute: 90000
Retry delay: 1 second
Exponential backoff: Yes
```

**Queue Management:**
```
Queue size: 100
Priority: FIFO / LIFO
Timeout: 300 seconds
```

## 🤖 Model Parameters

### Temperature

**Range:** 0.0 - 2.0

**Values:**
```
0.0 = Deterministic, focused
0.3 = Factual, precise
0.7 = Balanced (default)
1.0 = Creative
1.5+ = Very creative, random
```

**Use Cases:**
```
Code: 0.0-0.3
Technical: 0.3-0.5
General: 0.5-0.8
Creative: 0.8-1.5
Experimental: 1.5+
```

### Top P (Nucleus Sampling)

**Range:** 0.0 - 1.0

**Values:**
```
0.1 = Very focused
0.5 = Moderately focused
0.9 = Balanced (default)
1.0 = Full diversity
```

**Recommendation:**
```
Use Temperature OR Top P
Not both simultaneously
Top P often more stable
```

### Frequency Penalty

**Range:** -2.0 to 2.0

**Values:**
```
-2.0 = Encourage repetition
0.0 = No penalty (default)
1.0 = Reduce repetition
2.0 = Strongly avoid repetition
```

**Use Cases:**
```
Lists: 0.0-0.5
Varied text: 0.5-1.0
Avoid repetition: 1.0-2.0
```

### Presence Penalty

**Range:** -2.0 to 2.0

**Values:**
```
-2.0 = Stay on topic
0.0 = No penalty (default)
1.0 = Explore new topics
2.0 = Strongly encourage variety
```

**Use Cases:**
```
Focused: 0.0-0.5
Balanced: 0.5-1.0
Exploratory: 1.0-2.0
```

### Max Tokens

**Output Length:**
```
Min: 1
Max: Model dependent
Default: 2048
```

**Recommendations:**
```
Short answers: 256-512
Medium: 512-2048
Long: 2048-4096
Very long: 4096+
```

## 🗄️ LlamaIndex Settings

### Vector Store

**Store Type:**
```
SimpleVectorStore (default)
ChromaDB
Pinecone
Qdrant
Redis
Elasticsearch
```

**Configuration:**
```
Storage path: ~/.pygpt/index
Persist: Yes
Batch size: 100
```

### Embeddings

**Model:**
```
OpenAI: text-embedding-3-small
OpenAI: text-embedding-3-large
Local: sentence-transformers
Google: Gemini embeddings
```

**Settings:**
```
Dimensions: 1536 / 3072
Batch size: 100
Cache: Enable
```

### Chunking

**Chunk Size:**
```
Small: 256-512 tokens
Medium: 512-1024 tokens
Large: 1024-2048 tokens
```

**Overlap:**
```
None: 0 tokens
Small: 20 tokens
Medium: 50 tokens
Large: 100 tokens
```

### Retrieval

**Top K:**
```
Results to retrieve: 3-10
Default: 5
More = more context
```

**Similarity:**
```
Threshold: 0.0-1.0
Default: 0.7
Higher = more similar
```

## 🤖 Agent Settings

### General

**Max Steps:**
```
Range: 10-100
Default: 50
More = more complex tasks
```

**Timeout:**
```
Range: 60-600 seconds
Default: 300
Per-step timeout
```

**Evaluation:**
```
Enable: Yes/No
Mode: Completion / Accuracy
Threshold: 80%
```

### Tools

**Enable Tools:**
```
☑ Web search
☑ File operations
☑ Code execution
☐ System commands
☐ Custom tools
```

**Tool Settings:**
```
Timeout: 30 seconds
Max retries: 3
Error handling: Continue / Stop
```

### Memory

**Short-term:**
```
Context window: Model limit
Variables: Persistent
State: Maintained
```

**Long-term:**
```
Database: SQLite
Retention: Unlimited
Search: Enabled
```

## 🎨 Interface Customization

### Appearance

**Font:**
```
Family: System default / Custom
Size: 9-16pt
Code font: Monospace
```

**Colors:**
```
Theme: Light / Dark
Accent: Blue / Custom
Syntax: Highlight scheme
```

**Layout:**
```
Compact mode: Yes/No
Show timestamps: Yes/No
Avatar display: Yes/No
Message spacing: Comfortable / Compact
```

### Behavior

**Auto-scroll:**
```
Scroll to new: Yes/No
Stay at position: Manual
Smooth scroll: Yes/No
```

**Input:**
```
Auto-focus: Yes/No
Clear on send: Yes/No
Save drafts: Yes/No
Multi-line: Shift+Enter
```

**Notifications:**
```
Sound: Enable/Disable
Desktop: Enable/Disable
Flash taskbar: Enable/Disable
```

## 🔒 Security Settings

### Privacy

**Data Retention:**
```
Local storage: Encrypted
Cloud sync: Disabled
Telemetry: Disabled
```

**API Keys:**
```
Storage: Encrypted
Display: Masked
Auto-clear: Never
```

### Permissions

**File Access:**
```
Working directory: Restricted
System files: Denied
Network: Allowed
```

**Code Execution:**
```
Sandbox: Docker
Permissions: Limited
Timeout: 30 seconds
```

## 🐛 Developer Settings

### Debug Mode

**Enable Debug:**
```
Log level: DEBUG
Verbose output: Yes
Show API calls: Yes
```

**Logging:**
```
File: app.log
Console: Yes
Max size: 10MB
Rotation: 5 files
```

### Performance

**Caching:**
```
Enable cache: Yes
Cache size: 100MB
TTL: 3600 seconds
```

**Threading:**
```
Max threads: 4
Async: Enable
Queue size: 100
```

### Testing

**Test Mode:**
```
Mock API: Enable/Disable
Fake responses: Enable/Disable
Delay: 0-5 seconds
```

## 💡 Optimization Tips

### Performance

**Fast Response:**
```
✅ Use faster models (GPT-3.5, Gemini Flash)
✅ Reduce max tokens
✅ Lower temperature
✅ Disable unnecessary plugins
✅ Enable caching
```

**Quality Output:**
```
✅ Use better models (GPT-4, Claude)
✅ Increase max tokens
✅ Optimize temperature
✅ Better prompts
✅ Enable evaluation
```

### Cost Optimization

**Reduce Costs:**
```
✅ Use cheaper models
✅ Shorter prompts
✅ Limit max tokens
✅ Cache results
✅ Batch requests
```

**Monitor Usage:**
```
✅ Track API calls
✅ Review token usage
✅ Set budgets
✅ Use local models when possible
```

### Reliability

**Improve Reliability:**
```
✅ Enable retries
✅ Increase timeout
✅ Error handling
✅ Fallback models
✅ Regular backups
```

## 🔗 Related Features

- [Models Configuration](../reference/config-reference.md) - Model settings
- [Keyboard Shortcuts](../reference/keyboard-shortcuts.md) - Shortcuts
- [Troubleshooting](../reference/troubleshooting.md) - Common issues

## 📚 Additional Resources

- [OpenAI API Parameters](https://platform.openai.com/docs/api-reference/chat/create)
- [LlamaIndex Configuration](https://docs.llamaindex.ai/en/stable/module_guides/supporting_modules/settings/)
- [Performance Tuning](https://docs.llamaindex.ai/en/stable/optimizing/)

## 🆘 Need Help?

- Check [Configuration Reference](../reference/config-reference.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Development Documentation](../development/architecture.md) →
