# Chat Interface

Master the core chat functionality in PyGPT.

## 💬 Overview

The Chat interface is the primary way to interact with AI models in PyGPT. It provides a familiar chat experience similar to ChatGPT, with additional features for power users.

**Key Features:**
- Multi-model support
- Context persistence
- Message history
- Rich formatting
- Code highlighting
- Image support
- File attachments
- Voice input/output

## 🚀 Getting Started

### Basic Chat

1. **Launch PyGPT**
2. **Select Chat mode**
3. **Choose a model**
4. **Type your message**
5. **Press Enter or click Send**

That's it! The AI will respond to your message.

### Your First Conversation

```
You: Hello! Can you help me with Python?

AI: Of course! I'd be happy to help you with Python. 
What would you like to know or work on?

You: How do I read a CSV file?

AI: Here's how to read a CSV file in Python:

[Code example provided]

Would you like me to explain any part of this code?
```

## 🎯 Interface Elements

### Chat Window

The main area where conversation appears.

**Features:**
- Scrollable history
- Rich text formatting
- Code syntax highlighting
- Inline images
- Clickable links
- Copy buttons
- Message timestamps

**Controls:**
- Scroll to view history
- Click code blocks to copy
- Right-click for options
- Zoom with Ctrl + Mouse wheel

### Input Field

Where you type your messages.

**Features:**
- Multi-line input
- Auto-resize
- Character counter
- Token counter
- Attachment button
- Voice input button

**Shortcuts:**
- Enter: Send message
- Shift + Enter: New line
- Ctrl + ↑/↓: Navigate prompt history
- Ctrl + A: Select all
- Ctrl + Z: Undo

### Model Selector

Choose which AI model to use.

**Location:** Top-right dropdown

**Features:**
- Search models
- Filter by provider
- See model capabilities
- Quick switch

**Popular Models:**
- GPT-4: Most capable
- GPT-3.5: Fast and cost-effective
- Claude: Great reasoning
- Gemini: Free tier available
- Ollama: Local models

### Preset Selector

Load saved prompt templates.

**Location:** Below model selector

**Features:**
- Quick preset switching
- Custom system prompts
- Role definitions
- Saved configurations

**Example Presets:**
- Default
- Code Assistant
- Creative Writer
- Technical Expert
- Translator

## 🔧 Chat Features

### Context Management

PyGPT maintains conversation context automatically.

**How it works:**
- All messages stored
- Context sent with each request
- Model remembers conversation
- Long-term memory available

**Context Window:**
- Limited by model
- Older messages may be truncated
- Important: Save long conversations

**Manual Context:**
- Clear context: Start fresh
- Load context: Resume conversation
- Save context: Preserve for later

### Message Actions

Right-click any message for options:

**User Messages:**
- Edit message
- Regenerate response
- Copy message
- Delete message

**AI Messages:**
- Copy message
- Copy code blocks
- Regenerate response
- Continue response
- Rate response

### Code Blocks

Code appears in formatted blocks with syntax highlighting.

**Features:**
- Syntax highlighting
- Line numbers
- Copy button
- Language detection
- Run button (for Python)

**Example:**
```python
def hello_world():
    print("Hello, World!")
    
hello_world()
```

**Actions:**
- Click copy icon to copy code
- Click run icon to execute (if enabled)
- Select text to copy portion

### Inline Images

Images can appear directly in chat.

**Sources:**
- AI-generated images
- Uploaded images
- Camera captures
- File attachments

**Actions:**
- Click to view full size
- Right-click for options
- Save to disk
- Use in follow-up

### Markdown Support

Rich text formatting in messages.

**Supported:**
- **Bold** text
- *Italic* text
- `Code` inline
- [Links](https://example.com)
- Lists (bulleted/numbered)
- Tables
- Blockquotes
- Headings

**Math Formulas:**
- Inline: $E = mc^2$
- Block: $$\int_0^\infty e^{-x^2} dx$$

### Search & Filter

Find messages in conversation.

**Search:**
- Ctrl + F to open search
- Enter search term
- Navigate results
- Case-sensitive option

**Filter:**
- Show only user messages
- Show only AI messages
- Show only code blocks
- Show only images

## 🎨 Customization

### Appearance

**Theme:**
- Light theme
- Dark theme
- Custom themes
- Color schemes

**Font:**
- Font family
- Font size
- Line spacing
- Code font

**Layout:**
- Message spacing
- Avatar display
- Timestamp format
- Compact mode

### Behavior

**Auto-scroll:**
- Scroll to new messages
- Stay at current position
- Manual control

**Notifications:**
- Sound on response
- Desktop notifications
- Flash taskbar

**Input:**
- Auto-focus input
- Clear on send
- Save drafts

## 💡 Advanced Features

### Multi-turn Conversations

Build complex discussions over multiple messages.

**Example:**
```
Turn 1:
You: I need to build a web scraper
AI: I can help! What website and what data?

Turn 2:
You: News articles from example.com
AI: Here's a Python script using BeautifulSoup...

Turn 3:
You: Add error handling
AI: Updated script with try-except blocks...

Turn 4:
You: How do I run this?
AI: Here are the steps to run the scraper...
```

### Context Injection

Add additional context to any message.

**Methods:**
- Attach files
- Reference previous conversations
- Include external data
- Use RAG (vector store)

**Example:**
```
You: [Attaches code file]
"Review this code for security issues"

AI: [Analyzes attached code]
"I found several security concerns..."
```

### Streaming Responses

See AI responses as they're generated.

**Benefits:**
- Faster perceived response
- Can stop early if needed
- More engaging experience

**Controls:**
- Stop button appears during streaming
- Click to halt generation
- Partial response saved

### Response Regeneration

Get a different response to the same prompt.

**How to:**
1. Right-click AI message
2. Select "Regenerate"
3. New response generated
4. Previous response saved in history

**Use cases:**
- Unsatisfied with response
- Want alternative approach
- Exploring different angles

### Message Editing

Edit your messages after sending.

**How to:**
1. Right-click your message
2. Select "Edit"
3. Modify text
4. Save changes
5. AI responds to edited version

**Use cases:**
- Fix typos
- Clarify question
- Add details
- Change direction

### Continue Response

Ask AI to continue incomplete response.

**How to:**
1. Right-click AI message
2. Select "Continue"
3. AI continues from where it stopped

**Use cases:**
- Response was cut off
- Want more detail
- Need complete code

## 🔗 Integration Features

### File Attachments

Attach files to your messages.

**Supported:**
- Documents (PDF, DOCX, TXT)
- Code files (PY, JS, etc.)
- Images (JPG, PNG)
- Data files (CSV, JSON)

**How to:**
1. Click attachment button (📎)
2. Select file
3. File appears in message
4. Send message

**AI can:**
- Read file contents
- Analyze data
- Review code
- Extract information

### Voice Input

Speak your messages instead of typing.

**How to:**
1. Click microphone button (🎤)
2. Speak your message
3. Speech converted to text
4. Edit if needed
5. Send message

**Requirements:**
- Microphone access
- Internet connection
- Whisper API key (or local Whisper)

### Voice Output

Hear AI responses spoken aloud.

**How to:**
1. Enable audio output in settings
2. AI responses automatically spoken
3. Or click speaker icon on message

**Options:**
- Voice selection
- Speed adjustment
- Volume control
- Auto-play toggle

### Camera Capture

Capture images from camera for analysis.

**How to:**
1. Click camera button (📷)
2. Camera preview opens
3. Capture image
4. Image attached to message
5. Send for analysis

**Use cases:**
- Show physical objects
- Share whiteboard drawings
- Capture documents
- Real-time vision

## 🐛 Troubleshooting

### Messages Not Sending
**Problem:** Message won't send

**Solutions:**
- Check internet connection
- Verify API key is valid
- Check API quota/limits
- Try different model
- Check error message

### Slow Responses
**Problem:** AI takes too long

**Solutions:**
- Use faster model (GPT-3.5)
- Reduce context length
- Simplify prompt
- Check internet speed
- Try different provider

### Context Lost
**Problem:** AI forgets conversation

**Solutions:**
- Check context window size
- Save important conversations
- Use shorter messages
- Enable context persistence
- Check model limits

### Formatting Issues
**Problem:** Text not formatted correctly

**Solutions:**
- Check markdown syntax
- Verify code block formatting
- Try different theme
- Clear cache
- Restart application

## 💡 Best Practices

### Writing Effective Prompts

```
❌ "help me code"
✅ "Help me write a Python function to parse JSON files"

❌ "make it better"
✅ "Improve this code's error handling and add comments"

❌ "what about this"
✅ "Analyze this code for security vulnerabilities"
```

### Managing Long Conversations

```
✅ Save important conversations
✅ Start new chat for new topics
✅ Summarize long discussions
✅ Export for reference
❌ One endless conversation
❌ Mix unrelated topics
```

### Using Context Effectively

```
✅ Provide relevant background
✅ Reference previous messages
✅ Attach supporting files
✅ Be specific
❌ Assume AI remembers everything
❌ Vague references
```

### Optimizing Performance

```
✅ Use appropriate model for task
✅ Clear old contexts
✅ Disable unused features
✅ Close other applications
❌ Always use most expensive model
❌ Keep hundreds of contexts loaded
```

## 🔗 Related Features

- [Context Management](./02-context-management.md) - Save and load conversations
- [Presets & Prompts](./07-presets-prompts.md) - Prompt templates
- [File Attachments](../guides/03-working-with-files.md) - Working with files
- [Voice Features](../guides/04-audio-voice.md) - Audio input/output

## 📚 Additional Resources

- [Chat Modes Guide](../guides/01-chat-modes.md) - Different chat modes
- [Keyboard Shortcuts](../reference/keyboard-shortcuts.md) - Speed up workflow
- [Troubleshooting](../reference/troubleshooting.md) - Common issues

## 🆘 Need Help?

- Check [FAQ](../faq/general.md)
- Visit [Troubleshooting Guide](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Context Management](./02-context-management.md) →
