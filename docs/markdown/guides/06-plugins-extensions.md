# Plugins & Extensions Guide

Installing, configuring, and creating plugins for PyGPT.

## 🔌 What Are Plugins?

Extensions that add new features and functionality to PyGPT.

### Built-in Plugins
- File operations
- Web search
- Code execution
- Calendar integration
- Custom commands

### Plugin Types
- Command plugins
- Tool plugins
- Provider plugins
- Data processors

---

## 📥 Installing Plugins

### Method 1: Plugin Folder

1. Create folder: `~/.pygpt/plugins/myplugin/`
2. Add `__init__.py` with plugin code
3. Restart PyGPT
4. Enable in Settings → Plugins

### Method 2: From Repository

1. Clone plugin repo
2. Copy to `~/.pygpt/plugins/`
3. Restart PyGPT
4. Enable in Settings

---

## ⚙️ Configuring Plugins

### Enable/Disable Plugin

1. Settings → Plugins
2. Find plugin in list
3. Toggle ON/OFF
4. Restart if needed

### Plugin Settings

Each plugin may have settings:
1. Settings → Plugins
2. Click plugin name
3. Adjust settings
4. Save changes

---

## 🎯 Popular Plugins

### File Operations Plugin
- Upload/download files
- File management
- Directory operations

### Web Search Plugin
- Search internet
- Real-time information
- Citation sources

### Code Execution
- Run Python code
- Data analysis
- Visualizations

---

## 💻 Creating Your First Plugin

### Basic Structure

```python
from pygpt_net.plugin.base import PluginBase

class MyPlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_plugin"
        self.name = "My Plugin"
    
    def handle(self, ctx, **kwargs):
        return "Plugin works!"
```

### Installation

1. Save as `~/.pygpt/plugins/my_plugin/__init__.py`
2. Restart PyGPT
3. Check Settings → Plugins
4. Enable plugin

---

## 📚 Resources

- [Plugin Development Guide](../development/plugin-development.md)
- [Architecture Overview](../development/architecture.md)
- [Examples](../../examples/)

---

**Next:** [Advanced Settings Guide](./07-advanced-settings.md) →
