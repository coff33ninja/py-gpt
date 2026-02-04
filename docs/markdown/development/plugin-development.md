# Plugin Development Guide

How to create custom plugins for PyGPT.

## 🔧 Plugin Basics

### What Are Plugins?

Extensions that add features to PyGPT:
- Custom commands
- New tools
- Custom providers
- Data processors
- Integrations

### Plugin Structure

```python
from pygpt_net.plugin.base import PluginBase

class MyPlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_plugin"
        self.name = "My Custom Plugin"
    
    def handle(self, *args, **kwargs):
        # Your plugin code here
        pass
```

---

## 📁 Installation

### Create Plugin File

1. Create folder: `~/.pygpt/plugins/my_plugin/`
2. Create `__init__.py` with plugin code
3. Restart PyGPT
4. Enable in Settings → Plugins

### Plugin Folder Structure

```
~/.pygpt/plugins/
├── my_plugin/
│   ├── __init__.py      # Main plugin code
│   ├── config.json      # Configuration
│   └── README.md        # Documentation
```

---

## 💻 Writing Your First Plugin

### Minimal Example

```python
from pygpt_net.plugin.base import PluginBase

class MyPlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_plugin"
        self.name = "My First Plugin"
    
    def handle(self, ctx, **kwargs):
        # Receive context and arguments
        # Do something
        # Return result
        return "Plugin executed successfully"
```

---

## 🎯 Common Plugin Types

### Command Plugin

Adds new commands:

```python
class CommandPlugin(PluginBase):
    def handle(self, ctx, **kwargs):
        if ctx.command == "/mycommand":
            return "Command executed"
```

### Tool Plugin

Adds new tools:

```python
class ToolPlugin(PluginBase):
    def handle(self, ctx, **kwargs):
        tool_result = self.run_tool(ctx.tool_name, ctx.args)
        return tool_result
```

### Provider Plugin

Adds new AI provider:

```python
class ProviderPlugin(PluginBase):
    def handle(self, ctx, **kwargs):
        # Implement provider API calls
        response = self.call_api(ctx.prompt)
        return response
```

---

## 📚 Plugin API

### Available Methods

```python
# Configuration
self.get_config(key)        # Get config value
self.set_config(key, value) # Set config value

# Logging
self.log(message)           # Log message
self.debug(message)         # Debug log

# Context
self.get_context()          # Get current context
self.send_message(msg)      # Send message

# Tools
self.register_tool(name, func)  # Register tool
self.call_tool(name, args)      # Call tool
```

---

## 🧪 Testing Plugin

### Manual Testing

1. Create plugin in `~/.pygpt/plugins/`
2. Restart PyGPT
3. Check if plugin loads
4. Test functionality
5. Check debug log for errors

### Debug Logging

Enable debug mode:
1. Settings → Advanced → Debug Mode
2. Check log: `~/.pygpt/debug.log`
3. Look for plugin errors

---

## 📦 Distributing Plugin

### Create Package

1. Organize plugin folder
2. Add README.md
3. Add LICENSE
4. Create installation instructions

### Share Plugin

- GitHub repository
- PyPI package
- Plugin marketplace (when available)

---

## 🆘 Troubleshooting

### Plugin Won't Load

**Check:**
1. Plugin in correct folder?
2. `__init__.py` exists?
3. Syntax errors in code?
4. Debug log for details?

### Plugin Crashes

1. Check debug log
2. Test in isolation
3. Add error handling
4. Verify dependencies

---

## 📚 Resources

- [Architecture Guide](./architecture.md)
- [Example Plugins](../../examples/)
- [API Reference](./api-reference.md)

---

**Next:** [Contributing](./contributing.md) →
