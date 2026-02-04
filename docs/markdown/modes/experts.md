# Experts Mode

Multi-agent collaboration with specialized AI experts.

## 👥 Overview

Experts mode enables multiple AI agents to collaborate on complex tasks, each with specialized roles and capabilities. A planner agent coordinates the experts to achieve your goals.

**Key Features:**
- Multiple specialized agents
- Coordinated collaboration
- Role-based expertise
- Parallel task execution
- Comprehensive solutions

**Status:** Production-ready

## 🆚 vs Single Agent

### Experts Mode (Multi-Agent)
- ✅ Multiple specialized agents
- ✅ Coordinated collaboration
- ✅ Parallel task execution
- ✅ Broader expertise
- ✅ Complex problem solving
- ✅ Quality through specialization

### Single Agent Mode
- One generalist agent
- Sequential processing
- Single perspective
- Simpler tasks
- Faster for simple queries

## 🚀 Getting Started

### Prerequisites

1. **API Keys**
   - Configure providers in `Config → Settings → API Keys`
   - Can use different providers for different experts

2. **Supported Models**
   - Any chat-capable model
   - Different models per expert
   - Mix providers as needed

### Enable Experts Mode

1. Launch PyGPT
2. Select mode: **Experts**
3. Configure experts in preset
4. Start your task

## 🎯 Use Cases

### Software Development
```
Experts:
- Architect: System design
- Developer: Code implementation
- Tester: Quality assurance
- Reviewer: Code review

Task: "Build a REST API for user management"
```

### Content Creation
```
Experts:
- Researcher: Gather information
- Writer: Create content
- Editor: Refine and polish
- SEO Specialist: Optimize

Task: "Write a comprehensive blog post about AI trends"
```

### Business Analysis
```
Experts:
- Market Analyst: Market research
- Financial Analyst: Financial modeling
- Strategist: Strategic planning
- Presenter: Report creation

Task: "Analyze market opportunity for new product"
```

### Research Projects
```
Experts:
- Literature Reviewer: Find sources
- Data Analyst: Analyze data
- Statistician: Statistical analysis
- Writer: Synthesize findings

Task: "Research paper on climate change impacts"
```

## ⚙️ Configuration

### Settings Location
`Config → Presets → [Your Preset] → Experts`

### Expert Configuration

Each expert needs:
- **Name** - Expert identifier
- **Role** - Specialization description
- **Model** - AI model to use
- **Provider** - API provider
- **Instructions** - Specific guidelines
- **Tools** - Available capabilities

### Creating an Expert

1. Open preset editor
2. Go to Experts tab
3. Click "Add Expert"
4. Configure expert:
   ```
   Name: Code Reviewer
   Role: Reviews code for quality and best practices
   Model: gpt-4
   Provider: OpenAI
   Instructions: Focus on code quality, security, and maintainability
   Tools: [Enable relevant tools]
   ```
5. Save expert

### Planner Agent

The planner coordinates all experts:
- Analyzes the task
- Assigns work to experts
- Coordinates execution
- Synthesizes results

**Planner Configuration:**
```
Model: gpt-4 (recommended)
Provider: OpenAI
Instructions: Coordinate experts to achieve the goal
```

## 🔧 Expert Types

### Specialist Experts

**Researcher**
- Gathers information
- Finds sources
- Analyzes data
- Provides context

**Developer**
- Writes code
- Implements features
- Fixes bugs
- Optimizes performance

**Analyst**
- Analyzes data
- Identifies patterns
- Makes recommendations
- Creates reports

**Writer**
- Creates content
- Edits text
- Ensures clarity
- Maintains style

### Support Experts

**Reviewer**
- Quality assurance
- Error checking
- Improvement suggestions
- Validation

**Optimizer**
- Performance tuning
- Efficiency improvements
- Resource optimization
- Best practices

**Tester**
- Test creation
- Bug finding
- Validation
- Quality assurance

## 📋 How It Works

### 1. Task Analysis
Planner analyzes your request and breaks it into subtasks.

```
User: "Create a Python web scraper"

Planner Analysis:
- Design scraper architecture
- Implement scraping logic
- Add error handling
- Create tests
- Write documentation
```

### 2. Expert Assignment
Planner assigns subtasks to appropriate experts.

```
Assignments:
- Architect → Design architecture
- Developer → Implement code
- Tester → Create tests
- Writer → Write documentation
```

### 3. Parallel Execution
Experts work on their assigned tasks (when possible).

```
Architect: [Designs system]
Developer: [Waits for design]
Tester: [Prepares test strategy]
Writer: [Prepares doc structure]
```

### 4. Coordination
Planner coordinates dependencies and handoffs.

```
Architect completes → Developer starts
Developer completes → Tester starts
All complete → Writer finalizes docs
```

### 5. Synthesis
Planner combines all expert outputs into final result.

```
Final Output:
- Architecture document
- Working code
- Test suite
- Complete documentation
```

## 🎨 Examples

### Example 1: Software Development
```
User: "Create a REST API for a todo list application"

Planner: "I'll coordinate our experts to build this API"

Architect: "I'll design the API structure:
- Endpoints: GET/POST/PUT/DELETE /todos
- Data model: Todo {id, title, completed, created}
- Authentication: JWT tokens
- Database: PostgreSQL"

Developer: "Implementing the API:
[Provides complete code with Flask/FastAPI]
- Routes defined
- Database models
- Authentication middleware
- Error handling"

Tester: "Creating test suite:
[Provides pytest tests]
- Unit tests for each endpoint
- Integration tests
- Authentication tests
- Edge case coverage"

Writer: "API Documentation:
[Provides README and API docs]
- Setup instructions
- Endpoint documentation
- Example requests
- Deployment guide"

Planner: "Complete! Here's your todo list API with:
✓ Architecture design
✓ Working implementation
✓ Comprehensive tests
✓ Full documentation"
```

### Example 2: Content Creation
```
User: "Write a blog post about AI in healthcare"

Planner: "I'll coordinate our content team"

Researcher: "Key findings:
- AI diagnostics improving accuracy by 30%
- Radiology AI adoption at 60%
- Drug discovery accelerated 10x
- Privacy concerns remain
[Provides sources and data]"

Writer: "Draft article:
[Provides 1500-word article]
- Engaging introduction
- Data-driven content
- Real-world examples
- Balanced perspective"

Editor: "Refined version:
[Provides edited version]
- Improved flow
- Clearer language
- Better transitions
- Stronger conclusion"

SEO Specialist: "Optimizations:
- Keywords: AI healthcare, medical AI, diagnostic AI
- Meta description
- Header structure
- Internal linking suggestions"

Planner: "Complete blog post ready:
✓ Well-researched
✓ Professionally written
✓ Edited and polished
✓ SEO optimized"
```

### Example 3: Business Analysis
```
User: "Analyze the market opportunity for an AI coding assistant"

Planner: "I'll coordinate our analysis team"

Market Analyst: "Market Analysis:
- Market size: $2.5B (2026)
- Growth rate: 35% CAGR
- Key players: GitHub Copilot, Cursor, Tabnine
- Market gaps identified
[Detailed analysis]"

Financial Analyst: "Financial Projections:
- Revenue model: Subscription ($20/month)
- Target: 10K users year 1
- Projected revenue: $2.4M
- Break-even: Month 18
[Detailed financials]"

Strategist: "Strategic Recommendations:
1. Focus on niche: Python developers
2. Differentiation: Better context awareness
3. Pricing: Competitive at $15/month
4. Go-to-market: Developer communities
[Detailed strategy]"

Presenter: "Executive Summary:
[Provides formatted report]
- Market opportunity overview
- Financial projections
- Strategic recommendations
- Next steps"

Planner: "Complete market analysis:
✓ Market research
✓ Financial modeling
✓ Strategic planning
✓ Executive report"
```

## 🐛 Troubleshooting

### Experts Not Collaborating
**Problem:** Experts work independently

**Solutions:**
- Ensure planner is configured
- Check expert instructions
- Verify task requires collaboration
- Review planner model capability

### Slow Execution
**Problem:** Takes too long

**Solutions:**
- Reduce number of experts
- Use faster models
- Simplify task
- Enable parallel execution

### Inconsistent Results
**Problem:** Expert outputs don't align

**Solutions:**
- Improve expert instructions
- Add coordination guidelines
- Use better planner model
- Clarify task requirements

### High API Costs
**Problem:** Expensive to run

**Solutions:**
- Use fewer experts
- Choose cost-effective models
- Optimize expert instructions
- Limit task complexity

## 💡 Best Practices

### Define Clear Roles
```
✅ "Code Reviewer: Focus on security and performance"
✅ "Technical Writer: Create user-friendly documentation"
❌ "Helper: Do stuff"
❌ "Agent: Help with things"
```

### Use Appropriate Models
```
✅ Planner: GPT-4 (needs strong reasoning)
✅ Developer: GPT-4 or Claude (needs code skills)
✅ Writer: GPT-3.5 or Gemini (cost-effective)
❌ All experts: Most expensive model
```

### Provide Context
```
✅ "Create a REST API using FastAPI for a todo app"
✅ "Write a blog post for technical audience about AI"
❌ "Make an API"
❌ "Write something"
```

### Match Experts to Task
```
✅ Complex coding: Architect + Developer + Tester
✅ Simple task: Just Developer
❌ Simple task: 5 experts
```

## 🔗 Related Features

- [Agents & Automation](../features/06-agents-automation.md) - Single agent automation
- [Presets](../features/07-presets-prompts.md) - Configure experts
- [Chat Mode](../guides/01-chat-modes.md) - Single agent chat

## 📚 Additional Resources

- [Multi-Agent Systems](https://en.wikipedia.org/wiki/Multi-agent_system)
- [Agent Collaboration Patterns](../development/architecture.md)
- [Preset Configuration](../features/07-presets-prompts.md)

## ⚠️ Limitations

- **Cost** - Multiple API calls per task
- **Speed** - Slower than single agent
- **Complexity** - Requires good configuration
- **Coordination** - Planner quality matters
- **Overkill** - Not needed for simple tasks

## 💰 Cost Considerations

Experts mode uses more API calls:
- One call per expert
- Planner coordination calls
- Synthesis calls

**Cost-saving tips:**
- Use minimum necessary experts
- Choose cost-effective models
- Optimize expert instructions
- Use for complex tasks only

## 🆘 Need Help?

- Check [Agents Guide](../features/06-agents-automation.md)
- Visit [Presets Guide](../features/07-presets-prompts.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Agents Builder](./agents-builder.md) →
