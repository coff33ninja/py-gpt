# PyGPT Features Overview

Guide to all major features in PyGPT.

## 🎯 Core Features

---

## 💬 Chat System

**Multi-model conversation interface**

### Features
- ✅ Switch between AI models mid-chat
- ✅ Maintain conversation context
- ✅ Save conversations
- ✅ Export as PDF/Markdown
- ✅ Message history
- ✅ Search chat history

### Providers Supported
- OpenAI (GPT-4, GPT-4o, o1, o3)
- Google Gemini (all models)
- Anthropic Claude
- DeepSeek
- Mistral
- Ollama (local)
- HuggingFace
- And more!

### Tips
- Use Ctrl+N for new chat
- Shift+Enter for new line
- Ctrl+↑ to edit previous message

---

## 🖼️ Vision (Image Analysis)

**Analyze images and photos**

### Capabilities
- ✅ Describe images
- ✅ Extract text (OCR)
- ✅ Analyze charts
- ✅ Read handwriting
- ✅ Identify objects
- ✅ Answer questions about images

### Supported Models
- GPT-4V
- Gemini
- Claude 3
- Others

### Formats
- JPG, PNG, GIF, WebP
- Max 20MB per image

---

## 🎤 Audio (Voice Input/Output)

**Voice interaction**

### Features
- ✅ Speech-to-text (transcription)
- ✅ Text-to-speech (voice response)
- ✅ Multiple languages
- ✅ Voice selection
- ✅ Speed/pitch adjustment

### Transcription
- Uses OpenAI Whisper API
- 50+ languages supported
- Requires internet

### Text-to-Speech Options
- ElevenLabs (natural voice)
- Google TTS
- Azure TTS
- System TTS

---

## 💻 Code Execution

**Execute Python code directly**

### What It Does
- AI writes Python code
- Code executes in isolated environment
- Results shown in chat
- No safety risks

### Supported Libraries
- numpy
- pandas
- matplotlib
- scikit-learn
- requests
- And many more

### Use Cases
- Data analysis
- File operations
- Mathematical calculations
- Data visualization
- Web scraping

### Example
```
You: "Analyze my CSV file"
PyGPT: [Writes Python script]
Result: [Shows analysis with charts]
```

---

## 🔍 Web Search

**Search the internet in real-time**

### What It Does
- AI searches web for current information
- Reads search results
- Synthesizes findings
- Provides citations

### When to Use
- Current events
- Latest news
- Real-time data
- Recent developments

### Example
```
You: "What are latest AI breakthroughs in 2025?"
PyGPT: [Searches web]
Result: [Latest news with sources]
```

---

## 🗄️ Context Management

**Manage conversation memory**

### Features
- ✅ Save conversations
- ✅ Load previous chats
- ✅ Export conversations
- ✅ Search history
- ✅ Context window management

### Storage
- Local SQLite database
- Encrypted (optional)
- Private by default

### Tips
- Regularly export important chats
- Clear old conversations to free space
- Use descriptive names for saved chats

---

## 🎯 Presets & Prompts

**Save and reuse prompt templates**

### What They Are
- Customizable system prompts
- Role definitions
- Instruction templates
- Style guidelines

### Create Preset
1. Settings → Presets
2. Click "New"
3. Name preset (e.g., "Technical Writer")
4. Set system prompt
5. Save

### Use Preset
1. Start chat
2. Select preset from dropdown
3. Chat with preset active

### Example Presets
- "Expert Programmer"
- "Creative Writer"
- "Academic Researcher"
- "Business Analyst"

---

## 🔌 Plugins & Extensions

**Extend functionality**

### Available Plugins
- File operations
- Web search
- Code execution
- Calendar integration
- Custom commands
- And more

### Install Plugin
1. Copy plugin folder to `~/.pygpt/plugins`
2. Restart PyGPT
3. Settings → Plugins
4. Enable plugin

### Create Plugin
See [Plugin Development Guide](../development/plugin-development.md)

---

## 📎 File Attachments

**Include files in conversations**

### Supported Types
- Text files (TXT, MD, PDF)
- Code files (PY, JS, etc)
- Images (JPG, PNG)
- Documents

### How to Attach
1. Click 📎 button
2. Select file
3. Or drag & drop

### Use Cases
- Upload code for review
- Share documents
- Attach images for analysis
- Include data files

---

## 🤖 Agents & Automation

**Let AI execute tasks autonomously**

### What It Does
- AI plans multi-step tasks
- Uses available tools
- Executes steps automatically
- Reports results

### Features
- ✅ Goal planning
- ✅ Tool selection
- ✅ Error recovery
- ✅ Progress reporting

### Example
```
Goal: "Research and summarize AI trends"
Agent:
1. Plans research strategy
2. Searches web
3. Reads articles
4. Synthesizes findings
5. Reports summary
```

---

## 🧠 Vector Store & RAG

**Document retrieval and analysis**

### RAG = Retrieval-Augmented Generation

### What It Does
- Store documents
- Create embeddings
- Search semantic similarity
- Use relevant docs in responses

### Use Cases
- Document analysis
- Knowledge base search
- Company info retrieval
- Research paper analysis

### Supported Formats
- PDF
- TXT
- Markdown
- Code files

---

## 📝 Custom Commands

**Create custom AI commands**

### Examples
- Summarize text
- Translate to language
- Generate ideas
- Code review

### Create Command
1. Settings → Commands
2. Click "New"
3. Name: "Summarize"
4. Prompt: "Summarize the following..."
5. Save

### Use Command
1. Type `/summarize`
2. Paste text
3. Enter
4. Command executes

---

## ⚙️ Advanced Features

### Token Counter
- Shows input/output tokens
- Helps estimate costs
- Real-time updates

### Model Settings
- Temperature (creativity)
- Max tokens (response length)
- Top P (diversity)
- Custom parameters

### Debug Mode
- View detailed logs
- See API requests
- Troubleshoot issues

### Keyboard Shortcuts
- Full shortcut system
- Customizable hotkeys
- Pro tips available

---

## 🔐 Privacy & Security

### Local Storage
- Conversations stored locally
- Not sent to servers by default
- Encrypted (optional)

### API Keys
- Stored securely
- Only sent to provider APIs
- Never logged

### Data Control
- You control all data
- Export anytime
- Delete anytime

---

## 📊 See All Features

- [Chat](./01-chat.md)
- [Vision](./03-vision-images.md)
- [Audio](../guides/04-audio-voice.md)
- [Code Interpreter](./03-code-interpreter.md)
- [Web Search](./04-web-search.md)
- [Vector Store](./05-vector-store-rag.md)
- [Agents](./06-agents-automation.md)
- [Presets](./07-presets-prompts.md)
- [Custom Commands](./08-custom-commands.md)

---

**Next:** [Chat Guide](./01-chat.md) →
