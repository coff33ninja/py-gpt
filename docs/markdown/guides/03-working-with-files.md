# Working with Files Guide

How to upload, attach, and manage files in PyGPT.

## 📎 File Attachment Basics

### Supported File Types

| Type | Formats | Use |
|------|---------|-----|
| **Images** | JPG, PNG, GIF, WebP | Vision analysis |
| **Documents** | PDF, TXT, Markdown | Text analysis |
| **Code** | PY, JS, TS, Java, etc | Code review |
| **Data** | CSV, JSON | Data analysis |

### File Size Limits
- Image: 20MB max
- Document: Usually 10MB
- Code: No limit

---

## 📤 Uploading Files

### Method 1: Click Button

1. Find 📎 (attachment) button
2. Click attachment
3. Browse and select file
4. File attaches to chat

### Method 2: Drag & Drop

1. Select file from file explorer
2. Drag into chat window
3. Drop to attach
4. File ready to send

### Method 3: Copy & Paste

1. Some files can be copied
2. Ctrl+C to copy file contents
3. Ctrl+V in chat
4. Paste as text

---

## 🖼️ Working with Images

### Attach Image for Analysis

1. Click 📎 attachment button
2. Select image file
3. Type question about image
4. Send message
5. AI analyzes image

### Supported Analysis

- ✅ Describe image
- ✅ Extract text (OCR)
- ✅ Read charts
- ✅ Identify objects
- ✅ Answer questions

### Example

```
Attach: Screenshot of table
Ask: "What's the total in column C?"
Response: [AI reads and calculates]
```

### Requirements

- Model supports vision (GPT-4V, Gemini, Claude)
- Image under 20MB
- Internet connection

---

## 📝 Working with Documents

### Upload PDF or Text

1. Click 📎 button
2. Select document
3. Ask question about document
4. AI analyzes and responds

### Document Analysis

- ✅ Summarization
- ✅ Key points extraction
- ✅ Search for topics
- ✅ Answer questions
- ✅ Translation

### Example

```
Attach: research-paper.pdf
Ask: "What are the main findings?"
Response: [AI summarizes findings]
```

### Large Documents

For very large documents:
1. Split into sections
2. Analyze section by section
3. Compile results
4. Or use Vector Store for RAG

---

## 💻 Code File Review

### Upload Code for Review

1. Attach code file or paste code
2. Ask for code review
3. Ask for improvements
4. AI analyzes code

### Review Questions

- "Review this code for bugs"
- "How can I improve this?"
- "Explain what this function does"
- "Refactor this code"

### Example

```
Paste: Python function
Ask: "Are there any bugs?"
Response: [AI analyzes code]
```

---

## 📊 Data File Analysis

### Analyze CSV/JSON Data

1. Attach data file
2. Describe analysis needed
3. AI may:
   - Load and examine file
   - Run analysis code
   - Show visualizations
   - Answer questions

### Example

```
Attach: sales_data.csv
Ask: "What's the trend over time?"
Response: [AI analyzes with code + chart]
```

---

## 🔍 Managing Multiple Files

### Attach Multiple Files

1. Click 📎 multiple times
2. Or drag & drop multiple
3. All files attach to message
4. Send message

### Analysis

AI can:
- ✅ Compare files
- ✅ Merge data
- ✅ Cross-reference
- ✅ Analyze relationships

### Example

```
Attach: sales-2024.csv + sales-2023.csv
Ask: "Compare growth"
Response: [AI compares both files]
```

---

## 💾 Saving & Exporting

### Export Conversation with Files

1. Right-click chat
2. Select "Export"
3. Choose format (PDF, Markdown, JSON)
4. Files included in export

### Save Attachments

For each attachment:
- View in chat
- Some can be downloaded
- Or re-attach later

---

## 🔐 File Privacy

### Your Data Security

- ✅ Files stored locally by default
- ✅ Only sent to AI provider when needed
- ✅ Not stored on provider's servers
- ✅ Check provider's privacy policy

### Sensitive Files

For sensitive information:
- Use local Ollama (no uploads)
- Check provider's security
- Consider encryption
- Don't upload extremely sensitive data

---

## 🐛 Troubleshooting

### File Won't Attach

**Check:**
1. File size under limit?
2. Format supported?
3. File not corrupted?
4. Storage space available?

**Try:**
- Drag & drop instead of button
- Paste text instead of file
- Try smaller file
- Check file permissions

### File Upload Fails

**Solutions:**
1. Check internet connection
2. Try different file
3. Restart PyGPT
4. Clear cache

### Large File Too Slow

**Options:**
1. Split file into smaller parts
2. Compress file
3. Send text summary instead
4. Use Vector Store for RAG

---

## 📚 See Also

- [Vision Guide](./05-vision-images.md)
- [Code Interpreter](../features/03-code-interpreter.md)
- [Vector Store & RAG](../features/05-vector-store-rag.md)

---

**Next:** [Audio & Voice Guide](./04-audio-voice.md) →
