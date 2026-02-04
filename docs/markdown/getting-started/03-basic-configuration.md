# Basic Configuration

Learn how to configure PyGPT for your first time and customize the experience to your needs.

## 🔧 Accessing Settings

### Method 1: Settings Menu
- Look for **⚙️ Settings** icon (usually top-right)
- Or: Menu → Preferences/Settings
- Or: Keyboard shortcut `Ctrl+,` (Ctrl+comma)

### Method 2: Settings Dialog
- Window → Settings
- Or first-run configuration wizard

---

## 🔑 Adding Your First API Key

### Step 1: Get an API Key
Choose one provider to start:

| Provider | Free Tier | Setup Time |
|----------|-----------|-----------|
| **Google Gemini** | ✅ Yes | 2 minutes |
| **OpenAI** | ❌ No (needs card) | 5 minutes |
| **Anthropic Claude** | ❌ No | 5 minutes |

### Step 2: Add to PyGPT

#### For Google Gemini
1. Open Settings
2. Find **"API Keys"** section
3. Locate **"Google API key"** field
4. Paste your key
5. Click **"Save"** or **"Test Connection"**

#### For OpenAI
1. Open Settings
2. Find **"API Keys"** section
3. Locate **"OpenAI API key"** field
4. Paste your key
5. Click **"Save"**

#### For Other Providers
Similar process - find provider-specific key field and paste

### Step 3: Test the Connection
```
Click "Test" next to API key field
Expected: "✓ Connection successful"
```

---

## 🎨 Interface & Appearance

### Theme Settings
1. Go to Settings → **Appearance** or **UI**
2. Choose theme:
   - **Dark Mode** (easier on eyes, default)
   - **Light Mode** (better for bright environments)
   - **Auto** (switches based on system)

### Font Size
1. Settings → **Display** or **Interface**
2. Adjust:
   - **Chat text size** (main conversation)
   - **Input text size** (your message box)
   - **UI scale** (buttons, icons)

### Layout
1. Settings → **Layout**
2. Options:
   - **Single column** (full width chat)
   - **Split view** (chat + sidebar)
   - **Compact** (minimal space)
   - **Expanded** (more features visible)

---

## 🌐 Language Settings

### Change Interface Language
1. Settings → **Language** or **Localization**
2. Select from supported languages:
   - English, Polish, Spanish, French, German, etc.
3. Changes take effect on restart

### Chat Language
- AI respects your language preference
- Respond in any language, AI matches it
- Or set preferred language in prompts

---

## 🤖 Model Selection

### Default Model
1. Settings → **Models** or **LLM**
2. Find **"Default model"** dropdown
3. Select preferred model:
   - For beginners: `gpt-3.5-turbo` or `gemini-2.5-flash`
   - For better results: `gpt-4` or `claude-3-opus`
   - For fast/cheap: `gemini-2.5-flash` or `gpt-3.5-turbo`

### Quick Model Change
- Main window has **Model dropdown** at top
- Click to switch models mid-conversation (may lose context)

---

## 💬 Chat Behavior

### Message Settings
1. Settings → **Chat** or **Behavior**

| Setting | Options | Recommendation |
|---------|---------|-----------------|
| **Stream responses** | On/Off | On (see response as it generates) |
| **Auto-copy on response** | On/Off | Off (copy manually when needed) |
| **Show timestamp** | On/Off | On (track when each message sent) |
| **Clear after send** | On/Off | On (clean input box automatically) |

### Temperature
- **What it does**: Controls creativity vs consistency
- **Scale**: 0.0 (always same) → 1.0 (very creative)
- **For beginners**: Leave at default (0.7)
- **For creative tasks**: Increase to 0.8-1.0
- **For factual tasks**: Decrease to 0.3-0.5

### Max Tokens
- **What it does**: Max length of response
- **Recommendation**: 2048 for balanced responses
- **Increase for**: Longer essays, code samples
- **Decrease for**: Quick answers, summaries

---

## 💾 Storage & Files

### Chat History
1. Settings → **Storage** or **Data**
2. Options:
   - **Save chats** (On/Off)
   - **Auto-save interval** (how often to save)
   - **Keep chat history** (number of recent chats to keep)

### Data Location
- See where PyGPT stores data:
  - Windows: `%APPDATA%\pygpt`
  - Linux: `~/.pygpt`
  - macOS: `~/Library/Application Support/pygpt`

### Clear Data
- **Clear chat history**: Settings → Storage → Clear
- **Clear cache**: Settings → Advanced → Clear cache
- **Factory reset**: Settings → Advanced → Reset to defaults

⚠️ Warning: These actions cannot be undone!

---

## 🔒 Privacy & Security

### Data Usage
1. Settings → **Privacy** or **Security**

| Option | What it means |
|--------|--------------|
| **Send usage data** | Share errors/analytics with PyGPT |
| **Enable telemetry** | Help improve PyGPT |
| **Anonymous usage** | No personal info included |

### API Key Protection
- ✅ API keys stored locally, never sent elsewhere
- ✅ Keys never shown in chat history
- ⚠️ Keys stored in plain text on your computer
- Recommendation: Use read-only API keys if available

---

## 🔔 Notifications & Audio

### Sound Settings
1. Settings → **Audio** or **Notifications**

| Setting | Purpose |
|---------|---------|
| **Message notification sound** | Alert when AI responds |
| **Error sound** | Alert on errors |
| **Volume** | Adjust sound level |

### Notifications
- **Show desktop notifications** (On/Off)
- **Notify on response** (quick alerts)
- **Sound on new chat** (confirm new conversation)

---

## ⌨️ Keyboard Shortcuts

### Customize Shortcuts
1. Settings → **Shortcuts** or **Keybindings**
2. Find shortcut you want to change
3. Click and press new key combination
4. Click **"Bind"** to save

### Default Shortcuts
| Shortcut | Action |
|----------|--------|
| `Enter` | Send message |
| `Shift+Enter` | New line |
| `Ctrl+N` | New chat |
| `Ctrl+,` | Settings |
| `Ctrl+K` | Clear chat |
| `Ctrl+S` | Save chat |
| `F1` | Help |

---

## 🔌 Proxy Settings

### If Behind Corporate Firewall
1. Settings → **Network** or **Advanced**
2. Enable **Use proxy**
3. Enter proxy URL
4. Format: `http://user:pass@proxy.com:8080`

---

## 📦 Plugin Settings

### Enable/Disable Plugins
1. Settings → **Plugins**
2. Toggle plugins On/Off:
   - **Code Interpreter** (execute Python)
   - **Web Search** (search internet)
   - **File I/O** (read/write files)
   - Others...

### Plugin Configuration
- Click plugin name to configure options
- Each plugin has its own settings

---

## ✅ Configuration Checklist

After setting up PyGPT, you should have:

- [ ] ✅ API key added (at least one)
- [ ] ✅ Model selected
- [ ] ✅ Theme set (Dark/Light)
- [ ] ✅ Language configured
- [ ] ✅ Chat behavior configured
- [ ] ✅ Saved settings (test connection works)

---

## 🧪 Testing Your Setup

### Quick Test
1. Create new chat (`Ctrl+N`)
2. Type: "Hello! Are you working?"
3. Press Enter
4. Wait for response

**Should take**: 2-10 seconds depending on model/internet

### If It Doesn't Work
See [Troubleshooting](../reference/troubleshooting.md)

---

## Settings Structure

```
Settings Root
├── API Keys
│   ├── OpenAI API key
│   ├── Google API key
│   └── Other providers
├── Appearance
│   ├── Theme
│   ├── Font size
│   └── Layout
├── Chat
│   ├── Default model
│   ├── Temperature
│   ├── Max tokens
│   └── Behavior
├── Storage
│   ├── Save chats
│   ├── Data location
│   └── Clear data
├── Privacy
│   ├── Data usage
│   └── Anonymous mode
├── Audio
│   ├── Notifications
│   └── Sound
├── Shortcuts
│   └── Keyboard bindings
└── Advanced
    ├── Network/Proxy
    ├── Plugins
    └── Debug mode
```

---

## Common Configuration Issues

### Issue: Changes Don't Save
- ✓ Click **Save** button at bottom of settings
- ✓ Close and reopen PyGPT to verify

### Issue: Can't Find Setting
- ✓ Use search in settings (if available)
- ✓ Check different tabs/sections
- ✓ Check Settings → Advanced

### Issue: Reverted to Defaults
- ✓ Settings → Restore defaults?
- ✓ Or check if auto-sync is enabled

---

## Next Steps

- ✅ [First Steps Guide](./02-first-steps.md) - Start chatting
- ✅ [Add More API Keys](../guides/02-api-key-setup.md)
- ✅ [Explore Features](../features/)
- ✅ [Advanced Settings](../guides/07-advanced-settings.md)

---

## Getting Help

- 📖 [FAQ](../faq/)
- 🐛 [Troubleshooting](../reference/troubleshooting.md)
- ⚙️ [Full Config Reference](../reference/config-reference.md)
- 💬 [Discord Community](https://pygpt.net/discord)

---

**Ready to chat?** [First Steps Guide](./02-first-steps.md) →
