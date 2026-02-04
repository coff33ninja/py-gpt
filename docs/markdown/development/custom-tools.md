# Custom Tools Development Guide

Learn how to create custom tools and commands for PyGPT to extend its capabilities.

## 🛠️ What Are Custom Tools?

Custom tools are specialized functions that PyGPT can call to perform specific tasks:
- File operations (read, write, search)
- Web interactions (scraping, API calls)
- System commands (execute scripts, manage processes)
- Data processing (parse, transform, analyze)
- External integrations (databases, services, APIs)

### Tools vs Plugins

**Tools**: Specific functions AI can call during conversation
**Plugins**: Broader extensions that add features to PyGPT

Tools are typically registered through plugins but focus on discrete, callable operations.

---

## 🎯 Tool Architecture

### Tool Structure

```python
from pygpt_net.plugin.base import PluginBase

class MyToolPlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_tool"
        self.name = "My Custom Tool"
        
    def setup(self):
        """Register tools"""
        self.register_tool("my_function", self.my_function)
    
    def my_function(self, arg1: str, arg2: int) -> str:
        """
        Tool function that AI can call
        
        Args:
            arg1: Description of first argument
            arg2: Description of second argument
            
        Returns:
            Result string
        """
        result = f"Processed {arg1} with {arg2}"
        return result
```

### Tool Registration

Tools must be registered in the plugin's `setup()` method:

```python
def setup(self):
    # Register single tool
    self.register_tool("tool_name", self.tool_function)
    
    # Register multiple tools
    tools = {
        "read_file": self.read_file,
        "write_file": self.write_file,
        "search_files": self.search_files,
    }
    for name, func in tools.items():
        self.register_tool(name, func)
```

---

## 📝 Creating Your First Tool

### Step 1: Create Plugin File

Create `~/.pygpt/plugins/my_tools/__init__.py`:

```python
from pygpt_net.plugin.base import PluginBase

class MyToolsPlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_tools"
        self.name = "My Custom Tools"
        self.description = "Collection of custom tools"
        
    def setup(self):
        """Initialize and register tools"""
        self.register_tool("calculate", self.calculate)
        self.register_tool("format_text", self.format_text)
    
    def calculate(self, expression: str) -> float:
        """
        Evaluate mathematical expression
        
        Args:
            expression: Math expression to evaluate
            
        Returns:
            Calculation result
        """
        try:
            result = eval(expression)
            return float(result)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def format_text(self, text: str, style: str = "upper") -> str:
        """
        Format text in various styles
        
        Args:
            text: Text to format
            style: Format style (upper, lower, title, reverse)
            
        Returns:
            Formatted text
        """
        styles = {
            "upper": text.upper(),
            "lower": text.lower(),
            "title": text.title(),
            "reverse": text[::-1],
        }
        return styles.get(style, text)
```

### Step 2: Enable Plugin

1. Restart PyGPT
2. Go to Settings → Plugins
3. Enable "My Custom Tools"
4. Save settings

### Step 3: Test Tool

In chat, ask AI to use your tool:
```
User: Calculate 25 * 4 + 10
AI: [calls calculate tool with "25 * 4 + 10"]
Result: 110.0
```

---

## 🔧 Advanced Tool Patterns

### File Operations Tool

```python
import os
from pathlib import Path

class FileToolsPlugin(PluginBase):
    def setup(self):
        self.register_tool("read_file", self.read_file)
        self.register_tool("write_file", self.write_file)
        self.register_tool("list_files", self.list_files)
    
    def read_file(self, filepath: str) -> str:
        """Read file contents"""
        try:
            path = Path(filepath).expanduser()
            if not path.exists():
                return f"Error: File not found: {filepath}"
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            return content
        except Exception as e:
            return f"Error reading file: {str(e)}"
    
    def write_file(self, filepath: str, content: str) -> str:
        """Write content to file"""
        try:
            path = Path(filepath).expanduser()
            path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Successfully wrote to {filepath}"
        except Exception as e:
            return f"Error writing file: {str(e)}"
    
    def list_files(self, directory: str, pattern: str = "*") -> str:
        """List files in directory"""
        try:
            path = Path(directory).expanduser()
            if not path.exists():
                return f"Error: Directory not found: {directory}"
            
            files = list(path.glob(pattern))
            file_list = "\n".join([f.name for f in files])
            return f"Files in {directory}:\n{file_list}"
        except Exception as e:
            return f"Error listing files: {str(e)}"
```

### Web API Tool

```python
import requests
import json

class WebAPIPlugin(PluginBase):
    def setup(self):
        self.register_tool("fetch_url", self.fetch_url)
        self.register_tool("post_data", self.post_data)
    
    def fetch_url(self, url: str, headers: dict = None) -> str:
        """Fetch data from URL"""
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Try to parse as JSON
            try:
                data = response.json()
                return json.dumps(data, indent=2)
            except:
                return response.text
        except Exception as e:
            return f"Error fetching URL: {str(e)}"
    
    def post_data(self, url: str, data: dict, headers: dict = None) -> str:
        """POST data to URL"""
        try:
            response = requests.post(
                url, 
                json=data, 
                headers=headers, 
                timeout=10
            )
            response.raise_for_status()
            return f"Success: {response.status_code}"
        except Exception as e:
            return f"Error posting data: {str(e)}"
```

### Database Tool

```python
import sqlite3
from typing import List, Dict

class DatabasePlugin(PluginBase):
    def setup(self):
        self.register_tool("query_db", self.query_db)
        self.register_tool("execute_sql", self.execute_sql)
    
    def query_db(self, db_path: str, query: str) -> str:
        """Execute SELECT query"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            
            # Get column names
            columns = [desc[0] for desc in cursor.description]
            
            # Fetch results
            rows = cursor.fetchall()
            conn.close()
            
            # Format as table
            result = f"Columns: {', '.join(columns)}\n\n"
            for row in rows:
                result += " | ".join(str(val) for val in row) + "\n"
            
            return result
        except Exception as e:
            return f"Database error: {str(e)}"
    
    def execute_sql(self, db_path: str, sql: str) -> str:
        """Execute INSERT/UPDATE/DELETE"""
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            affected = cursor.rowcount
            conn.close()
            
            return f"Success: {affected} rows affected"
        except Exception as e:
            return f"Database error: {str(e)}"
```

### System Command Tool

```python
import subprocess
import shlex

class SystemPlugin(PluginBase):
    def setup(self):
        self.register_tool("run_command", self.run_command)
        self.register_tool("check_process", self.check_process)
    
    def run_command(self, command: str, timeout: int = 30) -> str:
        """Execute system command"""
        try:
            # Security: validate command
            if any(dangerous in command for dangerous in ['rm -rf', 'del /f']):
                return "Error: Dangerous command blocked"
            
            result = subprocess.run(
                shlex.split(command),
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            output = result.stdout if result.stdout else result.stderr
            return f"Exit code: {result.returncode}\n{output}"
        except subprocess.TimeoutExpired:
            return f"Error: Command timed out after {timeout}s"
        except Exception as e:
            return f"Error executing command: {str(e)}"
    
    def check_process(self, process_name: str) -> str:
        """Check if process is running"""
        try:
            if os.name == 'nt':  # Windows
                cmd = f'tasklist /FI "IMAGENAME eq {process_name}"'
            else:  # Unix/Linux
                cmd = f'pgrep -f {process_name}'
            
            result = subprocess.run(
                shlex.split(cmd),
                capture_output=True,
                text=True
            )
            
            running = result.returncode == 0
            return f"Process '{process_name}' is {'running' if running else 'not running'}"
        except Exception as e:
            return f"Error checking process: {str(e)}"
```

---

## 🎨 Tool Design Best Practices

### 1. Clear Function Signatures

```python
def good_tool(self, filepath: str, encoding: str = "utf-8") -> str:
    """
    Read file with specified encoding
    
    Args:
        filepath: Path to file to read
        encoding: File encoding (default: utf-8)
        
    Returns:
        File contents as string
    """
    pass

# Bad: unclear parameters
def bad_tool(self, f, e="utf-8"):
    pass
```

### 2. Comprehensive Error Handling

```python
def robust_tool(self, data: str) -> str:
    """Tool with proper error handling"""
    try:
        # Validate input
        if not data:
            return "Error: Empty input"
        
        # Process data
        result = process(data)
        
        # Validate output
        if not result:
            return "Warning: No results"
        
        return result
        
    except ValueError as e:
        return f"Validation error: {str(e)}"
    except IOError as e:
        return f"I/O error: {str(e)}"
    except Exception as e:
        self.log(f"Unexpected error: {str(e)}")
        return f"Error: {str(e)}"
```

### 3. Informative Return Values

```python
def informative_tool(self, action: str) -> str:
    """Return detailed results"""
    result = perform_action(action)
    
    # Good: detailed response
    return f"""
Action: {action}
Status: Success
Duration: 1.2s
Result: {result}
"""
    
    # Bad: minimal response
    # return "OK"
```

### 4. Security Considerations

```python
def secure_tool(self, user_input: str) -> str:
    """Tool with security checks"""
    # Validate input
    if not self.validate_input(user_input):
        return "Error: Invalid input"
    
    # Sanitize paths
    safe_path = os.path.normpath(user_input)
    if not safe_path.startswith(self.allowed_dir):
        return "Error: Access denied"
    
    # Limit resource usage
    if len(user_input) > self.max_input_size:
        return "Error: Input too large"
    
    # Process safely
    return self.process(safe_path)
```

---

## 📊 Tool Configuration

### Adding Configuration Options

```python
class ConfigurablePlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "configurable_tool"
        self.name = "Configurable Tool"
        
        # Define configuration
        self.config = {
            "api_key": {
                "type": "text",
                "label": "API Key",
                "value": "",
                "secret": True,
            },
            "timeout": {
                "type": "int",
                "label": "Timeout (seconds)",
                "value": 30,
                "min": 1,
                "max": 300,
            },
            "enabled_features": {
                "type": "list",
                "label": "Enabled Features",
                "value": ["feature1", "feature2"],
            },
        }
    
    def setup(self):
        # Use configuration
        api_key = self.get_config("api_key")
        timeout = self.get_config("timeout")
        
        self.register_tool("api_call", self.api_call)
    
    def api_call(self, endpoint: str) -> str:
        """Make API call with configured settings"""
        api_key = self.get_config("api_key")
        timeout = self.get_config("timeout")
        
        # Use configuration in tool
        return self.make_request(endpoint, api_key, timeout)
```

---

## 🧪 Testing Tools

### Unit Testing

```python
import unittest
from my_tools import MyToolsPlugin

class TestMyTools(unittest.TestCase):
    def setUp(self):
        self.plugin = MyToolsPlugin()
        self.plugin.setup()
    
    def test_calculate(self):
        result = self.plugin.calculate("2 + 2")
        self.assertEqual(result, 4.0)
    
    def test_format_text(self):
        result = self.plugin.format_text("hello", "upper")
        self.assertEqual(result, "HELLO")
    
    def test_error_handling(self):
        result = self.plugin.calculate("invalid")
        self.assertTrue(result.startswith("Error:"))

if __name__ == '__main__':
    unittest.main()
```

### Integration Testing

```python
def test_tool_integration():
    """Test tool in PyGPT context"""
    # Create plugin
    plugin = MyToolsPlugin()
    plugin.setup()
    
    # Simulate AI calling tool
    result = plugin.calculate("10 * 5")
    assert result == 50.0
    
    # Test with context
    ctx = create_test_context()
    result = plugin.handle(ctx)
    assert result is not None
```

---

## 📦 Tool Distribution

### Package Structure

```
my_tools_plugin/
├── __init__.py          # Main plugin code
├── config.json          # Default configuration
├── README.md            # Documentation
├── requirements.txt     # Dependencies
├── tests/               # Test files
│   └── test_tools.py
└── examples/            # Usage examples
    └── example.py
```

### README Template

```markdown
# My Tools Plugin

Custom tools for PyGPT.

## Features
- Feature 1
- Feature 2

## Installation
1. Copy to `~/.pygpt/plugins/my_tools/`
2. Install dependencies: `pip install -r requirements.txt`
3. Restart PyGPT
4. Enable in Settings → Plugins

## Configuration
- `api_key`: Your API key
- `timeout`: Request timeout

## Usage
Ask AI to use the tools:
- "Calculate 2 + 2"
- "Format 'hello' as uppercase"

## License
MIT
```

---

## 🔍 Debugging Tools

### Enable Debug Logging

```python
class DebugPlugin(PluginBase):
    def my_tool(self, arg: str) -> str:
        # Log input
        self.debug(f"Tool called with: {arg}")
        
        try:
            result = self.process(arg)
            
            # Log success
            self.debug(f"Tool result: {result}")
            return result
            
        except Exception as e:
            # Log error
            self.log(f"Tool error: {str(e)}")
            return f"Error: {str(e)}"
```

### Check Debug Log

```bash
# View debug log
tail -f ~/.pygpt/debug.log

# Search for tool calls
grep "my_tool" ~/.pygpt/debug.log
```

---

## 🆘 Troubleshooting

### Tool Not Appearing

**Check:**
1. Plugin enabled in Settings?
2. Tool registered in `setup()`?
3. Plugin loaded without errors?
4. Check debug log for errors

### Tool Not Being Called

**Check:**
1. Tool name clear and descriptive?
2. Function signature correct?
3. Docstring explains purpose?
4. AI understands when to use it?

### Tool Errors

**Check:**
1. Error handling implemented?
2. Input validation working?
3. Dependencies installed?
4. Permissions correct?

---

## 📚 Examples

### Complete Example: Weather Tool

```python
import requests
from pygpt_net.plugin.base import PluginBase

class WeatherPlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "weather_tool"
        self.name = "Weather Tool"
        
        self.config = {
            "api_key": {
                "type": "text",
                "label": "OpenWeather API Key",
                "value": "",
                "secret": True,
            },
        }
    
    def setup(self):
        self.register_tool("get_weather", self.get_weather)
        self.register_tool("get_forecast", self.get_forecast)
    
    def get_weather(self, city: str) -> str:
        """
        Get current weather for a city
        
        Args:
            city: City name
            
        Returns:
            Weather description
        """
        api_key = self.get_config("api_key")
        if not api_key:
            return "Error: API key not configured"
        
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather"
            params = {
                "q": city,
                "appid": api_key,
                "units": "metric"
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            
            return f"""
Weather in {city}:
Temperature: {temp}°C
Conditions: {desc}
Humidity: {humidity}%
"""
        except Exception as e:
            return f"Error getting weather: {str(e)}"
    
    def get_forecast(self, city: str, days: int = 3) -> str:
        """
        Get weather forecast
        
        Args:
            city: City name
            days: Number of days (1-5)
            
        Returns:
            Forecast description
        """
        # Implementation similar to get_weather
        pass
```

---

## 🚀 Advanced Topics

### Async Tools

```python
import asyncio

class AsyncPlugin(PluginBase):
    def setup(self):
        self.register_tool("async_fetch", self.async_fetch_wrapper)
    
    async def async_fetch(self, url: str) -> str:
        """Async HTTP request"""
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    
    def async_fetch_wrapper(self, url: str) -> str:
        """Wrapper for async function"""
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(self.async_fetch(url))
```

### Streaming Results

```python
class StreamingPlugin(PluginBase):
    def stream_data(self, source: str) -> str:
        """Stream large data"""
        results = []
        for chunk in self.process_stream(source):
            results.append(chunk)
            # Update UI progressively
            self.update_ui(chunk)
        
        return "\n".join(results)
```

---

## 📖 Resources

- [Plugin Development Guide](./plugin-development.md)
- [Architecture Overview](./architecture.md)
- [API Reference](./api-reference.md)
- [Example Tools](../../examples/tools/)

---

**Next:** [LLM Integration Guide](./llm-integration.md) →
