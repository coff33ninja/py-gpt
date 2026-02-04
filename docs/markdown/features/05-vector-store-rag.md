# Vector Store & RAG

Document retrieval and Retrieval-Augmented Generation.

## 🗄️ Overview

Vector Store & RAG (Retrieval-Augmented Generation) enables AI to access and use information from your documents, creating a knowledge base that enhances responses with relevant context.

**Key Features:**
- Document embedding
- Semantic search
- Multiple vector stores
- RAG integration
- Context retrieval
- Knowledge base management

**Integration:** LlamaIndex (built-in)

## 🚀 Getting Started

### What is RAG?

**RAG = Retrieval-Augmented Generation**

1. **Store** documents in vector database
2. **Embed** text as numerical vectors
3. **Search** semantically similar content
4. **Retrieve** relevant passages
5. **Augment** AI prompt with context
6. **Generate** informed response

**Benefits:**
- Access to your documents
- Up-to-date information
- Accurate responses
- Source citations
- No retraining needed

### Enable RAG

1. **Select Mode**
   ```
   Mode: Chat with Files
   ```

2. **Add Documents**
   ```
   Data → Upload files
   Or: Copy to data/ folder
   ```

3. **Index Documents**
   ```
   Right-click file → Index
   Or: Index All button
   ```

4. **Start Chatting**
   - Ask about your documents
   - AI retrieves relevant context
   - Responses based on your data

### Your First RAG Query

```
[Upload company_policy.pdf]
[Index the file]

You: What is our vacation policy?

AI: [Retrieves relevant sections from PDF]

According to your company policy document:
- Employees receive 15 days paid vacation
- Must be requested 2 weeks in advance
- Unused days don't roll over

[Source: company_policy.pdf, page 12]
```

## 🎯 Use Cases

### Document Q&A
```
Upload: Technical documentation
Query: "How do I configure the API?"
Result: Step-by-step instructions from docs
```

### Research Assistant
```
Upload: Research papers
Query: "Summarize findings on topic X"
Result: Synthesis of relevant papers
```

### Code Documentation
```
Upload: Codebase files
Query: "How does the authentication work?"
Result: Explanation based on actual code
```

### Knowledge Base
```
Upload: Company wiki, policies, guides
Query: "What's the expense reimbursement process?"
Result: Accurate answer from company docs
```

### Legal/Compliance
```
Upload: Contracts, regulations
Query: "What are our data retention requirements?"
Result: Specific clauses and requirements
```

## ⚙️ Configuration

### Settings Location
`Config → Settings → Indexes / LlamaIndex`

### Vector Store Selection

**Available Stores:**

**SimpleVectorStore** (Default)
- Local file-based
- No setup required
- Good for small datasets
- Fast for < 10K documents

**ChromaDB**
- Open-source
- Good performance
- Local or remote
- Persistent storage

**Pinecone**
- Cloud-based
- Scalable
- Fast queries
- Requires API key

**Qdrant**
- Open-source
- High performance
- Self-hosted or cloud
- Advanced filtering

**Redis**
- In-memory
- Very fast
- Requires Redis server
- Good for caching

**Elasticsearch**
- Enterprise-grade
- Full-text + vector search
- Scalable
- Complex setup

**Configuration:**
```
Vector Store: SimpleVectorStore
Storage Path: ~/.pygpt/index
Embedding Model: text-embedding-3-small
```

### Embedding Models

**OpenAI Embeddings:**
```
Model: text-embedding-3-small
Dimensions: 1536
Cost: $0.02 per 1M tokens
```

**OpenAI Embeddings (Large):**
```
Model: text-embedding-3-large
Dimensions: 3072
Cost: $0.13 per 1M tokens
Better quality
```

**Local Embeddings:**
```
Model: sentence-transformers
Free
Slower
No API needed
```

**Other Providers:**
- Google (Gemini)
- Anthropic (Claude)
- HuggingFace
- Ollama (local)

### Indexing Settings

**Chunk Size:**
```
Size: 512-2048 tokens
Default: 1024
Smaller = more precise
Larger = more context
```

**Chunk Overlap:**
```
Overlap: 0-200 tokens
Default: 20
Prevents context loss
```

**Metadata:**
```
Include: filename, date, author
Helps filtering
Improves retrieval
```

## 🔧 Features

### Document Indexing

**Supported Formats:**
- **Text:** TXT, MD, CSV
- **Documents:** PDF, DOCX, XLSX
- **Code:** PY, JS, Java, etc.
- **Web:** HTML, XML
- **Data:** JSON, YAML
- **Books:** EPUB

**Indexing Process:**
1. Upload/add document
2. Extract text
3. Split into chunks
4. Generate embeddings
5. Store in vector database

**Bulk Indexing:**
```
Select multiple files
Right-click → Index Selected
Or: Index All button
```

### Semantic Search

**How it Works:**
1. Convert query to vector
2. Find similar vectors
3. Retrieve matching chunks
4. Rank by relevance
5. Return top results

**Example:**
```
Query: "machine learning algorithms"

Matches:
- "neural networks and deep learning"
- "supervised learning techniques"
- "classification and regression models"

(Even without exact keyword match!)
```

### Context Retrieval

**Automatic Retrieval:**
- AI query triggers search
- Relevant chunks retrieved
- Added to prompt context
- AI generates response

**Manual Retrieval:**
```
Tools → Query Index
Enter query
View results
```

**Retrieval Settings:**
```
Top K: 3-10 chunks
Default: 5
More = more context, slower
```

### Source Citations

**Automatic Citations:**
```
AI: "According to your documentation [1], 
the API requires authentication..."

[1] api_docs.pdf, page 15
```

**Citation Formats:**
- Inline references
- Footnotes
- Source list
- Page numbers

### Metadata Filtering

**Filter by:**
- File type
- Date range
- Author
- Tags
- Custom metadata

**Example:**
```
Query: "API authentication"
Filter: file_type=pdf, date>2025-01-01
Result: Only recent PDF docs
```

### Index Management

**View Index:**
```
Tools → Index Manager
- See all indexed documents
- View statistics
- Manage entries
```

**Update Index:**
```
Right-click file → Re-index
Updates existing entry
Preserves metadata
```

**Delete from Index:**
```
Right-click file → Remove from Index
Deletes embeddings
Keeps original file
```

**Clear Index:**
```
Tools → Index Manager → Clear All
Removes all embeddings
Fresh start
```

## 🎨 Advanced Features

### Hybrid Search

Combine vector and keyword search.

**Benefits:**
- Better accuracy
- Handles exact matches
- Semantic understanding
- Flexible queries

**Configuration:**
```
Enable Hybrid Search: Yes
Vector Weight: 0.7
Keyword Weight: 0.3
```

### Query Modes

**Standard Mode:**
- Simple Q&A
- Single query
- Direct answers

**Chat Mode:**
- Conversational
- Follow-up questions
- Context maintained

**Summarize Mode:**
- Document summaries
- Key points extraction
- Overview generation

**Compare Mode:**
- Compare documents
- Find differences
- Highlight similarities

### Context Window Management

**Auto-context:**
```
Enable: Yes
Max chunks: 5
Auto-retrieve relevant context
```

**Manual context:**
```
Attach specific documents
Control what AI sees
Precise context
```

### Multi-Index Support

**Multiple Indexes:**
```
Index 1: Technical docs
Index 2: Business docs
Index 3: Code files
```

**Query Specific Index:**
```
"Search technical docs for API info"
"Query business docs for policy"
```

### Real-Time Indexing

**Auto-index:**
```
Watch folder: ~/documents
Auto-index new files
Keep index updated
```

**Incremental Updates:**
```
Only index changes
Faster updates
Efficient storage
```

## 🐛 Troubleshooting

### Indexing Failed
**Problem:** Can't index document

**Solutions:**
- Check file format supported
- Verify file not corrupted
- Check disk space
- Review error message
- Try re-indexing

### Poor Retrieval Quality
**Problem:** Irrelevant results

**Solutions:**
- Adjust chunk size
- Increase top K
- Try different embedding model
- Improve query phrasing
- Add metadata filters

### Slow Queries
**Problem:** Searches take too long

**Solutions:**
- Use faster vector store
- Reduce top K
- Optimize chunk size
- Use local embeddings
- Upgrade hardware

### High API Costs
**Problem:** Expensive embeddings

**Solutions:**
- Use smaller embedding model
- Reduce chunk overlap
- Index selectively
- Use local embeddings
- Batch operations

### Index Corruption
**Problem:** Index not working

**Solutions:**
- Rebuild index
- Clear and re-index
- Check storage path
- Verify permissions
- Restore from backup

## 💡 Best Practices

### Document Preparation

```
✅ Clean, well-formatted documents
✅ Remove unnecessary content
✅ Consistent formatting
✅ Meaningful filenames
❌ Scanned images without OCR
❌ Poorly formatted text
```

### Chunk Size Selection

```
✅ Technical docs: 512-1024 tokens
✅ Long-form content: 1024-2048 tokens
✅ Code files: 256-512 tokens
❌ One size fits all
```

### Query Optimization

```
✅ "Explain the authentication process in the API"
✅ "What are the requirements for data retention?"
❌ "auth"
❌ "stuff about data"
```

### Index Maintenance

```
✅ Regular updates
✅ Remove outdated docs
✅ Rebuild periodically
✅ Monitor performance
❌ Never update
❌ Accumulate old data
```

## 🔗 Related Features

- [Chat with Files Mode](../guides/01-chat-modes.md) - RAG mode
- [File Operations](../guides/03-working-with-files.md) - File handling
- [Agents](./06-agents-automation.md) - Automated RAG

## 📚 Additional Resources

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Vector Databases Explained](https://www.pinecone.io/learn/vector-database/)
- [RAG Best Practices](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/)

## ⚠️ Limitations

- **Embedding costs** - API charges apply
- **Storage space** - Vectors require disk space
- **Processing time** - Large documents take time
- **Context limits** - Model token limits apply
- **Quality depends** - On document quality

## 💰 Cost Considerations

**Embedding Costs:**
```
OpenAI text-embedding-3-small:
- $0.02 per 1M tokens
- 1000-page book ≈ $0.50

OpenAI text-embedding-3-large:
- $0.13 per 1M tokens
- 1000-page book ≈ $3.25
```

**Storage Costs:**
```
Local: Free (disk space)
Pinecone: $70/month (starter)
Qdrant Cloud: $25/month (starter)
```

**Cost-Saving Tips:**
- Use local embeddings
- Optimize chunk size
- Index selectively
- Use SimpleVectorStore
- Batch operations

## 🆘 Need Help?

- Check [Chat with Files Guide](../guides/01-chat-modes.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Agents & Automation](./06-agents-automation.md) →
