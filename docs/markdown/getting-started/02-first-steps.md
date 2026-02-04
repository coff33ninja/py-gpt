# Your First Steps with PyGPT

Welcome! This guide will get you up and running with your first AI conversation in minutes.

## Prerequisites

- ✅ PyGPT installed (see [Installation Guide](./01-installation.md))
- ✅ An API key from at least one AI provider
- ✅ Basic understanding of AI assistants (helpful but not required)

## Step 1: Launch PyGPT

### Windows
- Click PyGPT icon in Start Menu
- Or: Run `pygpt` in PowerShell

### Linux/macOS
```bash
pygpt
```

**Expected**: Application window opens with empty chat interface

---

## Step 2: Set Up Your First API Key

### Option A: OpenAI (ChatGPT)

1. **Get API Key**
   - Visit [platform.openai.com/api-keys](https://platform.openai.com/api-keys)
   - Create new API key
   - Copy the key

2. **Add to PyGPT**
   - Open Settings (⚙️ icon or menu)
   - Find "API Keys" or "Configuration"
   - Paste OpenAI API key in "OpenAI API key" field
   - Click "Save"

### Option B: Google Gemini (Alternative)

1. **Get API Key**
   - Visit [aistudio.google.com](https://aistudio.google.com)
   - Click "Get API Key"
   - Copy the key

2. **Add to PyGPT**
   - Open Settings
   - Find "Google API key" field
   - Paste key
   - Click "Save"

> **💡 Tip**: Choose Gemini if you want to try a free or cheaper alternative to OpenAI

---

## Step 3: Start Your First Chat

### Basic Chat
1. **Type your message** in the input box at the bottom
   - Example: "Hello! What can you do?"
   
2. **Press Enter** or click Send button

3. **Wait for response** - AI will respond in the main chat area

### Example First Questions
- "What is machine learning?"
- "Explain quantum computing like I'm 5"
- "Write a Python function that calculates fibonacci"
- "Tell me about yourself"

---

## Step 4: Understanding the Interface

### Main Areas

```
┌─────────────────────────────────┐
│     Chat Display Area           │  ← Shows conversation
│                                 │     history
├─────────────────────────────────┤
│ Your message | [Send]           │  ← Input field
└─────────────────────────────────┘
```

### Key UI Elements

| Element | Purpose |
|---------|---------|
| **Chat Area** | Shows all messages from you and AI |
| **Input Box** | Type your questions/prompts |
| **Send Button** | Submit your message |
| **Settings ⚙️** | Configure API keys, models, etc. |
| **New Chat 📝** | Start fresh conversation |
| **Model Selector** | Choose which AI model to use |
| **Context Panel** | View chat history (if available) |

---

## Step 5: Choose a Model

Different AI models have different strengths:

### Recommended for Beginners
- **GPT-3.5 Turbo** (OpenAI) - Fast, affordable, good quality
- **Gemini 2.5 Flash** (Google) - Fast, free tier available
- **Claude 3 Haiku** (Anthropic) - Cheap, reliable

### If You Have More Budget
- **GPT-4** (OpenAI) - More powerful reasoning
- **GPT-4o** (OpenAI) - Better multimodal (images, etc)
- **Claude 3 Opus** (Anthropic) - Best for complex tasks

### For Local/Free
- **Llama 3** (Ollama) - Run locally, free
- **Mistral** (Ollama) - Fast, open source

#### To Select Model
1. Look for "Model" dropdown in main window
2. Select preferred model
3. Click chat to use it

---

## Common First Chat Scenarios

### Scenario 1: Asking Questions
```
You: What is the capital of France?
AI: The capital of France is Paris...
```

### Scenario 2: Writing Code
```
You: Write me a Python function to check if a number is prime
AI: def is_prime(n): ...
```

### Scenario 3: Creative Writing
```
You: Write a short poem about programming
AI: Loops and functions intertwine...
```

### Scenario 4: Getting Explanations
```
You: Explain blockchain in simple terms
AI: Blockchain is like a chain of blocks...
```

---

## Useful Features for Beginners

### 🔄 Continue Conversation
- Just keep typing to continue the same conversation
- AI remembers previous messages

### 🗑️ Clear Chat
- Use "New Chat" button to start fresh
- Previous chats are saved in Context

### 📋 Copy Response
- Hover over AI response
- Click copy icon (or right-click → copy)

### 🔍 Search Chats
- Use search function to find past conversations
- Search by topic, date, or content

### 💾 Save Important Chats
- Mark chats as favorites
- Create folders for organization

---

## Tips for Better Results

### 1. Be Specific
❌ Bad: "Tell me about programming"
✅ Good: "Explain what recursion is and give a Python example"

### 2. Provide Context
❌ Bad: "How do I fix this?"
✅ Good: "I'm getting a NameError when importing numpy. How do I fix it?"

### 3. Break Down Complex Tasks
❌ Bad: "Make me a complete web app"
✅ Good: "First, help me create a basic HTML form with JavaScript validation"

### 4. Use Follow-ups
```
You: What is machine learning?
AI: [Explanation]
You: Can you give me a real-world example?
AI: [Example]
```

---

## Your First Advanced Feature: Presets

Presets are saved prompt templates that help you get better results.

### Using a Preset
1. Open Settings or look for "Presets"
2. Select a preset (e.g., "Code Assistant", "Creative Writing")
3. Presets will pre-configure the AI for that task

---

## Troubleshooting First Steps

### Issue: Nothing Happens When I Send
- ✓ Check internet connection
- ✓ Verify API key is correct in Settings
- ✓ Make sure you selected a model
- ✓ Check if account has credits (especially OpenAI)

### Issue: Slow Response
- ✓ Network might be slow
- ✓ Try smaller model (GPT-3.5 instead of GPT-4)
- ✓ Check your internet speed

### Issue: I Forgot Where Settings Are
- ✓ Look for ⚙️ icon (usually top right)
- ✓ Or check menu → Settings

### Issue: API Key Error
- ✓ Copy the ENTIRE key (no spaces at start/end)
- ✓ Make sure it's the right API key (not token)
- ✓ Regenerate key if lost

---

## What's Next?

Congratulations! You've had your first chat! 🎉

### Continue Learning
- 📖 [Basic Configuration](./03-basic-configuration.md) - Configure more settings
- 📘 [API Key Setup Guide](../guides/02-api-key-setup.md) - Add more providers
- 🔌 [All Providers](../providers/) - Explore different AI services
- ⚡ [Features](../features/) - Learn about advanced features

### Popular Next Steps
1. **Try another provider** - Compare different AIs
2. **Upload a document** - Analyze files with AI
3. **Use Code Interpreter** - Execute Python code
4. **Create custom prompts** - Save prompt templates

---

## Quick Reference

| Action | How To |
|--------|--------|
| Start new chat | Click "New Chat" 📝 |
| Send message | Press Enter or click Send |
| Change model | Select from Model dropdown |
| Access settings | Click ⚙️ Settings |
| Copy AI response | Hover and click copy icon |
| Save chat | Star/bookmark the conversation |
| Clear all | Go to Settings → Clear history |

---

## Common Questions

**Q: Is my data private?**
A: Conversations are sent to your chosen AI provider. Refer to their privacy policy.

**Q: Can I use without internet?**
A: With local models (Ollama) yes, with online models (OpenAI, etc) no.

**Q: How much will this cost?**
A: Depends on provider and usage. See [Pricing Guide](../faq/pricing-costs.md).

**Q: Can I use multiple AI providers?**
A: Yes! Add multiple API keys and switch between them.

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Enter` | Send message |
| `Shift+Enter` | New line in message |
| `Ctrl+K` | Clear chat |
| `Ctrl+N` | New chat |
| `Ctrl+,` | Open settings |

---

**Getting stuck?** 
- 📖 Check [FAQ](../faq/)
- 🐛 View [Troubleshooting](../reference/troubleshooting.md)
- 💬 Join [Discord](https://pygpt.net/discord)

**Next**: [Basic Configuration](./03-basic-configuration.md) →
