# Agents & Automation

Autonomous task execution and workflow automation.

## 🤖 Overview

Agents enable AI to autonomously execute multi-step tasks, use tools, make decisions, and achieve goals without constant human intervention.

**Key Features:**
- Autonomous task execution
- Multi-step planning
- Tool usage
- Error recovery
- Progress tracking
- Goal achievement

**Modes:** Agents (LlamaIndex), Agent (OpenAI), Autonomous

## 🚀 Getting Started

### What are Agents?

**Traditional Chat:**
```
You: "Search for Python tutorials"
AI: [Provides answer]
Done.
```

**Agent:**
```
You: "Research Python tutorials and create a learning plan"
Agent:
1. Plans approach
2. Searches web
3. Analyzes results
4. Organizes information
5. Creates structured plan
6. Presents final result
```

### Enable Agents

**LlamaIndex Agents:**
```
Mode: Agents (LlamaIndex)
Agent Type: ReAct / Function Calling / CodeAct
```

**OpenAI Agents:**
```
Mode: Agent (OpenAI)
Agent Type: Evolve / Researcher / Planner
```

**Autonomous Mode:**
```
Mode: Autonomous
Enable: Agent (autonomous) plugin
```

### Your First Agent Task

```
You: "Research the top 5 Python web frameworks and 
      create a comparison table"

Agent:
[Step 1] Planning research strategy...
[Step 2] Searching for Python web frameworks...
[Step 3] Found: Django, Flask, FastAPI, Pyramid, Tornado
[Step 4] Gathering details for each...
[Step 5] Analyzing features...
[Step 6] Creating comparison table...

Result: [Detailed comparison table with sources]
```

## 🎯 Use Cases

### Research & Analysis
```
"Research AI trends in 2026 and write a summary report"
"Analyze this dataset and create visualizations"
"Compare different cloud providers and recommend one"
```

### Content Creation
```
"Research topic X and write a blog post"
"Create a presentation about Y with sources"
"Generate a comprehensive guide on Z"
```

### Data Processing
```
"Process these CSV files and generate insights"
"Clean this dataset and create a report"
"Analyze sales data and identify trends"
```

### Software Development
```
"Create a REST API for user management"
"Build a web scraper for news articles"
"Develop a data pipeline with error handling"
```

### Automation
```
"Monitor news about topic X and summarize daily"
"Check these websites for updates"
"Generate weekly reports from data"
```

## ⚙️ Configuration

### Settings Location
`Config → Settings → Agents`

### Agent Types

**ReAct Agent (LlamaIndex)**
- Reasoning + Acting
- Step-by-step thinking
- Tool selection
- Good for complex tasks

**Function Calling Agent (LlamaIndex)**
- Direct function calls
- Faster execution
- Less reasoning
- Good for simple tasks

**CodeAct Agent (LlamaIndex)**
- Code-based actions
- Python execution
- Data analysis
- Good for technical tasks

**Evolve Agent (OpenAI)**
- Self-improving
- Learns from feedback
- Adaptive behavior
- Experimental

**Researcher Agent (OpenAI)**
- Deep research
- Multi-source analysis
- Comprehensive reports
- Academic quality

**Planner Agent (OpenAI)**
- Strategic planning
- Goal decomposition
- Resource allocation
- Project management

### Agent Settings

**Max Steps:**
```
Steps: 10-100
Default: 50
More steps = more complex tasks
```

**Timeout:**
```
Timeout: 60-600 seconds
Default: 300
Longer for complex tasks
```

**Tools:**
```
Enable/disable specific tools:
- Web search
- File operations
- Code execution
- API calls
- Custom tools
```

**Evaluation:**
```
Enable response evaluation: Yes/No
Evaluation mode: Completion / Accuracy
Improves quality
```

## 🔧 Agent Workflows

### Planning Phase

**Goal Analysis:**
1. Understand objective
2. Break into subtasks
3. Identify required tools
4. Plan execution order

**Example:**
```
Goal: "Create a market analysis report"

Plan:
1. Research market size
2. Identify key players
3. Analyze trends
4. Gather financial data
5. Create visualizations
6. Write report
```

### Execution Phase

**Step-by-Step:**
1. Execute first step
2. Evaluate result
3. Adjust plan if needed
4. Execute next step
5. Repeat until complete

**Example:**
```
[Step 1/6] Researching market size...
✓ Found: $2.5B market

[Step 2/6] Identifying key players...
✓ Found: 5 major companies

[Step 3/6] Analyzing trends...
✓ Growth rate: 25% YoY

...
```

### Tool Usage

**Available Tools:**
- Web search
- File I/O
- Code execution
- API calls
- Database queries
- System commands
- Custom tools

**Tool Selection:**
```
Agent analyzes task
Selects appropriate tool
Executes tool
Processes result
Continues workflow
```

### Error Recovery

**Automatic Recovery:**
```
Error detected
↓
Analyze error
↓
Try alternative approach
↓
If fails, try another
↓
Report if all fail
```

**Example:**
```
[Step 3] Searching web...
✗ Error: API quota exceeded

[Recovery] Trying alternative search provider...
✓ Success with DuckDuckGo
```

## 🎨 Advanced Features

### Multi-Agent Collaboration

**Experts Mode:**
```
Multiple specialized agents
Coordinated by planner
Parallel execution
Combined results
```

**Example:**
```
Task: "Build a web application"

Agents:
- Architect: Designs system
- Developer: Writes code
- Tester: Creates tests
- Writer: Documents code

Planner coordinates all agents
```

### Autonomous Mode

**Continuous Operation:**
```
Set goal
Agent works autonomously
Minimal human intervention
Reports progress
Achieves goal
```

**Features:**
- Self-directed
- Adaptive planning
- Resource management
- Progress tracking

**Use Cases:**
- Long-running tasks
- Background processing
- Scheduled operations
- Monitoring tasks

### Agent Evaluation

**Quality Assessment:**
```
After each step:
1. Evaluate completion
2. Check accuracy
3. Score performance
4. Adjust if needed
```

**Evaluation Modes:**

**Completion:**
```
0-100% complete
Tracks progress
Ensures goal achieved
```

**Accuracy:**
```
Checks correctness
Validates results
Ensures quality
```

### Agent Memory

**Short-term Memory:**
- Current task context
- Recent actions
- Intermediate results
- Active variables

**Long-term Memory:**
- Past tasks
- Learned patterns
- Successful strategies
- Error history

**Context Persistence:**
```
Agent remembers:
- Previous conversations
- Past solutions
- User preferences
- Domain knowledge
```

### Custom Agents

**Create Custom Agent:**
```
1. Define role
2. Set capabilities
3. Configure tools
4. Add instructions
5. Test and refine
```

**Example:**
```
Name: Data Analyst Agent
Role: Analyze data and create reports
Tools: Code execution, file I/O, visualization
Instructions: Focus on insights and trends
```

## 🐛 Troubleshooting

### Agent Not Starting
**Problem:** Agent won't begin task

**Solutions:**
- Check agent mode selected
- Verify tools enabled
- Check API keys valid
- Review error messages
- Restart PyGPT

### Agent Stuck
**Problem:** Agent stops progressing

**Solutions:**
- Check max steps not reached
- Verify timeout not exceeded
- Review last action
- Stop and restart
- Simplify task

### Poor Results
**Problem:** Agent produces bad output

**Solutions:**
- Enable evaluation mode
- Increase max steps
- Provide clearer instructions
- Use better model
- Add more tools

### High API Costs
**Problem:** Expensive agent runs

**Solutions:**
- Reduce max steps
- Use cheaper models
- Disable unnecessary tools
- Optimize prompts
- Monitor usage

### Tool Errors
**Problem:** Tools failing

**Solutions:**
- Check tool configuration
- Verify API keys
- Test tools individually
- Review permissions
- Check error logs

## 💡 Best Practices

### Clear Goals

```
❌ "Do something with data"
✅ "Analyze sales_data.csv and create a report 
    showing monthly trends and top products"

❌ "Research AI"
✅ "Research latest AI developments in 2026, 
    focusing on LLMs, and create a summary 
    with sources"
```

### Appropriate Complexity

```
✅ Simple task → Function Calling agent
✅ Complex task → ReAct agent
✅ Code task → CodeAct agent
✅ Research → Researcher agent
❌ Simple task → Complex agent (overkill)
```

### Tool Selection

```
✅ Enable only needed tools
✅ Configure tools properly
✅ Test tools before agent run
❌ Enable all tools always
❌ Unconfigured tools
```

### Monitoring

```
✅ Watch agent progress
✅ Review intermediate results
✅ Stop if going wrong direction
✅ Learn from failures
❌ Set and forget
❌ Ignore errors
```

## 🔗 Related Features

- [Experts Mode](../modes/experts.md) - Multi-agent collaboration
- [Agents Builder](../tools/agents-builder.md) - Visual agent design
- [Code Interpreter](./03-code-interpreter.md) - Code execution
- [Web Search](./04-web-search.md) - Information retrieval

## 📚 Additional Resources

- [LlamaIndex Agents](https://docs.llamaindex.ai/en/stable/module_guides/deploying/agents/)
- [OpenAI Agents](https://platform.openai.com/docs/guides/agents)
- [Agent Design Patterns](https://www.anthropic.com/research/building-effective-agents)

## ⚠️ Limitations

- **Cost** - Multiple API calls
- **Speed** - Slower than direct chat
- **Reliability** - May fail on complex tasks
- **Control** - Less direct control
- **Debugging** - Harder to troubleshoot

## 💰 Cost Considerations

**Agent runs typically cost more:**
- Multiple model calls
- Tool usage costs
- Longer context
- Evaluation calls

**Example Costs:**
```
Simple task: $0.01-0.05
Medium task: $0.05-0.25
Complex task: $0.25-1.00+
```

**Cost-Saving Tips:**
- Use cheaper models
- Limit max steps
- Disable evaluation
- Optimize prompts
- Monitor usage

## 🆘 Need Help?

- Check [Experts Mode](../modes/experts.md)
- Visit [Agents Builder](../tools/agents-builder.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Presets & Prompts](./07-presets-prompts.md) →
