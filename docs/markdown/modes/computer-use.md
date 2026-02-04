# Computer Use Mode

Autonomous navigation and control of your computer environment.

## 🖥️ Overview

Computer Use mode enables AI models to autonomously interact with your computer environment, including:
- Taking screenshots
- Moving the mouse
- Clicking elements
- Typing text
- Executing commands
- Navigating applications

**Status:** Beta  
**Available Models:** `computer-use-preview`, `gemini-2.5-computer-use-preview-10-2025`

## ⚠️ Important Safety Notice

Computer Use mode gives the AI direct control over your computer. Use with caution:
- AI can click buttons and execute commands
- AI can access files and applications
- AI can modify system settings
- Always supervise AI actions
- Use in a safe/test environment when possible

## 🚀 Getting Started

### Prerequisites

1. **Supported Model**
   - Anthropic: `computer-use-preview`
   - Google: `gemini-2.5-computer-use-preview-10-2025`

2. **API Key**
   - Configure in `Config → Settings → API Keys`

3. **Sandbox (Optional)**
   - Playwright sandbox for safer execution
   - Configure in `Config → Settings → Computer Use`

### Enable Computer Use Mode

1. Launch PyGPT
2. Select mode: **Computer Use**
3. Choose a compatible model
4. Enable the Computer Use remote tool in settings

## 🎯 Use Cases

### System Automation
```
"Open my browser and navigate to GitHub"
"Find and open the latest PDF in my Downloads folder"
"Take a screenshot of my desktop"
```

### Application Control
```
"Open VS Code and create a new Python file"
"Switch to my email client and check for new messages"
"Close all browser tabs except the first one"
```

### Data Entry
```
"Fill out this form with the data from my clipboard"
"Copy text from this document to that spreadsheet"
"Update my calendar with these events"
```

### Testing & QA
```
"Test the login flow on this website"
"Click through all menu items and report any errors"
"Verify that all buttons on this page are clickable"
```

## ⚙️ Configuration

### Settings Location
`Config → Settings → Remote Tools → Computer Use`

### Available Options

**Sandbox Mode**
- `Disabled` - Direct system access (default)
- `Playwright` - Isolated browser environment
- Recommended for web-based tasks

**Screen Resolution**
- Set virtual screen size
- Default: Your current resolution
- Lower resolution = faster processing

**Action Delay**
- Delay between actions (ms)
- Default: 1000ms
- Increase for slower systems

**Max Actions**
- Maximum actions per request
- Default: 50
- Prevents infinite loops

## 🔧 How It Works

### 1. Screenshot Capture
AI takes a screenshot of your screen to understand the current state.

### 2. Action Planning
AI analyzes the screenshot and plans the next action:
- Mouse movement
- Click
- Keyboard input
- Scroll

### 3. Action Execution
AI executes the planned action on your system.

### 4. Verification
AI takes another screenshot to verify the action succeeded.

### 5. Iteration
Process repeats until the goal is achieved.

## 📋 Supported Actions

### Mouse Actions
- **Move** - Move cursor to coordinates
- **Click** - Left/right/middle click
- **Double Click** - Double-click at location
- **Drag** - Click and drag

### Keyboard Actions
- **Type** - Type text
- **Press** - Press specific keys (Enter, Tab, etc.)
- **Hotkeys** - Key combinations (Ctrl+C, etc.)

### Screen Actions
- **Screenshot** - Capture screen
- **Scroll** - Scroll up/down
- **Wait** - Wait for element/time

### System Actions
- **Execute** - Run system commands
- **Open** - Open applications
- **Close** - Close windows

## 🎨 Examples

### Example 1: Web Research
```
User: "Search for 'PyGPT documentation' on Google and open the first result"

AI Actions:
1. Takes screenshot
2. Locates browser icon
3. Clicks to open browser
4. Types in search bar
5. Presses Enter
6. Clicks first result
7. Confirms page loaded
```

### Example 2: File Management
```
User: "Find all .txt files in Documents and move them to a new folder called 'Text Files'"

AI Actions:
1. Opens file manager
2. Navigates to Documents
3. Searches for .txt files
4. Creates new folder
5. Selects all .txt files
6. Moves to new folder
7. Verifies completion
```

### Example 3: Application Testing
```
User: "Test the login form on localhost:3000"

AI Actions:
1. Opens browser
2. Navigates to localhost:3000
3. Locates login form
4. Enters test credentials
5. Clicks submit
6. Verifies redirect/error
7. Reports results
```

## 🛡️ Safety Features

### Confirmation Prompts
- AI asks before destructive actions
- User can approve/deny each action
- Configure in settings

### Action Logging
- All actions are logged
- Review in debug console
- Export logs for audit

### Sandbox Mode
- Isolated environment
- No system access
- Safe for testing

### Emergency Stop
- Press `Esc` to stop AI
- Or click Stop button
- AI halts immediately

## 🐛 Troubleshooting

### AI Can't Find Elements
**Problem:** AI can't locate buttons/fields

**Solutions:**
- Increase screen resolution
- Ensure elements are visible
- Maximize windows
- Use descriptive instructions

### Actions Too Slow
**Problem:** AI takes too long between actions

**Solutions:**
- Reduce action delay in settings
- Use faster model
- Simplify task instructions

### Sandbox Not Working
**Problem:** Playwright sandbox fails

**Solutions:**
- Install Playwright: `pip install playwright`
- Run: `playwright install`
- Check browser installation

### Permission Errors
**Problem:** AI can't access certain areas

**Solutions:**
- Run PyGPT with appropriate permissions
- Check OS security settings
- Disable sandbox for system tasks

## 💡 Best Practices

### Clear Instructions
```
❌ "Do something with my files"
✅ "Move all PDF files from Downloads to Documents/PDFs"
```

### Break Down Complex Tasks
```
❌ "Set up my entire development environment"
✅ "Install VS Code, then install Python extension, then create a new project"
```

### Verify Results
```
Always ask AI to confirm:
"Did the file move successfully?"
"Is the application now open?"
```

### Use Sandbox for Web Tasks
```
Enable Playwright sandbox for:
- Web browsing
- Form filling
- Website testing
```

## 🔗 Related Features

- [Agents & Automation](../features/06-agents-automation.md) - Autonomous task execution
- [Custom Commands](../features/08-custom-commands.md) - Create custom actions
- [Plugins](../guides/06-plugins-extensions.md) - Extend functionality

## 📚 Additional Resources

- [Computer Use API Documentation](https://docs.anthropic.com/computer-use)
- [Playwright Documentation](https://playwright.dev/)
- [PyGPT GitHub Issues](https://github.com/szczyglis-dev/py-gpt/issues)

## ⚠️ Limitations

- **Screen-based only** - AI sees what you see
- **No background tasks** - Must be visible on screen
- **Resolution dependent** - Works best at standard resolutions
- **Language dependent** - Works best with English UI
- **Speed** - Slower than direct API calls

## 🆘 Need Help?

- Check [Troubleshooting Guide](../reference/troubleshooting.md)
- Visit [FAQ](../faq/general.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Realtime + Audio Mode](./realtime-audio.md) →
