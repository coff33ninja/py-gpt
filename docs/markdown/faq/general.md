# Frequently Asked Questions (FAQ)

Answers to the most common questions about PyGPT.

## 🎯 General Questions

### Q: What is PyGPT?
**A:** PyGPT is a desktop AI assistant that connects to multiple AI providers (OpenAI, Google Gemini, Anthropic, etc.). It offers a user-friendly interface for chat, code execution, vision, audio, and more.

### Q: Is PyGPT free?
**A:** PyGPT application itself is free and open source. However, using cloud AI providers (OpenAI, Google, Anthropic) requires API keys which may have costs. Local alternatives like Ollama are completely free.

### Q: Can I use PyGPT offline?
**A:** Yes! Use Ollama (local AI) for completely offline operation. Otherwise, you need internet for cloud providers.

### Q: What are the system requirements?
**A:** 
- OS: Windows 10+, Ubuntu 20.04+, macOS 10.14+
- RAM: 8GB minimum (16GB recommended)
- Storage: 2GB+ free space
- Python: 3.10 or higher (if installing from source)

### Q: Which AI models are best?
**A:** Depends on use case:
- **Speed & Budget**: Gemini 2.5 Flash
- **Best Quality**: GPT-4o or Claude 3 Opus
- **Free**: Gemini (free tier) or Ollama (local)
- **Reasoning**: o1, o3, or DeepSeek R1

---

## 💻 Installation & Setup

### Q: How do I install PyGPT?
**A:** Multiple methods:

**Option 1: Binary (Easiest)**
- Download from [releases page](https://github.com/szczyglis-dev/py-gpt/releases)
- Run installer or executable
- Works immediately

**Option 2: PyPI**
```bash
pip install py-gpt
pygpt
```

**Option 3: Docker**
```bash
docker run -it szczyglis/py-gpt
```

**Option 4: Source**
```bash
git clone https://github.com/szczyglis-dev/py-gpt.git
cd py-gpt
pip install -e .
pygpt
```

### Q: Do I need Python installed?
**A:** 
- If using binary/installer: **No**
- If using pip: **Yes** (Python 3.10+)
- If using Docker: **No** (Docker handles it)

### Q: Where are my files stored?
**A:**
- Windows: `C:\Users\[YourUser]\AppData\Roaming\pygpt`
- Linux: `~/.pygpt`
- macOS: `~/Library/Application Support/pygpt`

### Q: How do I uninstall PyGPT?
**A:** 
- **Windows**: Settings → Apps → Uninstall
- **Linux**: `pip uninstall py-gpt` or `sudo apt remove py-gpt`
- **macOS**: Delete from Applications folder

---

## 🔑 API Keys & Setup

### Q: I don't have an API key. How do I get one?
**A:** See [API Key Setup Guide](../guides/02-api-key-setup.md). Each provider has different steps:
- Google: [aistudio.google.com](https://aistudio.google.com) (free!)
- OpenAI: [platform.openai.com](https://platform.openai.com) (paid)
- Anthropic: [console.anthropic.com](https://console.anthropic.com) (paid)

### Q: Is Google Gemini API really free?
**A:** Yes! Google offers a free tier with these limits:
- 15 requests/minute
- 1 million tokens/day
- Some advanced features available

Perfect for learning and testing.

### Q: Can I use multiple API keys?
**A:** Yes! Add multiple keys in Settings → API Keys, then switch models in chat.

### Q: My API key isn't working. What's wrong?
**A:** Common issues:
1. Extra spaces in key - copy carefully
2. Wrong key from different service
3. Key has expired - regenerate
4. No credits/quota - check provider dashboard
5. API not enabled - check provider settings

See [Troubleshooting](../reference/troubleshooting.md) for more.

### Q: How do I keep my API key safe?
**A:** Best practices:
- Never share key publicly
- Don't commit to git
- Store in environment variables
- Regenerate if leaked
- Use read-only tokens when available

---

## 💬 Chat & Usage

### Q: Can I use multiple models in one conversation?
**A:** Yes! Switch models mid-chat using the model dropdown. Context continues with new model.

### Q: What's the difference between modes?
**A:** 
- **Chat**: Normal conversation
- **Vision**: Analyze images
- **Audio**: Voice input/output
- **Code**: Execute code
- **Agent**: Autonomous task execution
- **Completion**: Text generation

See [Chat Modes Guide](../guides/01-chat-modes.md).

### Q: How do I attach files or images?
**A:** 
1. Click attachment button (📎)
2. Select file
3. Or drag & drop directly into chat

Supported: Images (JPG, PNG), Documents (PDF, TXT), Code files.

### Q: Why is my response incomplete?
**A:** Possible causes:
1. Hit token limit - increase in Settings
2. Model's output was cut off
3. Connection interrupted
4. Rate limited

Try again or use different model.

### Q: How do I export conversations?
**A:** 
1. Right-click on chat tab
2. Select "Export"
3. Choose format: Markdown, PDF, JSON
4. Save to folder

---

## 📊 Tokens & Costs

### Q: What are tokens?
**A:** Tokens are chunks of text that AI models process:
- Approximately 4 characters = 1 token
- 1 word ≈ 1.3 tokens
- Both input and output count

Example: "Hello world" ≈ 2 tokens

### Q: How much does it cost?
**A:** Varies by provider:
- **Google Gemini**: ~$0.00075 per 1K input tokens
- **OpenAI GPT-4o**: ~$0.015 per 1K input tokens
- **Claude 3**: ~$0.003 per 1K input tokens
- **Ollama**: Free (your computer)

Typical conversation: 2000-5000 tokens = $0.01-$0.05

### Q: How do I reduce token usage?
**A:**
1. Keep conversations focused
2. Regularly clear old messages
3. Use shorter prompts
4. Avoid pasting large documents
5. Switch to cheaper model

### Q: Why are my tokens so high?
**A:** Common reasons:
1. Long conversation history included
2. Large file attachments
3. Vision processing (uses more tokens)
4. Multiple images analyzed
5. Using expensive model (GPT-4)

Clear old messages to reset.

---

## 🎨 Customization

### Q: Can I change the appearance?
**A:** Yes! Settings → Interface:
- Theme (Dark/Light)
- Font size
- Color scheme
- Layout

### Q: How do I change the language?
**A:** Settings → General → Language

Supports: English, Polish, German, French, Spanish, Chinese, Japanese, etc.

### Q: Can I customize keyboard shortcuts?
**A:** Yes! Settings → Keyboard

Click shortcut to change it.

---

## 🔌 Plugins & Extensions

### Q: What are plugins?
**A:** Plugins extend PyGPT with new features:
- File operations
- Web search
- Code execution
- Custom commands
- Custom AI providers

### Q: How do I install a plugin?
**A:**
1. Copy plugin to `~/.pygpt/plugins`
2. Restart PyGPT
3. Go to Settings → Plugins
4. Enable plugin
5. Configure if needed

### Q: Can I create my own plugin?
**A:** Yes! See [Plugin Development Guide](../development/plugin-development.md)

Plugins are Python files extending PluginBase class.

### Q: Are plugins safe?
**A:** Only use plugins from trusted sources. Plugins have full code access.

---

## 🎤 Audio Features

### Q: How do I use voice input?
**A:**
1. Click 🎤 microphone button
2. Speak clearly
3. Click stop when done
4. Message appears in chat

Requires internet for transcription (uses Whisper API).

### Q: Can PyGPT speak responses?
**A:** Yes! Click 🔊 speaker icon after response
- Uses Text-to-Speech
- Supports different voices
- Adjustable speed/pitch

### Q: What languages are supported?
**A:** Most major languages:
- Speech recognition: 50+ languages
- Text-to-speech: 30+ languages

Set in Settings → Audio.

---

## 👁️ Vision Features

### Q: How do I use image analysis?
**A:**
1. Switch to Vision mode (if available)
2. Attach image
3. Ask about the image
4. AI analyzes and responds

### Q: What image formats are supported?
**A:** JPG, PNG, GIF, WebP
- Max size: 20MB
- Higher resolution = more tokens

### Q: Can I generate images?
**A:** Not yet in PyGPT. Planned for future release.

---

## 🖥️ Performance & Issues

### Q: PyGPT is slow. How do I fix it?
**A:** Try:
1. Close other apps (frees RAM)
2. Reduce max_tokens in Settings
3. Switch to faster model (Flash vs GPT-4)
4. Disable animations: Settings → Interface
5. Clear cache: Delete `~/.pygpt/cache`

### Q: The app crashes. What do I do?
**A:**
1. Check debug log: Settings → Debug
2. Try reinstalling
3. Clear cache and restart
4. Report issue with debug log

### Q: Connection keeps dropping. Why?
**A:**
1. Check internet connection
2. Check provider status
3. Try different model/provider
4. Check firewall settings

---

## 📚 Learning & Help

### Q: Where can I find more help?
**A:**
- [Documentation](../README.md) - All guides
- [GitHub Issues](https://github.com/szczyglis-dev/py-gpt/issues) - Report bugs
- [GitHub Discussions](https://github.com/szczyglis-dev/py-gpt/discussions) - Ask questions
- [Troubleshooting](../reference/troubleshooting.md) - Common issues

### Q: How do I contribute to PyGPT?
**A:**
1. Fork repository
2. Create feature branch
3. Make changes
4. Submit pull request

See [Contributing](../development/contributing.md) guide.

### Q: Is there a community?
**A:** Yes!
- GitHub Discussions
- Discord Server
- Reddit community

---

## 🔐 Privacy & Security

### Q: Is my data private?
**A:** 
- Chat data stored locally by default
- When you use cloud API, data sent to provider
- Check provider's privacy policy
- Never store sensitive data in conversations

### Q: What happens to my conversations?
**A:** 
- Local: Stored in `~/.pygpt` only
- Cloud API: Provider's privacy policy applies
- Backups: Export conversations manually

### Q: Can PyGPT access my files?
**A:** Only files you explicitly share:
1. Attach in chat (reads copy)
2. Upload to plugins
3. Doesn't scan file system

### Q: Is my API key safe?
**A:** 
- Stored locally (encrypted if enabled)
- Never logged publicly
- Only sent to official provider API
- Use environment variables for extra safety

---

## 🚀 Advanced

### Q: Can I use PyGPT programmatically?
**A:** Yes! Examples available in `/examples` folder:
- `example_llm.py` - Basic LLM usage
- `example_plugin.py` - Custom plugin
- `example_tool.py` - Custom tool

### Q: How do I contribute a provider?
**A:** See [Provider Integration Guide](../development/llm-integration.md)

Steps:
1. Create provider in `provider/llms/`
2. Implement required methods
3. Test thoroughly
4. Submit pull request

### Q: Can I use PyGPT in production?
**A:** PyGPT is primarily a desktop application, but the underlying libraries can be used programmatically. See examples for integration patterns.

---

## 📞 Still Have Questions?

1. **Search Documentation** - [Full Docs](../README.md)
2. **Check Troubleshooting** - [Troubleshooting Guide](../reference/troubleshooting.md)
3. **Ask Community** - GitHub Discussions
4. **Report Bug** - GitHub Issues (with debug info)

---

**More Help:**
- [Troubleshooting](../reference/troubleshooting.md) - Common issues
- [API Setup Guide](../guides/02-api-key-setup.md) - All API providers
- [First Steps](../getting-started/02-first-steps.md) - Getting started

---

**Last Updated:** 2025
