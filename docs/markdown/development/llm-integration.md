# LLM Integration Guide

Learn how to integrate new AI providers and language models into PyGPT.

## 🤖 Provider Architecture

### Overview

PyGPT supports multiple AI providers through a unified interface:

```
User Request
    ↓
PyGPT Core
    ↓
Provider Wrapper (OpenAI, Google, Anthropic, etc.)
    ↓
LlamaIndex Integration (optional)
    ↓
External API
    ↓
Response Processing
    ↓
Display to User
```

### Provider Types

1. **Cloud Providers**: OpenAI, Google, Anthropic, etc.
2. **Local Providers**: Ollama, LM Studio, etc.
3. **Custom Providers**: Your own API or model

---

## 📁 Provider Structure

### File Organization

```
src/pygpt_net/provider/
├── llms/                    # LLM provider implementations
│   ├── base.py             # Base provider class
│   ├── openai.py           # OpenAI implementation
│   ├── google.py           # Google Gemini
│   ├── anthropic.py        # Anthropic Claude
│   ├── ollama.py           # Ollama local
│   └── my_provider.py      # Your custom provider
│
└── api/                     # API-specific handlers
    ├── openai/
    ├── google/
    └── my_provider/
```

### Provider Class Structure

```python
from pygpt_net.provider.llms.base import BaseLLM

class MyProvider(BaseLLM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_provider"
        self.name = "My AI Provider"
    
    def llama(self, model: ModelItem, **kwargs):
        """Return LlamaIndex-compatible LLM"""
        pass
    
    def get_models(self) -> list:
        """Return list of available models"""
        pass
    
    def setup_env(self, api_key: str):
        """Setup environment variables"""
        pass
```

---

## 🔧 Creating a Custom Provider

### Step 1: Create Provider File

Create `src/pygpt_net/provider/llms/my_provider.py`:

```python
from llama_index.core.llms import LLM
from pygpt_net.provider.llms.base import BaseLLM
from pygpt_net.item.model import ModelItem

class MyProviderLLM(BaseLLM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_provider"
        self.name = "My AI Provider"
        self.type = ["chat", "completion"]  # Supported modes
    
    def llama(self, model: ModelItem, **kwargs) -> LLM:
        """
        Create LlamaIndex LLM instance
        
        Args:
            model: Model configuration
            **kwargs: Additional parameters
            
        Returns:
            LlamaIndex LLM instance
        """
        from my_provider_sdk import MyProviderLLM as SDK_LLM
        
        # Get API key
        api_key = self.get_api_key()
        
        # Create LLM instance
        llm = SDK_LLM(
            model=model.id,
            api_key=api_key,
            temperature=kwargs.get('temperature', 0.7),
            max_tokens=kwargs.get('max_tokens', 2048),
        )
        
        return llm
    
    def get_models(self) -> list:
        """
        Get list of available models
        
        Returns:
            List of ModelItem objects
        """
        models = []
        
        # Define available models
        model_configs = [
            {
                "id": "my-model-v1",
                "name": "My Model v1",
                "ctx": 4096,
                "tokens": 4096,
            },
            {
                "id": "my-model-v2",
                "name": "My Model v2",
                "ctx": 8192,
                "tokens": 8192,
            },
        ]
        
        for config in model_configs:
            model = ModelItem()
            model.id = config["id"]
            model.name = config["name"]
            model.mode = ["chat", "completion"]
            model.llm = self.id
            model.ctx = config["ctx"]
            model.tokens = config["tokens"]
            models.append(model)
        
        return models
    
    def setup_env(self, api_key: str = None):
        """
        Setup environment variables
        
        Args:
            api_key: API key to set
        """
        import os
        if api_key:
            os.environ["MY_PROVIDER_API_KEY"] = api_key
    
    def get_api_key(self) -> str:
        """Get API key from config or environment"""
        import os
        
        # Try config first
        api_key = self.config.get("api_key")
        if api_key:
            return api_key
        
        # Try environment variable
        return os.getenv("MY_PROVIDER_API_KEY", "")
```

### Step 2: Register Provider

Add to `src/pygpt_net/core/llm.py`:

```python
from pygpt_net.provider.llms.my_provider import MyProviderLLM

class LLM:
    def __init__(self, window=None):
        self.window = window
        self.providers = {
            "openai": OpenAILLM(window),
            "google": GoogleLLM(window),
            "anthropic": AnthropicLLM(window),
            "my_provider": MyProviderLLM(window),  # Add your provider
        }
```

### Step 3: Add Model Definitions

Create `data/models/my_provider.json`:

```json
{
  "my-model-v1": {
    "id": "my-model-v1",
    "name": "My Model v1",
    "mode": ["chat", "completion"],
    "llm": "my_provider",
    "ctx": 4096,
    "tokens": 4096,
    "default": true
  },
  "my-model-v2": {
    "id": "my-model-v2",
    "name": "My Model v2",
    "mode": ["chat", "completion"],
    "llm": "my_provider",
    "ctx": 8192,
    "tokens": 8192,
    "vision": true
  }
}
```

### Step 4: Add UI Configuration

Add provider to settings UI in `src/pygpt_net/ui/dialog/settings.py`:

```python
def setup_providers(self):
    """Setup provider configuration"""
    providers = {
        "openai": "OpenAI",
        "google": "Google Gemini",
        "anthropic": "Anthropic Claude",
        "my_provider": "My AI Provider",  # Add here
    }
    
    # Add API key field
    self.add_field(
        "my_provider.api_key",
        "text",
        "My Provider API Key",
        secret=True
    )
```

---

## 🎨 Advanced Provider Features

### Vision Support

```python
class VisionProvider(BaseLLM):
    def llama(self, model: ModelItem, **kwargs) -> LLM:
        """Create vision-capable LLM"""
        from my_provider_sdk import VisionLLM
        
        llm = VisionLLM(
            model=model.id,
            api_key=self.get_api_key(),
            vision_enabled=True,
        )
        
        return llm
    
    def process_image(self, image_path: str, prompt: str) -> str:
        """Process image with vision model"""
        import base64
        
        # Read and encode image
        with open(image_path, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode()
        
        # Send to API
        response = self.api_call({
            "prompt": prompt,
            "image": image_data,
        })
        
        return response["text"]
```

### Streaming Support

```python
class StreamingProvider(BaseLLM):
    def llama(self, model: ModelItem, **kwargs) -> LLM:
        """Create streaming LLM"""
        from my_provider_sdk import StreamingLLM
        
        llm = StreamingLLM(
            model=model.id,
            api_key=self.get_api_key(),
            stream=True,
            callback=self.stream_callback,
        )
        
        return llm
    
    def stream_callback(self, chunk: str):
        """Handle streaming chunks"""
        # Update UI with chunk
        self.window.update_output(chunk)
```

### Function Calling

```python
class FunctionProvider(BaseLLM):
    def llama(self, model: ModelItem, **kwargs) -> LLM:
        """Create function-calling LLM"""
        from my_provider_sdk import FunctionLLM
        
        # Define available functions
        functions = [
            {
                "name": "get_weather",
                "description": "Get weather for a city",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "City name"
                        }
                    },
                    "required": ["city"]
                }
            }
        ]
        
        llm = FunctionLLM(
            model=model.id,
            api_key=self.get_api_key(),
            functions=functions,
        )
        
        return llm
```

### Embeddings Support

```python
class EmbeddingProvider(BaseLLM):
    def get_embeddings(self, texts: list) -> list:
        """Generate embeddings for texts"""
        from my_provider_sdk import Embeddings
        
        embedder = Embeddings(
            api_key=self.get_api_key(),
            model="my-embedding-model"
        )
        
        embeddings = embedder.embed(texts)
        return embeddings
```

---

## 🔌 LlamaIndex Integration

### Basic Integration

```python
from llama_index.core.llms import CustomLLM, CompletionResponse
from typing import Any

class MyLlamaIndexLLM(CustomLLM):
    """Custom LlamaIndex LLM wrapper"""
    
    model: str
    api_key: str
    temperature: float = 0.7
    
    @property
    def metadata(self) -> dict:
        return {
            "model": self.model,
            "temperature": self.temperature,
        }
    
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        """Generate completion"""
        # Call your API
        response = self.api_call(prompt)
        
        return CompletionResponse(
            text=response["text"],
            additional_kwargs=response.get("metadata", {})
        )
    
    def stream_complete(self, prompt: str, **kwargs: Any):
        """Stream completion"""
        for chunk in self.api_stream(prompt):
            yield CompletionResponse(
                text=chunk["text"],
                delta=chunk["text"]
            )
```

### Chat Integration

```python
from llama_index.core.llms import ChatMessage, ChatResponse

class MyChatLLM(CustomLLM):
    def chat(self, messages: list[ChatMessage], **kwargs) -> ChatResponse:
        """Generate chat response"""
        # Convert messages to API format
        api_messages = [
            {"role": msg.role, "content": msg.content}
            for msg in messages
        ]
        
        # Call API
        response = self.api_chat(api_messages)
        
        return ChatResponse(
            message=ChatMessage(
                role="assistant",
                content=response["text"]
            ),
            additional_kwargs=response.get("metadata", {})
        )
```

---

## 🧪 Testing Your Provider

### Unit Tests

```python
import unittest
from pygpt_net.provider.llms.my_provider import MyProviderLLM
from pygpt_net.item.model import ModelItem

class TestMyProvider(unittest.TestCase):
    def setUp(self):
        self.provider = MyProviderLLM()
        self.model = ModelItem()
        self.model.id = "my-model-v1"
    
    def test_get_models(self):
        """Test model listing"""
        models = self.provider.get_models()
        self.assertGreater(len(models), 0)
        self.assertEqual(models[0].llm, "my_provider")
    
    def test_llama_creation(self):
        """Test LLM instance creation"""
        llm = self.provider.llama(self.model)
        self.assertIsNotNone(llm)
    
    def test_api_key_setup(self):
        """Test API key configuration"""
        test_key = "test_key_123"
        self.provider.setup_env(test_key)
        self.assertEqual(self.provider.get_api_key(), test_key)

if __name__ == '__main__':
    unittest.main()
```

### Integration Tests

```python
def test_provider_integration():
    """Test provider in PyGPT"""
    from pygpt_net.core.llm import LLM
    
    # Initialize LLM manager
    llm_manager = LLM()
    
    # Get provider
    provider = llm_manager.providers["my_provider"]
    
    # Test model retrieval
    models = provider.get_models()
    assert len(models) > 0
    
    # Test LLM creation
    model = models[0]
    llm = provider.llama(model)
    assert llm is not None
    
    # Test completion
    response = llm.complete("Hello, world!")
    assert response.text
```

---

## 📊 Provider Configuration

### Configuration Schema

```python
class MyProvider(BaseLLM):
    def get_config_schema(self) -> dict:
        """Define configuration options"""
        return {
            "api_key": {
                "type": "text",
                "label": "API Key",
                "description": "Your My Provider API key",
                "secret": True,
                "required": True,
            },
            "api_endpoint": {
                "type": "text",
                "label": "API Endpoint",
                "description": "Custom API endpoint (optional)",
                "default": "https://api.myprovider.com/v1",
            },
            "timeout": {
                "type": "int",
                "label": "Request Timeout",
                "description": "Timeout in seconds",
                "default": 30,
                "min": 1,
                "max": 300,
            },
            "retry_attempts": {
                "type": "int",
                "label": "Retry Attempts",
                "description": "Number of retry attempts on failure",
                "default": 3,
                "min": 0,
                "max": 10,
            },
        }
```

### Loading Configuration

```python
def load_config(self):
    """Load provider configuration"""
    config = self.window.core.config.get("my_provider", {})
    
    self.api_key = config.get("api_key", "")
    self.api_endpoint = config.get("api_endpoint", self.default_endpoint)
    self.timeout = config.get("timeout", 30)
    self.retry_attempts = config.get("retry_attempts", 3)
```

---

## 🔐 Security Best Practices

### API Key Management

```python
class SecureProvider(BaseLLM):
    def get_api_key(self) -> str:
        """Securely retrieve API key"""
        import os
        from cryptography.fernet import Fernet
        
        # Try environment variable first
        api_key = os.getenv("MY_PROVIDER_API_KEY")
        if api_key:
            return api_key
        
        # Try encrypted config
        encrypted_key = self.config.get("api_key_encrypted")
        if encrypted_key:
            cipher = Fernet(self.get_encryption_key())
            return cipher.decrypt(encrypted_key).decode()
        
        # Fallback to plain config (not recommended)
        return self.config.get("api_key", "")
    
    def set_api_key(self, api_key: str, encrypt: bool = True):
        """Securely store API key"""
        if encrypt:
            from cryptography.fernet import Fernet
            cipher = Fernet(self.get_encryption_key())
            encrypted = cipher.encrypt(api_key.encode())
            self.config.set("api_key_encrypted", encrypted)
        else:
            self.config.set("api_key", api_key)
```

### Request Validation

```python
def validate_request(self, prompt: str, **kwargs) -> bool:
    """Validate request before sending"""
    # Check prompt length
    if len(prompt) > self.max_prompt_length:
        raise ValueError("Prompt too long")
    
    # Check for malicious content
    if self.contains_malicious_content(prompt):
        raise ValueError("Malicious content detected")
    
    # Validate parameters
    if "temperature" in kwargs:
        temp = kwargs["temperature"]
        if not 0 <= temp <= 2:
            raise ValueError("Invalid temperature")
    
    return True
```

---

## 🚀 Performance Optimization

### Caching

```python
from functools import lru_cache

class CachedProvider(BaseLLM):
    @lru_cache(maxsize=100)
    def get_completion(self, prompt: str, model: str) -> str:
        """Cached completion"""
        return self.api_call(prompt, model)
    
    def clear_cache(self):
        """Clear completion cache"""
        self.get_completion.cache_clear()
```

### Batch Processing

```python
class BatchProvider(BaseLLM):
    def batch_complete(self, prompts: list[str]) -> list[str]:
        """Process multiple prompts efficiently"""
        # Send batch request
        responses = self.api_batch_call(prompts)
        return [r["text"] for r in responses]
```

### Connection Pooling

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class PooledProvider(BaseLLM):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Setup session with connection pooling
        self.session = requests.Session()
        
        # Configure retries
        retry = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504]
        )
        
        adapter = HTTPAdapter(
            max_retries=retry,
            pool_connections=10,
            pool_maxsize=20
        )
        
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
    
    def api_call(self, prompt: str) -> dict:
        """Make API call with pooled connection"""
        response = self.session.post(
            self.api_endpoint,
            json={"prompt": prompt},
            timeout=self.timeout
        )
        return response.json()
```

---

## 🆘 Error Handling

### Comprehensive Error Handling

```python
class RobustProvider(BaseLLM):
    def llama(self, model: ModelItem, **kwargs) -> LLM:
        """Create LLM with error handling"""
        try:
            # Validate configuration
            if not self.validate_config():
                raise ValueError("Invalid configuration")
            
            # Create LLM
            llm = self.create_llm(model, **kwargs)
            
            # Test connection
            if not self.test_connection(llm):
                raise ConnectionError("Failed to connect to API")
            
            return llm
            
        except ValueError as e:
            self.log_error(f"Configuration error: {e}")
            raise
        except ConnectionError as e:
            self.log_error(f"Connection error: {e}")
            raise
        except Exception as e:
            self.log_error(f"Unexpected error: {e}")
            raise
    
    def api_call_with_retry(self, prompt: str, max_retries: int = 3) -> dict:
        """API call with automatic retry"""
        import time
        
        for attempt in range(max_retries):
            try:
                response = self.api_call(prompt)
                return response
                
            except requests.exceptions.Timeout:
                if attempt < max_retries - 1:
                    wait_time = 2 ** attempt  # Exponential backoff
                    time.sleep(wait_time)
                    continue
                raise
                
            except requests.exceptions.RequestException as e:
                self.log_error(f"Request failed (attempt {attempt + 1}): {e}")
                if attempt < max_retries - 1:
                    time.sleep(1)
                    continue
                raise
```

---

## 📚 Complete Example: Custom Provider

```python
"""
Complete example of a custom AI provider for PyGPT
"""

from llama_index.core.llms import CustomLLM, CompletionResponse, ChatResponse
from llama_index.core.llms import ChatMessage
from pygpt_net.provider.llms.base import BaseLLM
from pygpt_net.item.model import ModelItem
import requests
from typing import Any, List

class MyCustomLLM(CustomLLM):
    """LlamaIndex wrapper for custom provider"""
    
    model: str
    api_key: str
    api_endpoint: str
    temperature: float = 0.7
    max_tokens: int = 2048
    
    @property
    def metadata(self) -> dict:
        return {
            "model": self.model,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
        }
    
    def complete(self, prompt: str, **kwargs: Any) -> CompletionResponse:
        """Generate completion"""
        response = requests.post(
            f"{self.api_endpoint}/completions",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": self.model,
                "prompt": prompt,
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        
        return CompletionResponse(text=data["text"])
    
    def chat(self, messages: List[ChatMessage], **kwargs: Any) -> ChatResponse:
        """Generate chat response"""
        api_messages = [
            {"role": msg.role, "content": msg.content}
            for msg in messages
        ]
        
        response = requests.post(
            f"{self.api_endpoint}/chat",
            headers={"Authorization": f"Bearer {self.api_key}"},
            json={
                "model": self.model,
                "messages": api_messages,
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
            },
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        
        return ChatResponse(
            message=ChatMessage(
                role="assistant",
                content=data["message"]["content"]
            )
        )

class MyCustomProvider(BaseLLM):
    """PyGPT provider for custom AI service"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = "my_custom"
        self.name = "My Custom AI"
        self.type = ["chat", "completion"]
        self.default_endpoint = "https://api.mycustom.ai/v1"
    
    def llama(self, model: ModelItem, **kwargs) -> MyCustomLLM:
        """Create LlamaIndex LLM instance"""
        api_key = self.get_api_key()
        if not api_key:
            raise ValueError("API key not configured")
        
        endpoint = self.config.get("api_endpoint", self.default_endpoint)
        
        return MyCustomLLM(
            model=model.id,
            api_key=api_key,
            api_endpoint=endpoint,
            temperature=kwargs.get('temperature', 0.7),
            max_tokens=kwargs.get('max_tokens', 2048),
        )
    
    def get_models(self) -> List[ModelItem]:
        """Get available models"""
        models = []
        
        model_configs = [
            {
                "id": "custom-chat-v1",
                "name": "Custom Chat v1",
                "ctx": 4096,
                "tokens": 4096,
            },
            {
                "id": "custom-chat-v2",
                "name": "Custom Chat v2",
                "ctx": 8192,
                "tokens": 8192,
                "vision": True,
            },
        ]
        
        for config in model_configs:
            model = ModelItem()
            model.id = config["id"]
            model.name = config["name"]
            model.mode = self.type
            model.llm = self.id
            model.ctx = config["ctx"]
            model.tokens = config["tokens"]
            model.vision = config.get("vision", False)
            models.append(model)
        
        return models
    
    def setup_env(self, api_key: str = None):
        """Setup environment"""
        import os
        if api_key:
            os.environ["MY_CUSTOM_API_KEY"] = api_key
    
    def get_api_key(self) -> str:
        """Get API key"""
        import os
        
        # Try config
        api_key = self.config.get("api_key")
        if api_key:
            return api_key
        
        # Try environment
        return os.getenv("MY_CUSTOM_API_KEY", "")
    
    def get_config_schema(self) -> dict:
        """Configuration schema"""
        return {
            "api_key": {
                "type": "text",
                "label": "API Key",
                "secret": True,
                "required": True,
            },
            "api_endpoint": {
                "type": "text",
                "label": "API Endpoint",
                "default": self.default_endpoint,
            },
        }
```

---

## 📖 Resources

- [Architecture Overview](./architecture.md)
- [Plugin Development](./plugin-development.md)
- [Custom Tools](./custom-tools.md)
- [LlamaIndex Documentation](https://docs.llamaindex.ai/)

---

**Next:** [API Reference](./api-reference.md) →
