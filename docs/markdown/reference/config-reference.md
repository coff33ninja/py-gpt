# Configuration Reference

Complete guide to all PyGPT configuration options.

## 📍 Configuration Location

- **Windows**: `%APPDATA%\pygpt\config.json`
- **Linux**: `~/.pygpt/config.json`
- **macOS**: `~/Library/Application Support/pygpt/config.json`

---

## 🔑 Core Settings

### API Keys

```json
{
  "api_key": "sk-...",              // OpenAI key
  "api_key_google": "AIzaSy...",   // Google Gemini key
  "api_key_anthropic": "sk-ant-...", // Claude key
  "api_key_deepseek": "sk-...",     // DeepSeek key
  "api_key_mistral": "...",         // Mistral key
  "api_native_google": true         // Use native SDK
}
```

### Model Settings

```json
{
  "model": "gpt-4o",                // Default model
  "temperature": 0.7,               // Creativity (0-2)
  "max_tokens": 2000,               // Max response length
  "top_p": 1.0,                     // Nucleus sampling
}
```

---

## 🎨 Interface Settings

### Appearance

```json
{
  "theme": "dark",                  // dark or light
  "font_size": 12,                  // Font size in pt
  "font_family": "Courier New",     // Font name
  "width": 1200,                    // Window width
  "height": 800,                    // Window height
  "maximized": false,               // Window state
}
```

### Language

```json
{
  "lang": "en",                     // en, pl, de, fr, es, etc
}
```

---

## 🔐 API Settings

### OpenAI

```json
{
  "api_key": "sk-proj-...",         // API key
  "openai_org": "",                 // Organization (optional)
}
```

### Google

```json
{
  "api_key_google": "AIzaSy...",   // API key
  "api_native_google": false,       // Use native SDK
  "api_native_google.use_vertex": false,  // Use VertexAI
  "api_native_google.cloud_project": "", // GCP project
}
```

### Anthropic

```json
{
  "api_key_anthropic": "sk-ant-...", // API key
}
```

---

## 🔊 Audio Settings

### Speech Input

```json
{
  "audio_input_device": "default",  // Microphone
  "audio_input_lang": "en",         // Language
  "audio_input_model": "whisper",   // Model
}
```

### Speech Output

```json
{
  "audio_output_device": "default", // Speaker
  "audio_output_voice": "default",  // Voice type
  "audio_output_speed": 1.0,        // Speed (0.5-2.0)
  "audio_output_lang": "en",        // Language
}
```

---

## 💾 Storage Settings

```json
{
  "data_dir": "~/.pygpt/data",      // Data directory
  "db_path": "~/.pygpt/database.db", // Database path
  "auto_save": true,                // Auto-save conversations
  "save_interval": 60,              // Save every 60 seconds
}
```

---

## 🔌 Plugin Settings

```json
{
  "plugins_enabled": true,          // Enable plugins
  "plugins_dir": "~/.pygpt/plugins", // Plugins folder
  "plugin_file_commands": true,     // File operations plugin
  "plugin_web_search": true,        // Web search plugin
  "plugin_code_execution": true,    // Code execution plugin
}
```

---

## 🧪 Debug Settings

```json
{
  "debug": false,                   // Debug mode
  "debug_file": "~/.pygpt/debug.log", // Debug log file
  "log_level": "INFO",              // Log level
  "verbose": false,                 // Verbose output
}
```

---

## 📊 Advanced Settings

```json
{
  "context_window": 8000,           // Context size
  "token_counter": true,            // Show token count
  "token_limit_alert": false,       // Alert on limit
  "stream_responses": true,         // Stream responses
  "streaming_chunk_size": 50,       // Chunk size
  "timeout": 300,                   // API timeout (sec)
  "retry_attempts": 3,              // Retry API calls
}
```

---

## 🌐 Network Settings

```json
{
  "proxy_enabled": false,           // Use proxy
  "proxy_host": "proxy.example.com", // Proxy host
  "proxy_port": 8080,               // Proxy port
  "proxy_username": "",             // Proxy user
  "proxy_password": "",             // Proxy password
  "ssl_verify": true,               // Verify SSL
}
```

---

## 📚 Example config.json

```json
{
  "api_key": "sk-proj-example",
  "api_key_google": "AIzaSy-example",
  "model": "gpt-4o",
  "temperature": 0.7,
  "max_tokens": 2000,
  "theme": "dark",
  "font_size": 12,
  "lang": "en",
  "debug": false,
  "auto_save": true,
  "plugins_enabled": true,
  "stream_responses": true
}
```

---

## ✏️ Editing config.json

### Method 1: UI (Recommended)
1. Settings → each option
2. Changes saved automatically

### Method 2: Manual Edit
1. Close PyGPT
2. Edit `config.json` with text editor
3. Save file
4. Reopen PyGPT

⚠️ **Warning**: Invalid JSON breaks config!

---

## 🔄 Config Reset

### Reset to Defaults

1. Close PyGPT
2. Delete `config.json`
3. Reopen PyGPT
4. Settings reset to defaults

### Backup Config

```bash
# Windows
copy %APPDATA%\pygpt\config.json config.backup.json

# Linux
cp ~/.pygpt/config.json config.backup.json
```

---

## 🆘 Common Issues

### "Invalid config"
- Check JSON syntax
- Use JSON validator
- Restore from backup
- Reset to defaults

### "Config not loading"
- Check file permissions
- Verify file path
- Check file format
- Try resetting

---

**Next:** [Keyboard Shortcuts](./keyboard-shortcuts.md) →
