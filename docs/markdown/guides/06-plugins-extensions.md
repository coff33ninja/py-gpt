# Plugins & Extensions Guide

Extend PyGPT functionality with plugins and create your own.

## 🔌 Overview

Plugins extend PyGPT's capabilities by adding new features, tools, and integrations. Use built-in plugins or create custom ones for your specific needs.

**Key Features:**
- 30+ built-in plugins
- Easy enable/disable
- Configurable settings
- Custom plugin support
- Hot-reload capability
- Plugin marketplace

## 🚀 Getting Started

### Plugin Manager

**Access:**
```
Menu → Plugins
Or: Ctrl + P
```

**Interface:**
- Plugin list (left)
- Plugin details (center)
- Settings (right)
- Enable/disable toggles

### Enable a Plugin

1. **Open Plugin Manager**
   ```
   Menu → Plugins
   ```

2. **Find Plugin**
   - Browse list
   - Or search by name

3. **Enable Plugin**
   - Toggle switch to ON
   - Configure settings (if needed)
   - Click Save

4. **Use Plugin**
   - Plugin now active
   - Features available
   - Check documentation

## 📦 Built-in Plugins

### Essential Plugins

**Files I/O**
- Read/write files
- File management
- Directory operations
- File search

**Code Interpreter**
- Execute Python code
- IPython kernel
- Docker support
- Real-time execution

**Web Search**
- Search internet
- DuckDuckGo/Google/Bing
- Real-time information
- Source citations

**Chat with Files (LlamaIndex)**
- RAG integration
- Document Q&A
- Vector search
- Context retrieval

### Communication Plugins

**Google**
- Gmail integration
- Google Docs
- Google Drive
- Google Calendar
- Google Maps
- Google Colab

**Slack**
- Send messages
- Read channels
- File sharing
- Team communication

**Telegram**
- Send messages
- Bot integration
- File sharing
- Notifications

**X/Twitter**
- Post tweets
- Read timeline
- Search tweets
- Social integration

**Facebook**
- Post updates
- Read feed
- Messenger integration
- Social sharing

### Development Plugins

**GitHub**
- Repository management
- Issue tracking
- Pull requests
- Code search

**Bitbucket**
- Repository access
- Code management
- Team collaboration

**Serial Port**
- Serial communication
- Arduino/hardware
- Device control
- Data logging

### Utility Plugins

**System (OS)**
- System commands
- Process management
- System information
- File operations

**Custom Commands**
- Create custom tools
- Parameterized commands
- Quick execution
- Command library

**Crontab / Task Scheduler**
- Schedule tasks
- Automated execution
- Recurring jobs
- Background processing

**Audio Input**
- Voice recognition
- Speech-to-text
- Whisper integration
- Multiple providers

**Audio Output**
- Text-to-speech
- Voice synthesis
- Multiple voices
- Audio playback

### Integration Plugins

**MCP (Model Context Protocol)**
- Remote tools
- External services
- API integration
- Protocol support

**Server (FTP/SSH)**
- Remote servers
- File transfer
- Command execution
- Server management

**Tuya (IoT)**
- Smart home control
- Device management
- Automation
- IoT integration

### Information Plugins

**Wikipedia**
- Search articles
- Get summaries
- Reference information
- Knowledge base

**Wolfram Alpha**
- Mathematical queries
- Scientific data
- Computational knowledge
- Problem solving

**OpenStreetMap**
- Location data
- Map information
- Geographic queries
- Navigation

### Specialized Plugins

**Vision (inline)**
- Image analysis
- Any model support
- Camera integration
- OCR capabilities

**Image Generation (inline)**
- Generate images
- Any chat mode
- Multiple models
- Inline creation

**Agent (autonomous)**
- Autonomous operation
- Goal-driven
- Multi-step tasks
- Self-directed

## ⚙️ Plugin Configuration

### Common Settings

**Enable/Disable:**
```
Toggle: ON/OFF
Applies immediately
No restart needed
```

**API Keys:**
```
Some plugins need API keys
Configure in plugin settings
Stored securely
Per-plugin configuration
```

**Parameters:**
```
Adjust plugin behavior
Model selection
Timeout settings
Custom options
```

### Plugin-Specific Settings

**Files I/O:**
```
Working directory: ~/pygpt/files
Max file size: 100MB
Allowed extensions: All
Auto-create directories: Yes
```

**Code Interpreter:**
```
Execution mode: Local/Docker
Python path: /usr/bin/python3
Timeout: 30 seconds
Auto-install libraries: Yes
```

**Web Search:**
```
Provider: DuckDuckGo/Google/Bing
Max results: 10
Safe search: Moderate
Region: Auto
```

**Audio Input:**
```
Provider: OpenAI Whisper
Language: Auto-detect
Model: whisper-1
Timeout: 30 seconds
```

**Audio Output:**
```
Provider: OpenAI TTS
Voice: alloy
Speed: 1.0
Model: tts-1
```

## 🎯 Plugin Use Cases

### File Operations

```
You: "Read the file data.txt"
AI: [Uses Files I/O plugin]
"Here's the content of data.txt: ..."

You: "Save this to output.txt"
AI: [Writes file]
"Saved to output.txt"
```

### Code Execution

```
You: "Calculate the sum of numbers 1 to 100"
AI: [Uses Code Interpreter]
```python
result = sum(range(1, 101))
print(result)
```
Output: 5050
```

### Web Search

```
You: "What's the latest news about AI?"
AI: [Uses Web Search plugin]
"Here are the latest AI news stories:
1. [Article 1 with source]
2. [Article 2 with source]
..."
```

### Communication

```
You: "Send a message to #general on Slack: Meeting at 3pm"
AI: [Uses Slack plugin]
"Message sent to #general channel"
```

### Automation

```
You: "Schedule a daily backup at 2am"
AI: [Uses Crontab plugin]
"Scheduled daily backup at 2:00 AM"
```

## 🛠️ Creating Custom Plugins

### Plugin Structure

```python
# my_plugin.py

from pygpt_net.plugin.base import BasePlugin

class Plugin(BasePlugin):
    def __init__(self, *args, **kwargs):
        super(Plugin, self).__init__(*args, **kwargs)
        self.id = "my_plugin"
        self.name = "My Plugin"
        self.description = "Description of my plugin"
        self.order = 100
        
    def setup(self) -> dict:
        """Setup plugin configuration"""
        return {
            'api_key': {
                'type': 'text',
                'label': 'API Key',
                'value': '',
            }
        }
    
    def attach(self, window):
        """Attach plugin to window"""
        self.window = window
        
    def handle(self, event, *args, **kwargs):
        """Handle plugin events"""
        if event == "user.send":
            # Process user input
            pass
        elif event == "ai.response":
            # Process AI response
            pass
```

### Plugin Events

**Available Events:**
```
user.send - User sends message
ai.response - AI responds
context.before - Before context load
context.after - After context load
system.prompt - System prompt generation
tool.call - Tool call requested
plugin.settings.changed - Settings updated
```

### Plugin Tools

**Define Tools:**
```python
def get_tools(self) -> list:
    """Return list of tools"""
    return [
        {
            "name": "my_tool",
            "description": "Description of tool",
            "parameters": {
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "Parameter description"
                    }
                },
                "required": ["param1"]
            }
        }
    ]

def execute_tool(self, name: str, params: dict) -> str:
    """Execute tool"""
    if name == "my_tool":
        # Tool logic here
        return "Tool result"
```

### Plugin Installation

**Install Custom Plugin:**
```
1. Create plugin file: my_plugin.py
2. Copy to: ~/.pygpt/plugins/
3. Restart PyGPT
4. Plugin appears in list
5. Enable and configure
```

**Plugin Directory Structure:**
```
~/.pygpt/plugins/
├── my_plugin/
│   ├── __init__.py
│   ├── plugin.py
│   ├── config.json
│   └── README.md
```

## 🐛 Troubleshooting

### Plugin Not Loading

**Problem:** Plugin doesn't appear

**Solutions:**
- Check plugin file location
- Verify Python syntax
- Check plugin ID unique
- Review error logs
- Restart PyGPT

### Plugin Not Working

**Problem:** Plugin enabled but not functioning

**Solutions:**
- Check plugin settings
- Verify API keys configured
- Review error messages
- Check dependencies installed
- Test plugin individually

### Tool Not Called

**Problem:** AI doesn't use plugin tool

**Solutions:**
- Check tool description clear
- Verify tool enabled
- Enable "+Tools" checkbox
- Improve tool description
- Test with explicit request

### Settings Not Saving

**Problem:** Configuration doesn't persist

**Solutions:**
- Click Save button
- Check write permissions
- Verify config file location
- Check disk space
- Restart PyGPT

### Conflicts Between Plugins

**Problem:** Plugins interfere with each other

**Solutions:**
- Disable conflicting plugins
- Check plugin order
- Review plugin documentation
- Report issue
- Use one at a time

## 💡 Best Practices

### Plugin Selection

```
✅ Enable only needed plugins
✅ Configure properly
✅ Test individually
✅ Monitor performance
❌ Enable all plugins
❌ No configuration
```

### Plugin Development

```
✅ Clear tool descriptions
✅ Proper error handling
✅ Efficient code
✅ Good documentation
❌ Vague descriptions
❌ No error handling
```

### Performance

```
✅ Lightweight plugins
✅ Async operations
✅ Caching when possible
✅ Resource cleanup
❌ Heavy processing
❌ Blocking operations
```

### Security

```
✅ Validate inputs
✅ Secure API keys
✅ Limit permissions
✅ Sanitize outputs
❌ Trust all inputs
❌ Expose credentials
```

## 🔗 Related Features

- [Custom Commands](../features/08-custom-commands.md) - Custom tools
- [MCP Support](../features/09-mcp-support.md) - Remote tools
- [Plugin Development](../development/plugin-development.md) - Developer guide

## 📚 Additional Resources

- [Plugin Development Guide](../development/plugin-development.md)
- [Plugin API Reference](../development/api-reference.md)
- [Community Plugins](https://github.com/szczyglis-dev/py-gpt/discussions)
- [Plugin Examples](https://github.com/szczyglis-dev/py-gpt/tree/master/src/pygpt_net/plugin)

## 🆘 Need Help?

- Check [Plugin Development](../development/plugin-development.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Advanced Settings](./07-advanced-settings.md) →
