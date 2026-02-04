# Custom Commands

Create your own AI-powered commands and tools.

## 🛠️ Overview

Custom Commands allow you to create reusable AI commands with specific prompts and behaviors. Build your own tools tailored to your workflow.

**Key Features:**
- Custom command creation
- Parameterized prompts
- Quick execution
- Command library
- Import/export
- Keyboard shortcuts

**Plugin:** Custom Commands (built-in)

## 🚀 Getting Started

### What are Custom Commands?

**Regular Chat:**
```
You: "Summarize this text: [paste long text]"
AI: [Provides summary]
```

**Custom Command:**
```
You: /summarize [paste long text]
AI: [Provides summary using your custom prompt]
```

**Benefits:**
- Faster execution
- Consistent results
- Reusable templates
- Parameterized inputs
- Organized workflow

### Enable Custom Commands

1. **Open Plugins**
   ```
   Menu → Plugins → Custom Commands
   ```

2. **Enable Plugin**
   - Toggle switch to ON

3. **Create Commands**
   ```
   Plugins → Custom Commands → Manage
   ```

### Your First Custom Command

```
1. Click "New Command"
2. Name: summarize
3. Prompt: "Summarize the following text in 3 bullet points: {input}"
4. Save

Usage:
/summarize [your text here]
```

## 🎯 Use Cases

### Text Processing
```
/summarize - Summarize text
/translate - Translate to language
/proofread - Check grammar and spelling
/simplify - Simplify complex text
```

### Code Operations
```
/review - Review code quality
/document - Generate documentation
/test - Create unit tests
/optimize - Suggest optimizations
```

### Content Creation
```
/blog - Generate blog post
/email - Draft professional email
/social - Create social media post
/headline - Generate catchy headlines
```

### Data Analysis
```
/analyze - Analyze data
/visualize - Create visualization code
/insights - Extract key insights
/report - Generate report
```

### Research
```
/research - Research topic
/compare - Compare options
/pros-cons - List pros and cons
/sources - Find credible sources
```

## ⚙️ Configuration

### Command Editor

**Access:**
```
Plugins → Custom Commands → Manage Commands
```

### Basic Settings

**Command Name:**
```
Name: summarize
Trigger: /summarize
Description: Summarize text in bullet points
```

**Command Prompt:**
```
Summarize the following text in 3 concise bullet points:

{input}

Focus on the main ideas and key takeaways.
```

**Parameters:**
```
{input} - User input
{selection} - Selected text
{file} - File content
{clipboard} - Clipboard content
```

### Advanced Settings

**Model Selection:**
```
Model: GPT-4 / GPT-3.5 / etc.
Use specific model for command
Override default model
```

**Temperature:**
```
Temperature: 0.0 - 2.0
Control creativity
Command-specific setting
```

**Max Tokens:**
```
Max tokens: 100-4000
Limit response length
Prevent long outputs
```

**System Prompt:**
```
Additional context
Role definition
Constraints
```

**Output Format:**
```
Plain text
Markdown
Code block
JSON
```

## 🎨 Command Examples

### Summarize Command

```yaml
Name: summarize
Trigger: /summarize
Prompt: |
  Summarize the following text in 3 bullet points:
  
  {input}
  
  Focus on main ideas and key takeaways.

Model: GPT-3.5-turbo
Temperature: 0.5
Max Tokens: 200
```

**Usage:**
```
/summarize The quick brown fox jumps over the lazy dog...
```

### Translate Command

```yaml
Name: translate
Trigger: /translate
Prompt: |
  Translate the following text to {language}:
  
  {input}
  
  Provide natural, fluent translation.

Parameters:
  - language: Target language (default: Spanish)

Model: GPT-4
Temperature: 0.3
```

**Usage:**
```
/translate language=French Hello, how are you?
```

### Code Review Command

```yaml
Name: review
Trigger: /review
Prompt: |
  Review the following code for:
  - Code quality
  - Best practices
  - Security issues
  - Performance
  - Potential bugs
  
  Code:
  {input}
  
  Provide specific, actionable feedback.

Model: GPT-4
Temperature: 0.3
Max Tokens: 1000
```

**Usage:**
```
/review
def calculate(x, y):
    return x / y
```

### Email Draft Command

```yaml
Name: email
Trigger: /email
Prompt: |
  Draft a professional email with:
  - Subject: {subject}
  - Tone: {tone}
  - Content: {input}
  
  Make it clear, concise, and professional.

Parameters:
  - subject: Email subject
  - tone: formal/casual (default: formal)

Model: GPT-4
Temperature: 0.7
```

**Usage:**
```
/email subject="Meeting Request" tone=formal
I'd like to schedule a meeting to discuss the project.
```

### Data Analysis Command

```yaml
Name: analyze
Trigger: /analyze
Prompt: |
  Analyze the following data and provide:
  1. Key statistics
  2. Trends and patterns
  3. Insights and recommendations
  
  Data:
  {input}
  
  Use Python code if needed for calculations.

Model: GPT-4
Temperature: 0.5
Tools: Code execution
```

**Usage:**
```
/analyze
Sales data: Jan: 100, Feb: 150, Mar: 200...
```

## 🔧 Advanced Features

### Parameterized Commands

**Define Parameters:**
```
Prompt: Translate {input} to {language} in {style} style

Parameters:
- language: Target language (required)
- style: Translation style (optional, default: formal)
```

**Usage:**
```
/translate language=Spanish style=casual Hello!
```

### Multi-Step Commands

**Command Chain:**
```
Command 1: Research topic
  ↓
Command 2: Analyze findings
  ↓
Command 3: Create report
```

**Implementation:**
```
Name: research-report
Steps:
  1. /research {topic}
  2. /analyze {results}
  3. /report {analysis}
```

### Conditional Logic

**If-Then Commands:**
```
If input contains code:
  → Use code review prompt
Else if input contains data:
  → Use data analysis prompt
Else:
  → Use general analysis prompt
```

### Command Templates

**Template Variables:**
```
{date} - Current date
{time} - Current time
{user} - User name
{model} - Current model
{context} - Current context
```

**Example:**
```
Prompt: |
  Date: {date}
  User: {user}
  
  {input}
```

### Output Processing

**Post-Processing:**
```
1. Execute command
2. Get AI response
3. Process output:
   - Format as markdown
   - Extract code blocks
   - Save to file
   - Copy to clipboard
```

## 💾 Import/Export

### Export Commands

**Single Command:**
```
Right-click command → Export
Save as .json
```

**All Commands:**
```
Manage Commands → Export All
Save as .zip
```

**Command Format:**
```json
{
  "name": "summarize",
  "trigger": "/summarize",
  "prompt": "Summarize...",
  "model": "gpt-4",
  "temperature": 0.5,
  "max_tokens": 200
}
```

### Import Commands

**From File:**
```
Manage Commands → Import
Select .json or .zip
Commands added
```

**From Library:**
```
Browse command library
Select commands
Import to PyGPT
```

### Share Commands

**Community Library:**
```
Visit: pygpt.net/commands
Browse commands
Download and import
```

**Publish Your Commands:**
```
Export command
Upload to GitHub/Gist
Share with community
```

## 🐛 Troubleshooting

### Command Not Working
**Problem:** Command doesn't execute

**Solutions:**
- Check plugin enabled
- Verify command syntax
- Check trigger spelling
- Review error message
- Test prompt manually

### Wrong Output
**Problem:** Unexpected results

**Solutions:**
- Review prompt wording
- Adjust temperature
- Add more context
- Test with examples
- Refine instructions

### Parameters Not Working
**Problem:** Parameters not replaced

**Solutions:**
- Check parameter syntax: {param}
- Verify parameter names
- Test with simple example
- Check for typos

### Slow Execution
**Problem:** Command takes too long

**Solutions:**
- Use faster model
- Reduce max tokens
- Simplify prompt
- Optimize instructions

## 💡 Best Practices

### Command Design

```
✅ Clear, specific prompts
✅ Descriptive names
✅ Useful parameters
✅ Appropriate model
❌ Vague instructions
❌ Generic names
```

**Good Command:**
```
Name: code-review
Prompt: Review this code for security, performance, 
        and best practices. Provide specific, 
        actionable feedback with examples.
```

**Bad Command:**
```
Name: check
Prompt: Look at this
```

### Organization

```
✅ Group by category
✅ Consistent naming
✅ Document usage
✅ Version control
❌ Random organization
❌ No documentation
```

### Testing

```
✅ Test with various inputs
✅ Verify edge cases
✅ Check error handling
✅ Validate output
❌ No testing
❌ Assume it works
```

### Maintenance

```
✅ Update regularly
✅ Remove unused commands
✅ Refine prompts
✅ Backup commands
❌ Never update
❌ Accumulate clutter
```

## 🔗 Related Features

- [Presets & Prompts](./07-presets-prompts.md) - Prompt templates
- [Agents](./06-agents-automation.md) - Automated workflows
- [Plugins](../guides/06-plugins-extensions.md) - Plugin system

## 📚 Additional Resources

- [Prompt Engineering](https://www.promptingguide.ai/)
- [Command Examples](https://github.com/szczyglis-dev/py-gpt/discussions)
- [Community Commands](https://pygpt.net/commands)

## 🆘 Need Help?

- Check [Presets Guide](./07-presets-prompts.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [MCP Support](./09-mcp-support.md) →
