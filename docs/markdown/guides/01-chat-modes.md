# Chat Modes Guide

Explanation of all PyGPT operating modes and how to use them.

## 🎯 Available Modes

PyGPT supports multiple operating modes for different tasks.

---

## 💬 Chat Mode

**Standard conversation mode**

### What It Is
Normal back-and-forth conversation with AI

### How to Use
1. Select "Chat" mode from Mode dropdown
2. Type message
3. Send (Enter)
4. AI responds

### Best For
- General questions
- Brainstorming
- Discussions
- Everyday use

### Features
- ✅ Context maintained
- ✅ Multi-turn conversations
- ✅ All providers supported

---

## 🎨 Completion Mode

**Text generation and completion**

### What It Is
AI generates text based on your prompt (no back-and-forth)

### How to Use
1. Select "Completion" mode
2. Enter your text prompt
3. Send
4. AI completes/generates text

### Best For
- Writing assistance
- Story generation
- Code generation
- Email drafting

### Example
```
Input: "Write a short story about AI:\n"
Output: [AI writes a complete story]
```

---

## 🖼️ Vision Mode

**Analyze images and photos**

### What It Is
Upload images and ask AI to analyze them

### How to Use
1. Select "Vision" mode
2. Attach image (📎 button)
3. Ask question about image
4. AI analyzes and responds

### Supported Formats
- JPG
- PNG
- GIF
- WebP

### Best For
- Image analysis
- Describing photos
- Extracting text (OCR)
- Analyzing charts
- Reading handwriting

### Example
```
Attach: Photo of chart
Ask: "What trends do you see?"
Response: [AI describes trends]
```

### Requirements
- Model must support vision (GPT-4V, Gemini, Claude)
- Image under 20MB
- Internet connection

---

## 🎤 Audio Mode

**Voice input and output**

### What It Is
Speak to AI and/or hear responses

### How to Use
1. Select "Audio" mode
2. Click 🎤 to record or use microphone
3. Speak your question
4. Click stop when done
5. AI transcribes and responds
6. Click 🔊 to hear response

### Input Languages
- English
- Spanish
- French
- German
- Chinese
- Japanese
- 50+ languages

### Best For
- Hands-free operation
- Accessibility
- Multitasking
- Quick voice notes

### Requirements
- Microphone
- Speaker (for audio output)
- Internet for transcription

---

## 💻 Code Interpreter Mode

**Execute Python code**

### What It Is
PyGPT can write and execute Python code in an isolated environment

### How to Use
1. Select "Code Interpreter" mode
2. Describe what you want
3. AI writes code
4. Code executes automatically
5. Results shown in chat

### Features
- ✅ Python execution
- ✅ Data analysis
- ✅ File operations
- ✅ Visualization

### Example
```
Ask: "Analyze the data in my CSV file"
AI: [Writes Python code]
Result: [Code executes and shows analysis]
```

### Supported Libraries
- numpy
- pandas
- matplotlib
- scikit-learn
- Many others

---

## 🤖 Agent Mode

**Autonomous task execution**

### What It Is
AI can break down complex tasks and use tools to complete them

### How to Use
1. Select "Agent" mode
2. Describe task
3. AI plans and executes steps
4. Uses available tools
5. Returns results

### Features
- ✅ Multi-step reasoning
- ✅ Tool usage
- ✅ Error recovery
- ✅ Autonomous execution

### Example
```
Ask: "Research and summarize AI trends"
AI: [Breaks down task]
- Uses web search
- Reads multiple sources
- Summarizes findings
Result: [Comprehensive summary]
```

---

## 🔗 Langchain Mode

**Advanced chaining of operations**

### What It Is
Chain multiple LLM operations together

### How to Use
1. Select "Langchain" mode
2. Configure chain
3. Execute
4. Results combine from multiple steps

### Best For
- Complex workflows
- Multi-step reasoning
- Combining multiple tools

---

## 🔍 Research Mode

**Multi-source information gathering**

### What It Is
AI gathers and synthesizes information from multiple sources

### How to Use
1. Select "Research" mode
2. Ask research question
3. AI searches multiple sources
4. Compiles findings

### Features
- ✅ Web search
- ✅ Multiple sources
- ✅ Synthesis
- ✅ Citations

---

## 🧠 Thinking Mode (Extended Thinking)

**Advanced reasoning**

### What It Is
AI takes time to think deeply about complex problems

### How to Use
1. Select "Thinking" mode
2. Ask complex question
3. AI shows reasoning process
4. Provides detailed answer

### Best For
- Complex math
- Logic problems
- Philosophical questions
- Detailed analysis

### Note
- Slower responses
- More accurate
- Higher cost (tokens for thinking)

---

## 📋 Mode Comparison

| Mode | Speed | Input | Output | Use Case |
|------|-------|-------|--------|----------|
| Chat | Fast | Text | Text | General |
| Completion | Fast | Text | Text | Generation |
| Vision | Medium | Image+Text | Text | Analysis |
| Audio | Medium | Voice | Voice/Text | Hands-free |
| Code | Varies | Text | Results | Programming |
| Agent | Slower | Text | Results | Complex tasks |
| Thinking | Slowest | Text | Text | Deep reasoning |

---

## ⚙️ Switching Modes

### Method 1: Mode Dropdown
1. Find mode selector at top
2. Click dropdown
3. Select new mode
4. Chat continues with new mode

### Method 2: Keyboard Shortcut
- Often available, check Settings → Keyboard

### Note
- Context may change between modes
- Some context incompatible with some modes
- Previous messages usually retained

---

## 🎯 Choosing the Right Mode

### Need general conversation?
→ **Chat Mode**

### Want AI to write something?
→ **Completion Mode**

### Have an image to analyze?
→ **Vision Mode**

### Want to use voice?
→ **Audio Mode**

### Need to run code?
→ **Code Interpreter Mode**

### Complex task with multiple steps?
→ **Agent Mode**

### Need deep reasoning?
→ **Thinking Mode**

### Researching a topic?
→ **Research Mode**

---

## 💡 Pro Tips

### Tip 1: Combine Modes
- Start in Chat to plan
- Switch to Code to implement
- Switch to Vision to verify

### Tip 2: Mode Settings
- Each mode has settings
- Customize before using
- Save favorite configurations

### Tip 3: Switching Without Losing Context
- When you switch modes, previous messages usually stay
- New mode builds on prior context
- Some modes may ignore irrelevant context

### Tip 4: Agent Mode Pro Tip
- Be specific about goals
- Agent will use available tools
- Check each step if needed

---

## 🐛 Troubleshooting

### Mode Not Available
- Check if model supports mode
- Some modes require specific providers
- Upgrade to premium models if needed

### Context Lost Switching Modes
- Take screenshot before switching
- Copy important text
- Some modes incompatible with all context types

### Audio Mode Issues
- Check microphone is enabled
- Check speaker is working
- Check internet connection
- Try system audio test first

---

## 📚 See Also
- [First Steps](../getting-started/02-first-steps.md)
- [Chat Features](../features/01-chat.md)
- [Code Interpreter](../features/03-code-interpreter.md)

---

**Next:** [Advanced Settings](./07-advanced-settings.md) →
