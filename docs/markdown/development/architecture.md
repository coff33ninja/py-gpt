# PyGPT Architecture Overview

Understanding PyGPT's structure and how components work together.

## 🏗️ High-Level Architecture

```
┌─────────────────────────────────────────────┐
│           UI Layer (PySide/Qt)              │
│  • Chat Interface  • Settings • Plugins UI  │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│      Controller Layer (Business Logic)      │
│  • Chat Management  • File Handling         │
│  • Context Management • Command Execution   │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│        Core Layer (PyGPT Core)              │
│  • Config Management  • Plugin System       │
│  • Database (SQLite)  • Indexing (LlamaIdx) │
│  • Audio/Vision Processing • Web Access    │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│      Provider Layer (AI Services)           │
│  • OpenAI • Google • Anthropic • DeepSeek   │
│  • Local (Ollama) • Other Providers         │
└──────────────────┬──────────────────────────┘
                   │
┌──────────────────▼──────────────────────────┐
│      External APIs (Cloud Services)         │
│  • LLM APIs (GPT, Gemini, etc.)             │
│  • Embeddings • Vector Stores               │
│  • Audio Services • Image Generation        │
└─────────────────────────────────────────────┘
```

---

## 📁 Directory Structure

```
src/pygpt_net/
├── app.py                 # Main application entry
├── app_core.py           # Core orchestrator
├── config.py             # Configuration management
├── launcher.py           # Application launcher
├── utils.py              # Utility functions
│
├── controller/           # UI Controllers & Logic
│   ├── chat/            # Chat handling
│   ├── context/         # Context management
│   ├── files/           # File operations
│   ├── model/           # Model selection
│   └── ...
│
├── core/                # Core functionality
│   ├── agents.py        # Agent system
│   ├── assistants.py    # Assistant mode
│   ├── audio.py         # Audio processing
│   ├── bridge.py        # API bridge
│   ├── calendar.py      # Calendar integration
│   ├── camera.py        # Camera capture
│   ├── command.py       # Command execution
│   ├── db.py            # Database
│   ├── filesystem.py    # File I/O
│   ├── image.py         # Image operations
│   ├── llm.py           # LLM interface
│   ├── models.py        # Model management
│   ├── plugins.py       # Plugin system
│   ├── tokens.py        # Token counting
│   ├── vision.py        # Vision processing
│   ├── web.py           # Web access
│   └── ...
│
├── provider/            # AI Provider Integrations
│   ├── llms/            # LLM providers
│   │   ├── openai.py
│   │   ├── google.py
│   │   ├── anthropic.py
│   │   └── ...
│   ├── api/             # Provider API handlers
│   │   ├── openai/
│   │   ├── google/
│   │   └── ...
│   ├── audio_input/     # Speech recognition
│   ├── audio_output/    # Text-to-speech
│   └── ...
│
├── plugin/              # Plugin System
│   ├── base.py          # Base plugin class
│   ├── cmd_files.py     # File commands plugin
│   ├── cmd_web.py       # Web search plugin
│   ├── audio_input.py   # Audio input plugin
│   └── ...
│
├── ui/                  # User Interface
│   ├── base/            # Base components
│   ├── dialog/          # Dialog windows
│   ├── layout/          # UI layouts
│   ├── menu/            # Menus
│   └── widget/          # Custom widgets
│
├── item/                # Data Models
│   ├── model.py         # ModelItem
│   ├── context.py       # ContextItem
│   └── ...
│
├── data/                # Application Data
│   ├── locale/          # Translations
│   ├── models/          # Model definitions
│   ├── icons/           # UI icons
│   └── ...
│
└── migrations/          # Database migrations
```

---

## 🔄 Data Flow Example: Chat Message

### User sends a message:

```
1. USER INPUT
   └─→ Text typed in chat input box

2. UI LAYER
   └─→ ChatController receives input
   └─→ Validates message
   └─→ Adds to UI (shows user message)

3. CORE PROCESSING
   └─→ Get current model & config
   └─→ Build prompt (with context/presets)
   └─→ Count tokens
   └─→ Prepare attachment data

4. PROVIDER LAYER
   └─→ BridgeContext created
   └─→ Select correct provider (OpenAI/Google/etc)
   └─→ Prepare API request

5. EXTERNAL API
   └─→ Send to LLM API
   └─→ Stream response back
   └─→ Handle errors/retries

6. POST-PROCESSING
   └─→ Parse response
   └─→ Extract commands (if any)
   └─→ Execute commands (code, web search, etc)

7. STORAGE
   └─→ Save to database
   └─→ Update context history
   └─→ Update embeddings (if RAG enabled)

8. UI UPDATE
   └─→ Display AI response
   └─→ Update token counter
   └─→ Show status
```

---

## 🔌 Plugin System

### Plugin Architecture

```
PluginBase
├── cmd_* plugins         # Commands (file, web, code, etc)
├── audio_* plugins       # Audio (input, output)
├── provider_* plugins    # Custom providers
└── custom plugins        # User-created
```

### Plugin Lifecycle

```
1. Discovery
   └─→ PyGPT scans plugins directory
   └─→ Loads plugin metadata

2. Initialization
   └─→ Plugin.__init__() called
   └─→ Register handlers
   └─→ Load configuration

3. Runtime
   └─→ Plugin listens for events
   └─→ Executes on triggers
   └─→ Returns results

4. Shutdown
   └─→ Plugin cleanup
   └─→ Save state (if needed)
```

---

## 🗄️ Data Storage

### SQLite Database

```
database.db
├── contexts          # Chat conversations
├── attachments       # File attachments
├── presets          # Prompt templates
├── models           # Available models
├── calendar         # Calendar entries
├── notes            # User notes
└── chat_history     # Full history
```

### File Storage

```
~/.pygpt/
├── config.json      # Main configuration
├── data/            # User data
│   ├── contexts/    # Saved conversations
│   ├── attachments/ # Uploaded files
│   ├── models/      # Model cache
│   └── embeddings/  # Vector store
└── cache/           # Temporary files
```

---

## 🤖 AI Integration Points

### LLM Integration

```
ModelItem (config)
    ↓
Provider-specific wrapper (GoogleLLM, OpenAILLM, etc)
    ↓
LlamaIndex wrapper (for advanced features)
    ↓
External API calls
    ↓
Response processing
    ↓
Command extraction (if enabled)
    ↓
Result to UI
```

### Multi-Modal Support

```
Input types:
├── Text messages
├── Images (for vision models)
├── Audio (for voice input)
├── Files (for RAG)
└── Real-time camera

Output types:
├── Text responses
├── Generated images
├── Audio/speech
├── Code execution results
└── Web search results
```

---

## 🔐 Security Architecture

### API Key Management
```
User API Key
    ↓
Encrypted storage (if enabled)
    ↓
Environment variable or config file
    ↓
Only sent to legitimate provider API
    ↓
Never logged or exposed
```

### Data Privacy
```
Chat data
    ↓
Stored locally by default
    ↓
Or sent to selected AI provider
    ↓
User responsible for provider's privacy policy
    ↓
No data sent elsewhere
```

---

## 🧩 Key Components

### BridgeContext
Central data container for API calls:
```python
BridgeContext {
    - messages: list        # Conversation history
    - model: ModelItem      # Selected model
    - prompt: str           # System prompt
    - attachments: list     # Files/images
    - temperature: float    # Model parameter
    - max_tokens: int       # Response limit
    - extra_params: dict    # Custom params
}
```

### ModelItem
Represents an AI model:
```python
ModelItem {
    - id: str               # Model identifier
    - name: str             # Display name
    - provider: str         # OpenAI, Google, etc
    - mode: str             # chat, completion, image
    - token_limit: int      # Context window
    - vision: bool          # Supports images
    - audio: bool           # Supports audio
}
```

### Config Manager
Centralized configuration:
```
config.get(key)         # Get value
config.set(key, value)  # Set value
config.save()           # Persist to disk
config.reset()          # Reset to defaults
```

---

## 🔄 Mode System

### Operating Modes

```
Chat Mode
└─→ Normal conversation with AI

Completion Mode
└─→ Text completion/generation

Vision Mode
└─→ Image analysis and generation

Assistant Mode
└─→ OpenAI assistants with tools

Agent Mode
└─→ Autonomous task execution

Langchain Mode
└─→ Advanced chain operations

Audio Mode
└─→ Real-time voice interaction

Research Mode
└─→ Multi-source information gathering
```

---

## ⚡ Performance Considerations

### Optimization Strategies

1. **Caching**
   - Model cache
   - Response cache
   - Embedding cache

2. **Streaming**
   - Real-time response display
   - Reduces latency perception

3. **Threading**
   - API calls on background threads
   - Keeps UI responsive

4. **Lazy Loading**
   - Load features only when needed
   - Faster startup

---

## 🧪 Testing Architecture

```
tests/
├── unit/           # Individual component tests
├── integration/    # Component interaction tests
├── fixtures/       # Mock data
└── conftest.py     # Test configuration
```

---

## 🔄 Extensibility Points

### Adding New Features

1. **New Provider**: Create provider in `provider/llms/`
2. **New Plugin**: Extend `PluginBase` in `plugin/`
3. **New UI Component**: Create in `ui/widget/`
4. **New Data Type**: Add to `item/`
5. **New Command**: Add to plugin system

---

## 📊 Dependency Map

```
Core Dependencies:
├── PySide6           # UI framework
├── LlamaIndex        # RAG & indexing
├── google-genai      # Google API
├── openai            # OpenAI API
├── anthropic         # Anthropic API
├── sqlalchemy        # Database ORM
├── pydantic          # Data validation
└── pydub             # Audio processing

Optional Dependencies:
├── chromadb          # Vector database
├── requests          # HTTP client
├── beautifulsoup4    # HTML parsing
└── pillow            # Image processing
```

---

## 🚀 Development Workflow

### Making Changes

1. **Create feature branch**
2. **Modify code** in appropriate module
3. **Add tests** in `tests/`
4. **Run tests** to verify
5. **Update docs** if needed
6. **Create pull request**

### Adding a New Provider

1. Create `provider/llms/my_provider.py`
2. Extend `BaseLLM` class
3. Implement required methods:
   - `llama()` - LlamaIndex integration
   - `get_models()` - List available models
   - `setup_env()` - Environment setup
4. Register in provider registry
5. Add to UI model selector

---

## 📈 Scaling Considerations

### Future Enhancements

- Multi-GPU support
- Distributed processing
- Advanced caching strategies
- Model optimization (quantization, pruning)
- Mobile deployment

---

## 🆘 Getting Help

- **Architecture questions**: [GitHub Discussions](https://github.com/szczyglis-dev/py-gpt/discussions)
- **Code review**: [Pull Requests](https://github.com/szczyglis-dev/py-gpt/pulls)
- **Bug reports**: [GitHub Issues](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next**: [Plugin Development Guide](./plugin-development.md) →
