# Presets & Prompts

Create and manage reusable prompt templates.

## 📝 Overview

Presets allow you to save and reuse system prompts, model configurations, and agent setups. Create specialized AI assistants for different tasks without reconfiguring each time.

**Key Features:**
- Save prompt templates
- Model configurations
- Agent setups
- Quick switching
- Import/export
- Sharing presets

## 🚀 Getting Started

### What are Presets?

**Preset = Configuration Package**

Includes:
- System prompt
- Model selection
- Temperature/parameters
- Agent configuration
- Tool settings
- Expert definitions

**Benefits:**
- Consistency
- Time-saving
- Reusability
- Specialization
- Easy switching

### Using Presets

**Select Preset:**
```
Preset dropdown (top-right)
↓
Choose preset
↓
Configuration applied
↓
Start chatting
```

**Default Presets:**
- Default
- Code Assistant
- Creative Writer
- Technical Expert
- Translator
- Analyst

### Your First Custom Preset

```
1. Click "New Preset" button
2. Name: "Python Tutor"
3. System Prompt: "You are an expert Python teacher..."
4. Model: GPT-4
5. Temperature: 0.7
6. Save

Now you have a specialized Python tutor!
```

## 🎯 Use Cases

### Role-Based Assistants
```
Preset: "Business Analyst"
Prompt: "You are a business analyst specializing 
         in market research and data analysis..."
Use: Business queries and analysis
```

### Task-Specific Helpers
```
Preset: "Code Reviewer"
Prompt: "Review code for quality, security, 
         and best practices..."
Use: Code review tasks
```

### Language/Style Variants
```
Preset: "Casual Chat"
Prompt: "Respond in a friendly, casual tone..."

Preset: "Formal Writing"
Prompt: "Use formal, professional language..."
```

### Domain Experts
```
Preset: "Legal Assistant"
Prompt: "You are a legal expert specializing in..."

Preset: "Medical Advisor"
Prompt: "You are a medical professional..."
```

## ⚙️ Configuration

### Preset Editor

**Access:**
```
Config → Presets
Or: Click preset name → Edit
```

### Basic Settings

**Name:**
```
Preset name: "Python Expert"
Description: "Expert Python developer and teacher"
```

**System Prompt:**
```
You are an expert Python developer with 10+ years 
of experience. You specialize in:
- Clean code practices
- Performance optimization
- Best practices
- Teaching and mentoring

Always provide:
- Clear explanations
- Code examples
- Best practices
- Common pitfalls to avoid
```

**Model:**
```
Model: GPT-4
Provider: OpenAI
Fallback: GPT-3.5-turbo
```

### Advanced Settings

**Temperature:**
```
Range: 0.0 - 2.0
Default: 0.7

0.0 = Deterministic, focused
0.7 = Balanced
1.5+ = Creative, varied
```

**Max Tokens:**
```
Response length limit
Default: 2048
Range: 1-32000 (model dependent)
```

**Top P:**
```
Nucleus sampling
Range: 0.0 - 1.0
Default: 1.0
Lower = more focused
```

**Frequency Penalty:**
```
Reduce repetition
Range: -2.0 to 2.0
Default: 0.0
Positive = less repetition
```

**Presence Penalty:**
```
Encourage new topics
Range: -2.0 to 2.0
Default: 0.0
Positive = more variety
```

### Agent Configuration

**Enable Agents:**
```
Use agents: Yes/No
Agent type: ReAct / Function Calling / CodeAct
Max steps: 50
```

**Tools:**
```
Enable tools:
☑ Web search
☑ File operations
☑ Code execution
☐ System commands
```

**Experts:**
```
Add expert agents:
- Expert 1: Researcher
- Expert 2: Analyst
- Expert 3: Writer
```

## 🎨 Preset Examples

### Code Assistant

```yaml
Name: Code Assistant
Model: GPT-4
Temperature: 0.3

System Prompt:
You are an expert programmer proficient in multiple 
languages. Provide:
- Clean, well-commented code
- Best practices
- Error handling
- Performance considerations

Always explain your code and suggest improvements.

Tools: Code execution, File I/O
```

### Creative Writer

```yaml
Name: Creative Writer
Model: GPT-4
Temperature: 1.2

System Prompt:
You are a creative writer specializing in fiction, 
poetry, and storytelling. Your writing is:
- Imaginative and original
- Emotionally engaging
- Well-structured
- Vivid and descriptive

Help users develop their creative ideas.

Tools: None
```

### Data Analyst

```yaml
Name: Data Analyst
Model: GPT-4
Temperature: 0.5

System Prompt:
You are a data analyst expert in:
- Statistical analysis
- Data visualization
- Pattern recognition
- Insight generation

Provide clear, actionable insights from data.

Tools: Code execution, File I/O, Web search
Agents: Enabled (CodeAct)
```

### Research Assistant

```yaml
Name: Research Assistant
Model: GPT-4
Temperature: 0.7

System Prompt:
You are a research assistant skilled in:
- Information gathering
- Source evaluation
- Synthesis
- Citation

Provide well-researched, cited information.

Tools: Web search, File I/O
Agents: Enabled (Researcher)
```

### Language Tutor

```yaml
Name: Spanish Tutor
Model: GPT-3.5-turbo
Temperature: 0.8

System Prompt:
You are a patient Spanish language tutor. You:
- Explain grammar clearly
- Provide examples
- Correct mistakes gently
- Encourage practice

Always respond in Spanish unless asked otherwise.

Tools: None
```

## 🔧 Advanced Features

### Preset Inheritance

**Base Preset:**
```
Name: Base Assistant
Prompt: Common instructions
Settings: Default values
```

**Derived Presets:**
```
Python Expert → extends Base Assistant
  + Python-specific instructions
  
JavaScript Expert → extends Base Assistant
  + JavaScript-specific instructions
```

### Dynamic Prompts

**Variables:**
```
System Prompt:
You are a {role} specializing in {domain}.
Current date: {date}
User name: {user_name}
```

**Filled at runtime:**
```
role = "developer"
domain = "web development"
date = "2026-02-04"
user_name = "John"
```

### Conditional Logic

**If-Then Prompts:**
```
If user asks about code:
  → Use technical language
  → Provide code examples
  
If user asks about concepts:
  → Use simple language
  → Provide analogies
```

### Preset Chains

**Multi-Step Presets:**
```
Step 1: Research preset
  → Gather information
  
Step 2: Analysis preset
  → Analyze findings
  
Step 3: Writing preset
  → Create report
```

## 💾 Import/Export

### Export Preset

**Single Preset:**
```
Right-click preset → Export
Choose location
Save as .json
```

**Multiple Presets:**
```
Select presets (Ctrl+Click)
Right-click → Export Selected
Save as .zip
```

**Export Format:**
```json
{
  "name": "Python Expert",
  "model": "gpt-4",
  "temperature": 0.7,
  "system_prompt": "You are...",
  "tools": ["code_execution"],
  "agents": {...}
}
```

### Import Preset

**From File:**
```
Presets → Import
Select .json or .zip file
Preset added to list
```

**From URL:**
```
Presets → Import from URL
Enter preset URL
Download and import
```

### Share Presets

**Community Presets:**
```
Visit: pygpt.net/presets
Browse presets
Download and import
```

**Create Shareable:**
```
Export preset
Upload to GitHub/Gist
Share URL
Others can import
```

## 🐛 Troubleshooting

### Preset Not Loading
**Problem:** Preset won't apply

**Solutions:**
- Check preset file valid
- Verify model available
- Check API key configured
- Review error message
- Try re-importing

### Model Not Available
**Problem:** Selected model not found

**Solutions:**
- Check model name correct
- Verify API access
- Update model list
- Choose alternative model
- Check provider settings

### Prompt Too Long
**Problem:** System prompt exceeds limit

**Solutions:**
- Shorten prompt
- Remove unnecessary details
- Use more concise language
- Split into multiple presets

### Settings Not Saving
**Problem:** Changes don't persist

**Solutions:**
- Click Save button
- Check write permissions
- Verify disk space
- Restart PyGPT
- Check config file

## 💡 Best Practices

### Effective Prompts

```
✅ Clear role definition
✅ Specific instructions
✅ Examples of desired output
✅ Constraints and guidelines
❌ Vague descriptions
❌ Contradictory instructions
```

**Good Example:**
```
You are a Python expert who:
1. Writes clean, PEP 8 compliant code
2. Includes docstrings and comments
3. Handles errors gracefully
4. Suggests optimizations

Always explain your reasoning.
```

**Bad Example:**
```
You know Python. Help with code.
```

### Organization

```
✅ Descriptive names
✅ Group by category
✅ Use tags/labels
✅ Regular cleanup
❌ Generic names
❌ No organization
```

### Testing

```
✅ Test new presets
✅ Verify behavior
✅ Adjust as needed
✅ Document usage
❌ Deploy untested
❌ No validation
```

### Maintenance

```
✅ Update regularly
✅ Remove unused presets
✅ Backup important ones
✅ Version control
❌ Never update
❌ Accumulate clutter
```

## 🔗 Related Features

- [Chat Interface](./01-chat.md) - Using presets in chat
- [Agents](./06-agents-automation.md) - Agent configuration
- [Experts Mode](../modes/experts.md) - Expert presets

## 📚 Additional Resources

- [Prompt Engineering Guide](https://www.promptingguide.ai/)
- [OpenAI Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Community Presets](https://github.com/szczyglis-dev/py-gpt/discussions)

## 🆘 Need Help?

- Check [FAQ](../faq/general.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Custom Commands](./08-custom-commands.md) →
