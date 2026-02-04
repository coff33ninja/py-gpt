# Context Management Guide

Managing conversation memory and history in PyGPT.

## 🧠 What Is Context?

Context is the conversation history that AI uses to understand your current message. Larger context = more memory but higher cost.

---

## 📚 Context Window

### Understanding Context Windows

Different models have different limits:
- GPT-3.5: 16K tokens
- GPT-4: 128K tokens
- Gemini: 200K tokens
- Claude: 200K tokens

### How Context Works

1. All previous messages sent with each new message
2. AI reads full history
3. Uses to understand current question
4. Generates response

---

## 💰 Cost Impact

Each message costs:
- Input tokens (all context + new message)
- Output tokens (response)

**Example:**
- Context: 2000 tokens
- New message: 50 tokens
- Total input: 2050 tokens

---

## 🛠️ Managing Context

### Clear Old Messages
1. In chat, select old messages
2. Click delete
3. Context reduced
4. Future messages cheaper

### Start New Chat
1. Create new chat
2. Fresh start
3. No previous context
4. Lower cost

### Context Panel
1. View context in sidebar
2. See what's being sent
3. Identify large messages
4. Remove as needed

---

## 💡 Context Optimization

### Keep Focused
- Delete off-topic messages
- Remove tangents
- Maintain relevance

### Summarize
- Ask AI to summarize
- Use summary in new chat
- Reduce context

### Archive
- Save important chats
- Start fresh regularly
- Keep efficient

---

**Next:** [Code Interpreter](./03-code-interpreter.md) →
