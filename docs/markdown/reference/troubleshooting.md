# Troubleshooting Guide

Solutions for common PyGPT issues.

## 🔧 Common Issues

### App Won't Start

**Symptom:** PyGPT fails to launch

**Solutions:**

1. **Check Python Version**
   ```powershell
   python --version
   # Should be 3.10 or higher
   ```

2. **Reinstall Application**
   ```powershell
   pip uninstall py-gpt
   pip install py-gpt
   pygpt
   ```

3. **Clear Cache**
   - Windows: Delete `%APPDATA%\pygpt\cache`
   - Linux: Delete `~/.pygpt/cache`
   - macOS: Delete `~/Library/Application Support/pygpt/cache`

4. **Check System Requirements**
   - 8GB+ RAM (16GB recommended)
   - 2GB+ free disk space
   - Windows 10+, Ubuntu 20.04+, or macOS 10.14+

---

### API Connection Issues

**Symptom:** "Connection failed" or "Network error"

**Check:**

1. **Internet Connection**
   ```powershell
   # Test connection
   ping google.com
   ```

2. **API Status**
   - OpenAI: [status.openai.com](https://status.openai.com)
   - Google: [status.cloud.google.com](https://status.cloud.google.com)
   - Anthropic: [status.anthropic.com](https://status.anthropic.com)

3. **Firewall/Proxy**
   - Check if Windows Firewall is blocking PyGPT
   - If behind proxy, configure in Settings → Network

4. **Try Different API**
   - Switch to local Ollama if cloud API down
   - Use different provider temporarily

---

### Invalid API Key

**Symptom:** "Invalid API key" or "Authentication failed"

**Troubleshooting:**

1. **Check Key Format**
   ```
   OpenAI:    sk-...
   Google:    AIzaSy...
   Anthropic: sk-ant-...
   ```

2. **Verify Key Works**
   - Test on provider's website first
   - Ensure no extra spaces: `key.strip()`
   - Check key hasn't expired

3. **Check Permissions**
   - Ensure API is enabled for the key
   - Verify account has credits/quota
   - Check key isn't IP-restricted

4. **Regenerate Key**
   - If suspected leak: Regenerate immediately
   - Wait a few minutes for propagation
   - Update in PyGPT Settings

---

### Slow Responses

**Symptom:** AI responses take very long

**Causes & Fixes:**

| Cause | Fix |
|-------|-----|
| Model too complex | Use faster model (Flash vs GPT-4) |
| Long context | Clear old messages |
| Rate limited | Wait or upgrade plan |
| Network slow | Check internet speed |
| CPU overloaded | Close other apps |

**Quick Fixes:**
```
1. Reduce max_tokens: Settings → Chat → Max Tokens
2. Use temperature: Settings → Chat → Temperature = 0.7
3. Disable streaming: Might speed up some models
4. Switch model: Try Flash instead of GPT-4
```

---

### High Token Usage / Costs

**Symptom:** Token counter shows high usage or bills increasing

**Analysis:**
```
Per message tokens = input + output

Example:
- Input: 2000 tokens (previous context)
- Output: 500 tokens (response)
- Total: 2500 tokens per message

Cost calculation:
- GPT-4o: $0.015/1K input = $0.03 per message
- Gemini: $0.00075/1K input = $0.0015 per message
```

**Cost Reduction:**
1. **Switch to cheaper model**
   - Use Gemini 2.5 Flash (cheapest)
   - Or use local Ollama (free)

2. **Reduce context**
   - Clear old messages periodically
   - Use shorter prompts
   - Disable RAG if not needed

3. **Monitor usage**
   - Check provider dashboard weekly
   - Set spending alerts
   - Review recent API calls

4. **Use free tier**
   - Gemini: Free tier available
   - Ollama: Completely free (local)

---

### Out of Memory Errors

**Symptom:** "Out of memory" or app crashes unexpectedly

**Solutions:**

1. **Close Other Apps**
   - Free up system RAM
   - Close browser tabs

2. **Reduce Model Size**
   - Use smaller models
   - Reduce batch size in settings

3. **Clear Database**
   - Old chats consume storage
   - Archive old conversations
   - Delete unused attachments

4. **Check Disk Space**
   ```powershell
   # Windows
   Get-Volume | Select-Object DriveLetter, Size, SizeRemaining
   ```

---

### UI Not Responding

**Symptom:** App freezes or buttons don't respond

**Solutions:**

1. **Wait**
   - App might be processing
   - Wait 10-30 seconds

2. **Interrupt Process**
   - Press `Ctrl + C` in terminal
   - Or find Python process in Task Manager

3. **Restart App**
   - Close: `Ctrl + Q`
   - Reopen: `pygpt`

4. **Disable Animations**
   - Settings → Interface → Disable Animations
   - May improve responsiveness

5. **Check System Resources**
   - Task Manager → Performance
   - Close memory-heavy apps

---

### Audio Issues

**Symptom:** Microphone not detecting or speech output not working

**Microphone Not Working:**
1. Check device in Settings → Audio Input
2. Test microphone in Windows Settings
3. Grant PyGPT microphone permission
4. Try different USB microphone

**Audio Output Not Working:**
1. Check speaker in Settings → Audio Output
2. Test speaker in Windows Settings
3. Increase volume
4. Try different audio format

**Whisper Errors:**
1. Ensure audio file is supported (WAV, MP3, M4A)
2. Check internet connection (needs cloud)
3. Use shorter audio files if timeout

---

### Vision/Image Issues

**Symptom:** Images not uploading or not processed

**Image Upload Fails:**
1. Check file size: Images should be < 20MB
2. Supported formats: JPG, PNG, GIF, WebP
3. Clear cache: Delete `~/.pygpt/cache`
4. Try smaller image

**Vision Model Errors:**
1. Ensure model supports vision (check Settings)
2. Check API has vision enabled
3. Verify API quota available
4. Try built-in model first

---

### Plugin Errors

**Symptom:** Plugin not loading or plugin crashes

**Plugin Not Found:**
1. Check plugin folder: `~/.pygpt/plugins`
2. Ensure plugin has required structure
3. Restart PyGPT to reload

**Plugin Crashes:**
1. Check error log: Settings → Debug → Error Log
2. Review plugin code for errors
3. Try disabling plugin
4. Report to plugin author

---

### Database Issues

**Symptom:** "Database error" or chats not saving

**Corruption:**
```powershell
# Backup existing database
cp ~/.pygpt/database.db ~/.pygpt/database.db.backup

# Delete and recreate
rm ~/.pygpt/database.db
# Restart PyGPT - will recreate
```

**Large Database:**
- Archive old chats
- Delete unused attachments
- Vacuum database: Settings → Database → Optimize

---

### Settings Not Saving

**Symptom:** Changes revert after restart

**Solutions:**
1. Check if using Settings correctly
2. Click "Save" button explicitly
3. Check file permissions
4. Check disk space available
5. Restart app and try again

---

## 📊 Debug Mode

### Enable Debug Logging

```
1. Settings → Advanced → Debug Mode
2. Click "Enable"
3. Restart PyGPT
4. Reproduce issue
5. Send logs to support
```

### View Debug Log
```
Settings → Debug → View Logs

Or file location:
Windows: %APPDATA%\pygpt\debug.log
Linux: ~/.pygpt/debug.log
```

### Debug Output
```
Each log entry shows:
[TIMESTAMP] [LEVEL] [MODULE] Message

Levels:
- DEBUG: Detailed information
- INFO: General information
- WARNING: Warning (might be issue)
- ERROR: Error occurred
- CRITICAL: Critical error
```

---

## 🧪 Testing Your Setup

### Connection Test

```
1. Settings → API Keys
2. Select an API key
3. Click "Test"
4. Should show "✓ Connection successful"
```

### Model Test

```
1. Select model
2. Type simple message: "Say hello"
3. Should respond with greeting
4. Check response time and tokens
```

### Full System Test

```
1. Test each API separately
2. Test with text message
3. Test with image attachment
4. Test with audio input
5. Test with plugin command
```

---

## 🆘 Getting Help

### Collect Information

When reporting issues:
1. **Error message** - Exact text
2. **Steps to reproduce** - How to trigger issue
3. **Debug log** - Settings → Debug
4. **System info** - OS, Python version, RAM
5. **Screenshots** - Visual evidence

### Report Issue

1. **GitHub Issues**
   - [github.com/szczyglis-dev/py-gpt/issues](https://github.com/szczyglis-dev/py-gpt/issues)
   - Search for similar issues first
   - Include all information above

2. **Discord Community**
   - [Discord Server](https://discord.gg/...)
   - Ask for help in #support channel
   - Share screenshots/logs

3. **Documentation**
   - [FAQ Guide](./faq.md)
   - [API Setup Guide](../guides/02-api-key-setup.md)
   - Search documentation site

---

## 📈 Performance Optimization

### Speed Up PyGPT

```
1. Use faster model (Flash vs GPT-4)
2. Reduce max_tokens
3. Disable plugins you don't use
4. Clear old chats regularly
5. Use local Ollama as backup
6. Disable animations: Settings → Interface
7. Disable auto-save: Settings → Storage
8. Close other applications
```

### Save Money on API Calls

```
1. Use free tier: Gemini or Ollama
2. Use cheaper model: Flash vs GPT-4
3. Reduce context: Clear old messages
4. Monitor usage: Check provider dashboard
5. Set spending alert
6. Use local model for development
```

---

## 📚 Resources

- [FAQ](./faq.md) - Frequently asked questions
- [API Setup](../guides/02-api-key-setup.md) - How to add API keys
- [First Steps](../getting-started/02-first-steps.md) - Getting started
- [GitHub Discussions](https://github.com/szczyglis-dev/py-gpt/discussions)

---

**Next**: [FAQ](./faq.md) →
