# Agents Builder

Visual node-based editor for designing agent workflows.

## 🎨 Overview

Agents Builder is a visual tool for creating custom agent workflows using a node-based interface. Design complex agent behaviors by connecting nodes that represent actions, decisions, and data flow.

**Key Features:**
- Visual workflow design
- Drag-and-drop interface
- Node-based logic
- Custom agent flows
- Real-time testing
- Export/import workflows

**Status:** Beta  
**Location:** `Tools → Agents Builder`

## 🆚 vs Traditional Agents

### Agents Builder (Visual)
- ✅ Visual workflow design
- ✅ No coding required
- ✅ Easy to understand
- ✅ Quick prototyping
- ✅ Reusable workflows
- ✅ Visual debugging

### Traditional Agents (Code)
- Requires coding
- Text-based configuration
- Harder to visualize
- More flexible
- Better for complex logic

## 🚀 Getting Started

### Prerequisites

1. **PyGPT Installed**
   - Version 2.6.60 or later

2. **Basic Understanding**
   - Agent concepts
   - Workflow logic
   - Node connections

### Open Agents Builder

1. Launch PyGPT
2. Menu: `Tools → Agents Builder`
3. New canvas opens
4. Start building!

## 🎯 Use Cases

### Task Automation
```
Design workflows for:
- File processing pipelines
- Data transformation
- Report generation
- Scheduled tasks
```

### Decision Trees
```
Create decision logic:
- Conditional branching
- Multi-step decisions
- Error handling
- Fallback paths
```

### Multi-Step Processes
```
Build complex processes:
- Research → Analyze → Report
- Gather → Process → Store
- Input → Validate → Execute
```

### Agent Behaviors
```
Define agent behaviors:
- How to handle errors
- When to ask for help
- What tools to use
- How to respond
```

## 🧩 Node Types

### Input Nodes

**User Input**
- Receives user message
- Starting point
- One per workflow

**File Input**
- Reads file content
- Supports multiple formats
- Passes to next node

**Data Input**
- Static data
- Configuration values
- Constants

### Processing Nodes

**LLM Call**
- Calls AI model
- Processes text
- Generates responses

**Transform**
- Modifies data
- Applies functions
- Formats output

**Filter**
- Filters data
- Applies conditions
- Removes items

**Aggregate**
- Combines data
- Summarizes
- Calculates

### Decision Nodes

**Condition**
- If/else logic
- Multiple branches
- Boolean evaluation

**Switch**
- Multiple paths
- Value matching
- Default case

**Loop**
- Iterate over data
- Repeat actions
- Break conditions

### Action Nodes

**Tool Call**
- Executes tool
- Passes parameters
- Returns result

**Command**
- Runs command
- System execution
- Captures output

**API Call**
- HTTP requests
- External APIs
- Data fetching

**File Write**
- Saves to file
- Multiple formats
- Append/overwrite

### Output Nodes

**Response**
- Returns to user
- Final output
- End point

**Store**
- Saves to database
- Persistent storage
- Context memory

**Log**
- Logs information
- Debugging
- Audit trail

## 📋 Building a Workflow

### Step 1: Add Nodes

1. **Open Node Palette**
   - Left sidebar
   - Categorized nodes
   - Search available

2. **Drag Node to Canvas**
   - Click and drag
   - Drop on canvas
   - Node appears

3. **Configure Node**
   - Double-click node
   - Set properties
   - Save changes

### Step 2: Connect Nodes

1. **Click Output Port**
   - Small circle on right
   - Drag to create connection

2. **Connect to Input Port**
   - Drop on target node
   - Connection created
   - Data flows

3. **Multiple Connections**
   - One output → many inputs
   - Branching logic
   - Parallel processing

### Step 3: Configure Flow

1. **Set Node Properties**
   - Model selection
   - Prompts
   - Parameters
   - Conditions

2. **Add Error Handling**
   - Error output ports
   - Fallback paths
   - Retry logic

3. **Test Flow**
   - Run button
   - Test inputs
   - Check outputs

### Step 4: Save & Use

1. **Save Workflow**
   - File → Save
   - Name workflow
   - Export option

2. **Use in Agent**
   - Load in Agents mode
   - Assign to preset
   - Execute workflow

## 🎨 Example Workflows

### Example 1: Research Assistant

```
[User Input]
    ↓
[Extract Topic] (LLM)
    ↓
[Web Search] (Tool)
    ↓
[Analyze Results] (LLM)
    ↓
[Format Report] (Transform)
    ↓
[Response]
```

**Nodes:**
1. User Input: Receives research query
2. Extract Topic: LLM extracts key topic
3. Web Search: Searches web for information
4. Analyze Results: LLM analyzes findings
5. Format Report: Formats as markdown
6. Response: Returns to user

### Example 2: Code Review Pipeline

```
[File Input]
    ↓
[Check Language] (Condition)
    ├─ Python → [Python Linter]
    ├─ JavaScript → [ESLint]
    └─ Other → [Generic Review]
    ↓
[LLM Review] (LLM)
    ↓
[Generate Report] (Transform)
    ↓
[Response]
```

**Nodes:**
1. File Input: Reads code file
2. Check Language: Detects language
3. Language-specific linters: Run appropriate linter
4. LLM Review: AI reviews code
5. Generate Report: Creates review report
6. Response: Returns review

### Example 3: Data Processing

```
[File Input]
    ↓
[Parse CSV] (Transform)
    ↓
[Filter Rows] (Filter)
    ↓
[Loop Each Row] (Loop)
    ├─ [Process Row] (LLM)
    ├─ [Validate] (Condition)
    └─ [Store Result] (Store)
    ↓
[Aggregate Results] (Aggregate)
    ↓
[Generate Summary] (LLM)
    ↓
[Response]
```

**Nodes:**
1. File Input: Reads CSV file
2. Parse CSV: Converts to data structure
3. Filter Rows: Removes invalid rows
4. Loop Each Row: Iterates over data
5. Process Row: LLM processes each row
6. Validate: Checks result validity
7. Store Result: Saves to database
8. Aggregate Results: Combines all results
9. Generate Summary: LLM creates summary
10. Response: Returns summary

## 🔧 Advanced Features

### Variables

Store and reuse data across nodes.

**Create Variable:**
```
Node: Set Variable
Name: user_name
Value: {input.name}
```

**Use Variable:**
```
Node: LLM Call
Prompt: "Hello {var.user_name}"
```

### Conditional Logic

Branch based on conditions.

**Condition Node:**
```
Condition: {data.score} > 80
True → [High Score Path]
False → [Low Score Path]
```

### Loops

Iterate over collections.

**Loop Node:**
```
Input: {data.items}
For Each: item
  → [Process Item]
  → [Store Result]
End Loop
```

### Error Handling

Handle errors gracefully.

**Try-Catch Pattern:**
```
[Action Node]
  Success → [Continue]
  Error → [Error Handler]
    → [Log Error]
    → [Retry] or [Fallback]
```

### Parallel Execution

Run multiple paths simultaneously.

**Parallel Pattern:**
```
[Input]
  ├─ [Path A] → [Result A]
  ├─ [Path B] → [Result B]
  └─ [Path C] → [Result C]
    ↓
[Merge Results]
```

## 🎨 Canvas Controls

### Navigation

**Pan**
- Click and drag canvas
- Or middle mouse button

**Zoom**
- Mouse wheel
- Ctrl + Plus/Minus
- Zoom controls

**Fit to View**
- View → Fit All
- Shows entire workflow

### Selection

**Select Node**
- Click node
- Shows properties

**Multi-Select**
- Ctrl + Click
- Drag selection box

**Select All**
- Ctrl + A

### Editing

**Copy/Paste**
- Ctrl + C / Ctrl + V
- Duplicates nodes

**Delete**
- Select + Delete key
- Or right-click → Delete

**Undo/Redo**
- Ctrl + Z / Ctrl + Y
- History maintained

## 🐛 Troubleshooting

### Nodes Not Connecting
**Problem:** Can't create connection

**Solutions:**
- Check port types match
- Ensure valid connection
- Try different ports
- Restart builder

### Workflow Not Running
**Problem:** Execution fails

**Solutions:**
- Check all nodes configured
- Verify connections complete
- Test individual nodes
- Check error logs

### Missing Nodes
**Problem:** Can't find node type

**Solutions:**
- Update PyGPT
- Check node palette
- Search by name
- Verify installation

### Performance Issues
**Problem:** Slow or laggy

**Solutions:**
- Simplify workflow
- Reduce node count
- Close other applications
- Restart PyGPT

## 💡 Best Practices

### Keep It Simple
```
✅ Clear, linear flows
✅ Logical grouping
✅ Minimal complexity
❌ Spaghetti connections
❌ Too many branches
```

### Use Descriptive Names
```
✅ "Extract User Email"
✅ "Validate Input Data"
❌ "Node 1"
❌ "Process"
```

### Add Comments
```
✅ Comment nodes for clarity
✅ Explain complex logic
✅ Document assumptions
```

### Test Incrementally
```
✅ Test each node
✅ Verify connections
✅ Check outputs
❌ Build entire flow first
```

### Handle Errors
```
✅ Add error paths
✅ Provide fallbacks
✅ Log failures
❌ Assume success
```

## 🔗 Related Features

- [Agents & Automation](../features/06-agents-automation.md) - Agent basics
- [Experts Mode](../modes/experts.md) - Multi-agent collaboration
- [Custom Commands](../features/08-custom-commands.md) - Custom tools

## 📚 Additional Resources

- [Node-Based Programming](https://en.wikipedia.org/wiki/Node_graph_architecture)
- [Visual Programming](https://en.wikipedia.org/wiki/Visual_programming_language)
- [Workflow Automation](../features/06-agents-automation.md)

## ⚠️ Limitations

- **Beta status** - May have bugs
- **Performance** - Large workflows may be slow
- **Complexity** - Very complex logic difficult
- **Learning curve** - Requires understanding of nodes
- **Export** - Limited export formats

## 🆘 Need Help?

- Check [Agents Guide](../features/06-agents-automation.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Painter Tool](./painter.md) →
