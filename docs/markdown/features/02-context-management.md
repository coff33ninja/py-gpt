# Context Management

Save, load, and organize your conversations.

## 💾 Overview

Context Management in PyGPT allows you to save conversations, resume them later, search through history, and organize your interactions with AI models.

**Key Features:**
- Save conversations
- Load previous chats
- Search history
- Export conversations
- Context groups
- Calendar integration
- Auto-summarization

## 🚀 Getting Started

### Automatic Context Saving

PyGPT automatically saves your conversations as you chat.

**What's saved:**
- All messages (user and AI)
- Timestamps
- Model used
- Attachments
- Metadata

**When it's saved:**
- After each message
- Real-time updates
- No manual save needed

### Context List

View all your saved conversations in the context list.

**Location:** Left sidebar

**Features:**
- Chronological order
- Search functionality
- Group by date
- Pin important contexts
- Color labels

## 🎯 Use Cases

### Resume Conversations
```
Save a conversation about a project, 
close PyGPT, and resume later exactly 
where you left off.
```

### Organize by Topic
```
Group contexts by:
- Projects
- Topics
- Clients
- Dates
```

### Search History
```
Find that conversation where AI 
explained a specific concept or 
provided a code solution.
```

### Export for Reference
```
Export conversations as:
- PDF documents
- Markdown files
- Plain text
- JSON data
```

## 🔧 Context Operations

### Creating Contexts

**New Context:**
```
File → New Context
Or: Ctrl + N
```

**Auto-create:**
- First message creates context
- Named automatically
- Can rename later

### Loading Contexts

**From List:**
1. Click context in list
2. Conversation loads
3. Continue chatting

**From Search:**
1. Search for keyword
2. Click result
3. Context loads

**Recent Contexts:**
- Quick access to recent
- Keyboard shortcuts
- Pin favorites

### Renaming Contexts

**How to:**
1. Right-click context
2. Select "Rename"
3. Enter new name
4. Press Enter

**Auto-naming:**
- AI can suggest names
- Based on conversation content
- Enable in settings

### Deleting Contexts

**Single Context:**
1. Right-click context
2. Select "Delete"
3. Confirm deletion

**Multiple Contexts:**
1. Select contexts (Ctrl + Click)
2. Right-click selection
3. Select "Delete Selected"
4. Confirm deletion

**Bulk Delete:**
```
Tools → Context Manager → Bulk Operations
- Delete by date range
- Delete by keyword
- Delete empty contexts
```

## 📁 Context Organization

### Groups

Organize contexts into groups.

**Create Group:**
1. Right-click in context list
2. Select "New Group"
3. Name the group
4. Drag contexts into group

**Group Features:**
- Collapsible
- Color coding
- Nested groups
- Drag and drop

**Example Groups:**
```
📁 Work Projects
  ├─ Project A
  ├─ Project B
  └─ Project C

📁 Learning
  ├─ Python Tutorials
  ├─ Machine Learning
  └─ Web Development

📁 Personal
  ├─ Creative Writing
  └─ General Questions
```

### Labels

Add color labels to contexts.

**How to:**
1. Right-click context
2. Select "Label"
3. Choose color
4. Label applied

**Use cases:**
- Priority marking
- Status indication
- Category coding
- Visual organization

**Example Labels:**
- 🔴 Urgent
- 🟡 In Progress
- 🟢 Completed
- 🔵 Reference

### Pinning

Pin important contexts to top of list.

**How to:**
1. Right-click context
2. Select "Pin"
3. Context moves to top

**Pinned contexts:**
- Always visible
- Quick access
- Separate section
- Unpin anytime

## 🔍 Search & Filter

### Search Contexts

Find contexts by content or metadata.

**Search Box:**
- Top of context list
- Real-time search
- Highlights matches

**Search by:**
- Message content
- Context name
- Date
- Model used
- Attachments

**Example Searches:**
```
"Python function"  - Find Python discussions
"2026-01"         - Find January 2026 contexts
"GPT-4"           - Find GPT-4 conversations
```

### Filter Contexts

Filter by various criteria.

**Filter Options:**
- Date range
- Model
- Has attachments
- Has code
- Has images
- Pinned only
- Labeled only

**Quick Filters:**
- Today
- This week
- This month
- This year
- Pinned
- Favorites

### Advanced Search

More powerful search options.

**Operators:**
```
AND: python AND function
OR: python OR javascript
NOT: python NOT tutorial
"exact phrase": "hello world"
```

**Fields:**
```
name:project     - Search in name
content:code     - Search in content
model:gpt-4      - Search by model
date:2026-01     - Search by date
```

## 📅 Calendar Integration

### Calendar View

View contexts by date in calendar.

**Location:** `View → Calendar`

**Features:**
- Monthly view
- Daily view
- Context count per day
- Click date to filter
- Visual indicators

**Use cases:**
- Track activity
- Find conversations by date
- Review history
- Plan follow-ups

### Day Notes

Add notes to specific dates.

**How to:**
1. Open calendar
2. Click date
3. Add note
4. Save

**Use cases:**
- Meeting notes
- Daily summaries
- Reminders
- Context annotations

## 💾 Export & Backup

### Export Single Context

Export one conversation.

**Formats:**
- **Markdown** (.md) - Formatted text
- **Plain Text** (.txt) - Simple text
- **PDF** (.pdf) - Document
- **JSON** (.json) - Data format
- **HTML** (.html) - Web page

**How to:**
1. Right-click context
2. Select "Export"
3. Choose format
4. Select location
5. Save

### Export Multiple Contexts

Export several conversations at once.

**How to:**
1. Select contexts (Ctrl + Click)
2. Right-click selection
3. Select "Export Selected"
4. Choose format
5. Save

**Options:**
- Single file (combined)
- Multiple files (separate)
- Archive (ZIP)

### Backup All Contexts

Backup entire conversation database.

**How to:**
```
Tools → Backup → Create Backup
```

**Backup includes:**
- All contexts
- All messages
- Attachments
- Metadata
- Settings

**Backup location:**
- Choose location
- Automatic naming
- Compressed format

### Restore from Backup

Restore previously backed up data.

**How to:**
```
Tools → Backup → Restore Backup
```

**Options:**
- Full restore
- Selective restore
- Merge with existing
- Replace existing

## 🤖 Auto-Summarization

### Context Summaries

AI automatically generates conversation summaries.

**When:**
- After conversation ends
- On context close
- Manually triggered
- Scheduled

**Summary includes:**
- Main topics discussed
- Key points
- Action items
- Conclusions

**Use cases:**
- Quick review
- Search by summary
- Context overview
- Meeting notes

### Enable Auto-Summary

**Settings:**
```
Config → Context → Auto-summarize contexts
```

**Options:**
- After N messages
- On context close
- Manual only
- Never

### View Summaries

**How to:**
1. Right-click context
2. Select "View Summary"
3. Summary displays

**Summary actions:**
- Edit summary
- Regenerate
- Export
- Copy

## 🔧 Advanced Features

### Context Merging

Combine multiple contexts into one.

**How to:**
1. Select contexts to merge
2. Right-click selection
3. Select "Merge Contexts"
4. Choose order
5. Confirm merge

**Use cases:**
- Combine related conversations
- Consolidate project discussions
- Create comprehensive context

### Context Splitting

Split one context into multiple.

**How to:**
1. Open context
2. Select split point
3. Right-click
4. Select "Split Context Here"
5. Two contexts created

**Use cases:**
- Separate topics
- Extract specific discussion
- Organize better

### Context Duplication

Create a copy of a context.

**How to:**
1. Right-click context
2. Select "Duplicate"
3. Copy created

**Use cases:**
- Experiment with variations
- Create templates
- Backup before editing

### Context Templates

Save contexts as reusable templates.

**How to:**
1. Create ideal conversation structure
2. Right-click context
3. Select "Save as Template"
4. Name template

**Use templates:**
1. File → New from Template
2. Select template
3. Context created with structure

## 🐛 Troubleshooting

### Context Not Loading
**Problem:** Context won't open

**Solutions:**
- Check database connection
- Verify context not corrupted
- Try restarting PyGPT
- Check disk space
- Restore from backup

### Search Not Working
**Problem:** Can't find contexts

**Solutions:**
- Rebuild search index
- Check search syntax
- Clear search filters
- Verify database integrity

### Export Failed
**Problem:** Can't export context

**Solutions:**
- Check disk space
- Verify write permissions
- Try different format
- Check file path length

### Lost Contexts
**Problem:** Contexts disappeared

**Solutions:**
- Check filters/search
- Look in different groups
- Check backup
- Verify database file

## 💡 Best Practices

### Naming Conventions

```
✅ "Python Web Scraper Project"
✅ "Client Meeting - 2026-01-15"
✅ "Learning: React Hooks"
❌ "Untitled"
❌ "Chat 1"
❌ "asdf"
```

### Organization

```
✅ Use groups for projects
✅ Label by priority/status
✅ Pin active contexts
✅ Archive completed work
❌ Everything in one list
❌ No organization
```

### Maintenance

```
✅ Regular backups
✅ Delete old/unused contexts
✅ Review and summarize
✅ Export important conversations
❌ Never clean up
❌ No backups
```

### Search Optimization

```
✅ Use descriptive names
✅ Add relevant keywords
✅ Use summaries
✅ Tag appropriately
❌ Generic names
❌ No metadata
```

## 🔗 Related Features

- [Chat Interface](./01-chat.md) - Main chat functionality
- [Presets & Prompts](./07-presets-prompts.md) - Prompt templates
- [Calendar](../reference/calendar.md) - Calendar features

## 📚 Additional Resources

- [Keyboard Shortcuts](../reference/keyboard-shortcuts.md) - Speed up workflow
- [Troubleshooting](../reference/troubleshooting.md) - Common issues
- [FAQ](../faq/general.md) - Frequently asked questions

## 🆘 Need Help?

- Check [FAQ](../faq/general.md)
- Visit [Troubleshooting Guide](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Code Interpreter](./03-code-interpreter.md) →
