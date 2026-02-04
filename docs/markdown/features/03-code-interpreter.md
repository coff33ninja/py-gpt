# Code Interpreter

Execute Python code directly within PyGPT.

## 💻 Overview

Code Interpreter allows AI models to write and execute Python code in real-time, enabling data analysis, file processing, calculations, visualizations, and more.

**Key Features:**
- Real-time Python execution
- IPython kernel support
- Docker isolation (optional)
- Image/plot output
- File I/O operations
- Library auto-installation
- Code persistence

**Plugin:** Code Interpreter (built-in)

## 🚀 Getting Started

### Enable Code Interpreter

1. **Open Plugins**
   ```
   Menu → Plugins → Code Interpreter
   ```

2. **Enable Plugin**
   - Toggle switch to ON
   - Configure settings (optional)

3. **Start Using**
   - Ask AI to write code
   - Code executes automatically
   - Results appear in chat

### Your First Code Execution

```
You: Calculate the sum of numbers from 1 to 100

AI: I'll calculate that for you:

```python
result = sum(range(1, 101))
print(f"The sum is: {result}")
```

[Code executes]

Output: The sum is: 5050
```

## 🎯 Use Cases

### Data Analysis
```python
import pandas as pd

# Load and analyze CSV
df = pd.read_csv('data.csv')
print(df.describe())
print(df.groupby('category').mean())
```

### Mathematical Calculations
```python
import numpy as np

# Complex calculations
matrix = np.array([[1, 2], [3, 4]])
eigenvalues = np.linalg.eigvals(matrix)
print(f"Eigenvalues: {eigenvalues}")
```

### Data Visualization
```python
import matplotlib.pyplot as plt

# Create plot
data = [1, 4, 9, 16, 25]
plt.plot(data)
plt.title('Square Numbers')
plt.savefig('plot.png')
plt.show()
```

### File Processing
```python
# Read and process files
with open('input.txt', 'r') as f:
    content = f.read()
    
# Process content
processed = content.upper()

# Write output
with open('output.txt', 'w') as f:
    f.write(processed)
```

### Web Scraping
```python
import requests
from bs4 import BeautifulSoup

# Fetch webpage
response = requests.get('https://example.com')
soup = BeautifulSoup(response.text, 'html.parser')

# Extract data
titles = soup.find_all('h2')
for title in titles:
    print(title.text)
```

## ⚙️ Configuration

### Settings Location
`Plugins → Code Interpreter → Settings`

### Execution Environment

**Local (IPython)**
- Runs on your machine
- Direct system access
- Fast execution
- No isolation

**Docker Container**
- Isolated environment
- Safe execution
- Slower startup
- Better security

**Configuration:**
```
Execution Mode: Local / Docker
Python Path: /usr/bin/python3
Working Directory: ~/pygpt/code
```

### IPython Kernel

**Kernel Settings:**
```
Auto-start: Yes/No
Restart on error: Yes/No
Timeout: 30 seconds
Max output: 10000 chars
```

**Kernel Management:**
- Auto-restart on failure
- Manual restart option
- Clear output option
- Kernel status indicator

### Docker Configuration

**Docker Settings:**
```
Image: python:3.11
Container Name: pygpt-code
Memory Limit: 512MB
CPU Limit: 1.0
```

**Volume Mounts:**
```
Host: ~/pygpt/data
Container: /data
Read-only: No
```

### Library Management

**Auto-install:**
- Detects missing libraries
- Installs automatically
- Uses pip
- Caches installations

**Pre-installed Libraries:**
```
numpy
pandas
matplotlib
scikit-learn
requests
beautifulsoup4
pillow
```

**Custom Libraries:**
```
Settings → Additional Libraries
Add: tensorflow, torch, etc.
```

## 🔧 Features

### Code Execution

**Automatic Execution:**
- AI writes code
- Code runs automatically
- Results shown in chat
- Errors displayed

**Manual Execution:**
- Click "Run" button on code block
- Execute specific code
- Test modifications
- Debug issues

**Execution Flow:**
```
1. AI generates code
2. Code sent to kernel
3. Kernel executes
4. Output captured
5. Results displayed
```

### Output Handling

**Text Output:**
```python
print("Hello, World!")
# Output: Hello, World!
```

**Data Output:**
```python
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3]})
print(df)
# Output: DataFrame displayed
```

**Image Output:**
```python
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.savefig('plot.png')
# Output: Image displayed in chat
```

**Error Output:**
```python
1 / 0
# Output: ZeroDivisionError with traceback
```

### File Operations

**Read Files:**
```python
with open('data.txt', 'r') as f:
    content = f.read()
```

**Write Files:**
```python
with open('output.txt', 'w') as f:
    f.write('Hello, World!')
```

**File Paths:**
- Relative to working directory
- Absolute paths supported
- Access to data folder
- Restricted by permissions

### Working Directory

**Default Location:**
```
~/pygpt/code/
```

**Access:**
- Read/write files
- Create subdirectories
- Persistent storage
- Shared with AI

**Management:**
```
Tools → Code Interpreter → Open Working Directory
```

### Code Persistence

**Session Persistence:**
- Variables persist between executions
- Import statements remembered
- State maintained
- Clear with kernel restart

**Example:**
```python
# First execution
x = 10

# Later execution
print(x)  # Works! x is still 10
```

### Image Generation

**Matplotlib Plots:**
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title('Square Numbers')
plt.xlabel('X')
plt.ylabel('Y²')
plt.savefig('plot.png')
plt.show()
```

**PIL/Pillow Images:**
```python
from PIL import Image, ImageDraw

img = Image.new('RGB', (200, 200), 'white')
draw = ImageDraw.Draw(img)
draw.rectangle([50, 50, 150, 150], fill='blue')
img.save('rectangle.png')
```

**Display in Chat:**
- Images automatically displayed
- Click to view full size
- Save to disk
- Use in follow-up

## 🎨 Advanced Features

### CodeAct Agent

Specialized agent for code execution.

**Features:**
- Multi-step code execution
- Automatic error recovery
- Library installation
- File management
- Plot generation

**Enable:**
```
Mode: Agents (LlamaIndex)
Agent Type: CodeAct
```

**Use Cases:**
- Complex data analysis
- Multi-file projects
- Iterative development
- Automated workflows

### Tool Integration

**Available Tools:**
- File I/O
- Web requests
- Database access
- System commands
- Custom tools

**Tool Calls:**
```python
# AI can call tools from code
result = call_tool('web_search', query='Python tutorials')
print(result)
```

### Error Handling

**Automatic Retry:**
- Detects errors
- Attempts fix
- Retries execution
- Reports if fails

**Error Recovery:**
```python
try:
    risky_operation()
except Exception as e:
    print(f"Error: {e}")
    # AI suggests fix
```

### Debugging

**Debug Mode:**
```
Settings → Debug Mode: Enabled
```

**Features:**
- Verbose output
- Execution logs
- Variable inspection
- Step-by-step execution

**Debug Output:**
```
[DEBUG] Executing code...
[DEBUG] Importing libraries...
[DEBUG] Running main code...
[DEBUG] Output: ...
[DEBUG] Execution complete
```

## 🐛 Troubleshooting

### Code Not Executing
**Problem:** Code doesn't run

**Solutions:**
- Check plugin is enabled
- Verify kernel is running
- Restart kernel
- Check Python installation
- Review error messages

### Kernel Not Starting
**Problem:** IPython kernel fails

**Solutions:**
- Check Python installation
- Verify ipykernel installed
- Check port availability
- Review kernel logs
- Restart PyGPT

### Docker Issues
**Problem:** Docker container fails

**Solutions:**
- Verify Docker installed
- Check Docker running
- Pull Python image
- Check permissions
- Review Docker logs

### Library Not Found
**Problem:** Import fails

**Solutions:**
- Enable auto-install
- Install manually: `pip install library`
- Check library name
- Verify Python version compatibility

### Permission Errors
**Problem:** Can't access files

**Solutions:**
- Check file permissions
- Verify working directory
- Use absolute paths
- Check Docker mounts

### Slow Execution
**Problem:** Code runs slowly

**Solutions:**
- Optimize code
- Use local execution
- Increase timeout
- Check system resources

## 💡 Best Practices

### Code Quality

```python
✅ # Clear, commented code
def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    return sum(numbers) / len(numbers)

❌ # Unclear, no comments
def f(x):
    return sum(x)/len(x)
```

### Error Handling

```python
✅ # Proper error handling
try:
    result = risky_operation()
except ValueError as e:
    print(f"Invalid value: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

❌ # No error handling
result = risky_operation()  # May crash
```

### File Management

```python
✅ # Use context managers
with open('file.txt', 'r') as f:
    content = f.read()

❌ # Manual file handling
f = open('file.txt', 'r')
content = f.read()
# Forgot to close!
```

### Resource Cleanup

```python
✅ # Clean up resources
import matplotlib.pyplot as plt
plt.plot(data)
plt.savefig('plot.png')
plt.close()  # Free memory

❌ # No cleanup
plt.plot(data)
plt.savefig('plot.png')
# Memory leak!
```

## 🔗 Related Features

- [Agents & Automation](./06-agents-automation.md) - CodeAct agent
- [File Operations](../guides/03-working-with-files.md) - File handling
- [Custom Commands](./08-custom-commands.md) - Custom tools

## 📚 Additional Resources

- [IPython Documentation](https://ipython.readthedocs.io/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [Docker Documentation](https://docs.docker.com/)

## ⚠️ Security Considerations

### Code Execution Risks

**Dangers:**
- System access
- File modification
- Network requests
- Resource consumption

**Mitigation:**
- Use Docker isolation
- Limit permissions
- Monitor execution
- Review code before running

### Safe Practices

```
✅ Use Docker for untrusted code
✅ Review AI-generated code
✅ Limit file access
✅ Monitor resource usage
❌ Execute without review
❌ Grant full system access
```

## 🆘 Need Help?

- Check [Agents Guide](./06-agents-automation.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Web Search](./04-web-search.md) →
