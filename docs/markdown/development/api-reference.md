# API Reference

Complete API reference for PyGPT development.

## 🏗️ Core APIs

### Window (Main Application)

```python
from pygpt_net.app import Window

# Main application window
window = Window()

# Access core components
window.core.config      # Configuration manager
window.core.models      # Model manager
window.core.ctx         # Context manager
window.core.llm         # LLM provider manager
window.core.plugins     # Plugin manager
window.core.db          # Database manager
```

### Configuration API

```python
# Get configuration value
value = window.core.config.get(key, default=None)

# Set configuration value
window.core.config.set(key, value)

# Save configuration
window.core.config.save()

# Load configuration
window.core.config.load()

# Reset to defaults
window.core.config.reset()

# Check if key exists
exists = window.core.config.has(key)

# Get all config
all_config = window.core.config.all()
```

### Model API

```python
# Get current model
model = window.core.models.get_current()

# Get model by ID
model = window.core.models.get(model_id)

# Get all models
models = window.core.models.get_all()

# Get models by mode
chat_models = window.core.models.get_by_mode("chat")

# Get models by provider
openai_models = window.core.models.get_by_provider("openai")

# Set current model
window.core.models.set_current(model_id)

# Model properties
model.id            # Model identifier
model.name          # Display name
model.mode          # Supported modes
model.llm           # Provider ID
model.ctx           # Context window size
model.tokens        # Max tokens
model.vision        # Vision support
model.audio         # Audio support
```

---

## 💬 Context API

### Context Management

```python
# Get current context
ctx = window.core.ctx.get_current()

# Create new context
ctx = window.core.ctx.new()

# Get context by ID
ctx = window.core.ctx.get(ctx_id)

# Get all contexts
contexts = window.core.ctx.get_all()

# Delete context
window.core.ctx.delete(ctx_id)

# Clear context
window.core.ctx.clear(ctx_id)

# Context properties
ctx.id              # Context ID
ctx.name            # Context name
ctx.messages        # Message list
ctx.model           # Associated model
ctx.mode            # Chat mode
ctx.created_at      # Creation timestamp
ctx.updated_at      # Last update
```

### Message API

```python
# Add message to context
msg = window.core.ctx.add_message(
    ctx_id=ctx.id,
    role="user",  # or "assistant", "system"
    content="Hello",
    attachments=[]
)

# Get messages from context
messages = window.core.ctx.get_messages(ctx_id)

# Delete message
window.core.ctx.delete_message(msg_id)

# Update message
window.core.ctx.update_message(msg_id, content="Updated")

# Message properties
msg.id              # Message ID
msg.role            # user/assistant/system
msg.content         # Message text
msg.attachments     # File attachments
msg.tokens          # Token count
msg.created_at      # Timestamp
```

---

## 🤖 LLM API

### Provider Management

```python
# Get LLM manager
llm = window.core.llm

# Get provider by ID
provider = llm.get_provider("openai")

# Get all providers
providers = llm.get_providers()

# Create LLM instance
llm_instance = provider.llama(model, **kwargs)

# Get available models
models = provider.get_models()

# Setup environment
provider.setup_env(api_key="your_key")
```

### Completion API

```python
# Generate completion
response = llm_instance.complete(
    prompt="Hello, world!",
    temperature=0.7,
    max_tokens=2048
)

# Stream completion
for chunk in llm_instance.stream_complete(prompt):
    print(chunk.text)

# Chat completion
from llama_index.core.llms import ChatMessage

messages = [
    ChatMessage(role="system", content="You are helpful"),
    ChatMessage(role="user", content="Hello"),
]

response = llm_instance.chat(messages)
```

---

## 🔌 Plugin API

### Plugin Base Class

```python
from pygpt_net.plugin.base import PluginBase

class MyPlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_plugin"
        self.name = "My Plugin"
        self.description = "Plugin description"
        self.config = {}  # Configuration schema
    
    def setup(self):
        """Initialize plugin"""
        pass
    
    def handle(self, ctx, **kwargs):
        """Handle plugin execution"""
        pass
    
    def on_enable(self):
        """Called when plugin is enabled"""
        pass
    
    def on_disable(self):
        """Called when plugin is disabled"""
        pass
```

### Plugin Methods

```python
# Configuration
self.get_config(key, default=None)
self.set_config(key, value)
self.has_config(key)

# Logging
self.log(message)
self.debug(message)
self.error(message)

# Context access
self.get_context()
self.get_current_model()

# Tool registration
self.register_tool(name, function)
self.unregister_tool(name)

# Event handling
self.on_message(ctx, message)
self.on_response(ctx, response)
self.on_error(ctx, error)
```

---

## 📁 File API

### File Operations

```python
# File manager
files = window.core.filesystem

# Read file
content = files.read(filepath)

# Write file
files.write(filepath, content)

# Append to file
files.append(filepath, content)

# Delete file
files.delete(filepath)

# Check if exists
exists = files.exists(filepath)

# List directory
items = files.list_dir(dirpath)

# Create directory
files.mkdir(dirpath)

# Get file info
info = files.get_info(filepath)
```

### Attachment API

```python
# Add attachment to message
attachment = window.core.attachments.add(
    msg_id=msg.id,
    filepath="/path/to/file",
    name="file.txt",
    type="text/plain"
)

# Get attachments
attachments = window.core.attachments.get_by_message(msg_id)

# Delete attachment
window.core.attachments.delete(attachment_id)

# Attachment properties
attachment.id           # Attachment ID
attachment.msg_id       # Message ID
attachment.filepath     # File path
attachment.name         # File name
attachment.type         # MIME type
attachment.size         # File size
```

---

## 🗄️ Database API

### Database Manager

```python
# Database manager
db = window.core.db

# Execute query
result = db.execute(sql, params)

# Fetch one
row = db.fetch_one(sql, params)

# Fetch all
rows = db.fetch_all(sql, params)

# Insert
db.insert(table, data)

# Update
db.update(table, data, where)

# Delete
db.delete(table, where)

# Begin transaction
db.begin()

# Commit transaction
db.commit()

# Rollback transaction
db.rollback()
```

### ORM Models

```python
from sqlalchemy import Column, Integer, String, Text
from pygpt_net.core.db import Base

class MyModel(Base):
    __tablename__ = 'my_table'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    content = Column(Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
        }
```

---

## 🎨 UI API

### Dialog API

```python
# Show message dialog
window.ui.dialogs.alert(
    title="Alert",
    message="This is an alert"
)

# Show confirmation dialog
result = window.ui.dialogs.confirm(
    title="Confirm",
    message="Are you sure?"
)

# Show input dialog
text = window.ui.dialogs.input(
    title="Input",
    label="Enter text:",
    default="default value"
)

# Show file dialog
filepath = window.ui.dialogs.open_file(
    title="Open File",
    filters="Text files (*.txt)"
)

# Show save dialog
filepath = window.ui.dialogs.save_file(
    title="Save File",
    filters="Text files (*.txt)"
)
```

### Status Bar API

```python
# Show status message
window.ui.status.show("Processing...")

# Show temporary message
window.ui.status.show_temp("Done!", duration=3000)

# Clear status
window.ui.status.clear()

# Show progress
window.ui.status.progress(50, 100)  # 50%

# Hide progress
window.ui.status.hide_progress()
```

### Chat Output API

```python
# Append to chat
window.ui.chat.append(
    role="assistant",
    content="Hello!",
    ctx_id=ctx.id
)

# Clear chat
window.ui.chat.clear()

# Scroll to bottom
window.ui.chat.scroll_to_bottom()

# Update message
window.ui.chat.update_message(msg_id, content)

# Delete message
window.ui.chat.delete_message(msg_id)
```

---

## 🔧 Utility APIs

### Token Counter

```python
# Count tokens
tokens = window.core.tokens.count(text, model_id)

# Count tokens in messages
tokens = window.core.tokens.count_messages(messages, model_id)

# Get token limit
limit = window.core.tokens.get_limit(model_id)

# Check if within limit
within_limit = window.core.tokens.check_limit(text, model_id)
```

### Command Parser

```python
# Parse command from text
command = window.core.command.parse(text)

# Execute command
result = window.core.command.execute(command, ctx)

# Register custom command
window.core.command.register(
    name="mycommand",
    handler=my_handler_function,
    description="My custom command"
)

# Command properties
command.name        # Command name
command.args        # Arguments
command.kwargs      # Keyword arguments
```

### Audio API

```python
# Audio input (speech-to-text)
text = window.core.audio.transcribe(audio_file)

# Audio output (text-to-speech)
audio_file = window.core.audio.synthesize(text, voice="alloy")

# Play audio
window.core.audio.play(audio_file)

# Stop audio
window.core.audio.stop()

# Get available voices
voices = window.core.audio.get_voices()
```

### Vision API

```python
# Analyze image
result = window.core.vision.analyze(
    image_path="/path/to/image.jpg",
    prompt="What's in this image?"
)

# Generate image
image_path = window.core.vision.generate(
    prompt="A beautiful sunset",
    size="1024x1024"
)

# Edit image
edited_path = window.core.vision.edit(
    image_path="/path/to/image.jpg",
    mask_path="/path/to/mask.png",
    prompt="Add a rainbow"
)
```

---

## 🌐 Web API

### Web Search

```python
# Search web
results = window.core.web.search(
    query="Python programming",
    num_results=10
)

# Get page content
content = window.core.web.get_page(url)

# Extract text from HTML
text = window.core.web.extract_text(html)

# Search result properties
result.title        # Page title
result.url          # Page URL
result.snippet      # Description
result.content      # Full content (if fetched)
```

### HTTP Client

```python
# GET request
response = window.core.web.get(
    url="https://api.example.com/data",
    headers={"Authorization": "Bearer token"}
)

# POST request
response = window.core.web.post(
    url="https://api.example.com/data",
    json={"key": "value"},
    headers={"Content-Type": "application/json"}
)

# Response properties
response.status_code    # HTTP status
response.text           # Response text
response.json()         # Parse JSON
response.headers        # Response headers
```

---

## 📊 Vector Store API

### Indexing

```python
# Create index
index = window.core.idx.create(
    name="my_index",
    documents=documents
)

# Add documents
window.core.idx.add_documents(
    index_name="my_index",
    documents=documents
)

# Delete index
window.core.idx.delete(index_name="my_index")

# List indexes
indexes = window.core.idx.list()
```

### Querying

```python
# Query index
results = window.core.idx.query(
    index_name="my_index",
    query="search query",
    top_k=5
)

# Query result properties
result.text         # Document text
result.score        # Relevance score
result.metadata     # Document metadata
result.id           # Document ID
```

---

## 🎯 Event System

### Event Dispatcher

```python
# Register event listener
window.core.events.on(
    event="message.sent",
    handler=my_handler
)

# Emit event
window.core.events.emit(
    event="message.sent",
    data={"message": msg}
)

# Remove listener
window.core.events.off(
    event="message.sent",
    handler=my_handler
)

# Available events
"message.sent"          # Message sent
"message.received"      # Response received
"context.created"       # Context created
"context.deleted"       # Context deleted
"model.changed"         # Model changed
"plugin.enabled"        # Plugin enabled
"plugin.disabled"       # Plugin disabled
```

---

## 🔐 Security API

### API Key Management

```python
# Store API key
window.core.security.store_key(
    provider="openai",
    key="sk-..."
)

# Retrieve API key
key = window.core.security.get_key(provider="openai")

# Delete API key
window.core.security.delete_key(provider="openai")

# Encrypt data
encrypted = window.core.security.encrypt(data)

# Decrypt data
decrypted = window.core.security.decrypt(encrypted)
```

---

## 📝 Data Models

### ModelItem

```python
from pygpt_net.item.model import ModelItem

model = ModelItem()
model.id = "gpt-4"
model.name = "GPT-4"
model.mode = ["chat", "completion"]
model.llm = "openai"
model.ctx = 8192
model.tokens = 8192
model.vision = True
model.audio = False
```

### ContextItem

```python
from pygpt_net.item.context import ContextItem

ctx = ContextItem()
ctx.id = 1
ctx.name = "My Conversation"
ctx.messages = []
ctx.model = "gpt-4"
ctx.mode = "chat"
```

### MessageItem

```python
from pygpt_net.item.message import MessageItem

msg = MessageItem()
msg.id = 1
msg.ctx_id = 1
msg.role = "user"
msg.content = "Hello"
msg.attachments = []
msg.tokens = 10
```

---

## 🧪 Testing Utilities

### Mock Objects

```python
from tests.mocks import MockWindow, MockConfig

# Create mock window
window = MockWindow()

# Create mock config
config = MockConfig()
config.set("key", "value")

# Create mock context
ctx = create_mock_context()
```

### Test Helpers

```python
from tests.helpers import (
    create_test_model,
    create_test_context,
    create_test_message,
)

# Create test objects
model = create_test_model()
ctx = create_test_context()
msg = create_test_message()
```

---

## 📚 Code Examples

### Complete Plugin Example

```python
from pygpt_net.plugin.base import PluginBase

class WeatherPlugin(PluginBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "weather"
        self.name = "Weather Plugin"
        
        self.config = {
            "api_key": {
                "type": "text",
                "label": "API Key",
                "secret": True,
            }
        }
    
    def setup(self):
        self.register_tool("get_weather", self.get_weather)
    
    def get_weather(self, city: str) -> str:
        """Get weather for city"""
        api_key = self.get_config("api_key")
        # Implementation
        return f"Weather in {city}: Sunny"
    
    def handle(self, ctx, **kwargs):
        """Handle plugin execution"""
        if ctx.command == "/weather":
            city = ctx.args[0] if ctx.args else "London"
            return self.get_weather(city)
```

### Complete Provider Example

```python
from pygpt_net.provider.llms.base import BaseLLM
from llama_index.core.llms import CustomLLM

class MyProvider(BaseLLM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_provider"
        self.name = "My Provider"
    
    def llama(self, model, **kwargs):
        return CustomLLM(
            model=model.id,
            api_key=self.get_api_key(),
        )
    
    def get_models(self):
        # Return list of ModelItem objects
        pass
```

---

## 🔗 Related Documentation

- [Architecture Overview](./architecture.md)
- [Plugin Development](./plugin-development.md)
- [Custom Tools](./custom-tools.md)
- [LLM Integration](./llm-integration.md)

---

## 📖 External Resources

- [LlamaIndex API](https://docs.llamaindex.ai/)
- [PySide6 Documentation](https://doc.qt.io/qtforpython/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

**Next:** [Contributing Guide](./contributing.md) →
