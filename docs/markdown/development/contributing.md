# Contributing to PyGPT

Thank you for your interest in contributing to PyGPT! This guide will help you get started.

## 🎯 Ways to Contribute

### Code Contributions
- Bug fixes
- New features
- Performance improvements
- Code refactoring
- Test coverage

### Documentation
- Fix typos and errors
- Improve existing docs
- Add new guides
- Translate documentation

### Community
- Answer questions
- Report bugs
- Suggest features
- Share use cases

### Testing
- Test new releases
- Report issues
- Verify bug fixes
- Test on different platforms

---

## 🚀 Getting Started

### 1. Fork the Repository

```bash
# Fork on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/py-gpt.git
cd py-gpt

# Add upstream remote
git remote add upstream https://github.com/szczyglis-dev/py-gpt.git
```

### 2. Set Up Development Environment

```bash
# Install dependencies
pip install -r requirements.txt

# Or use poetry
poetry install

# Run the application
python run.py
```

### 3. Create a Branch

```bash
# Update your fork
git checkout main
git pull upstream main

# Create a feature branch
git checkout -b feature/your-feature-name
# or
git checkout -b fix/bug-description
```

---

## 📝 Development Guidelines

### Code Style

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions focused and concise
- Comment complex logic

### Code Structure

```python
"""
Module docstring explaining purpose
"""

class MyClass:
    """Class docstring"""
    
    def __init__(self):
        """Initialize the class"""
        pass
    
    def my_method(self, param: str) -> bool:
        """
        Method description
        
        :param param: Parameter description
        :return: Return value description
        """
        pass
```

### Testing

- Write tests for new features
- Ensure existing tests pass
- Test on multiple platforms if possible

```bash
# Run tests
python -m pytest tests/

# Or use the test script
./run-tests.sh
```

### Commit Messages

Use clear, descriptive commit messages:

```bash
# Good examples
git commit -m "Add support for custom API endpoints"
git commit -m "Fix memory leak in chat history"
git commit -m "Update documentation for plugin system"

# Bad examples
git commit -m "fix"
git commit -m "update"
git commit -m "changes"
```

**Commit Message Format:**

```
<type>: <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

---

## 🔧 Making Changes

### 1. Write Your Code

- Make focused, atomic changes
- Follow the existing code style
- Add comments where needed
- Update documentation if needed

### 2. Test Your Changes

```bash
# Run the application
python run.py

# Run tests
python -m pytest tests/

# Test specific functionality
python -m pytest tests/test_specific.py
```

### 3. Update Documentation

If your changes affect:
- User-facing features → Update user documentation
- API or code structure → Update developer documentation
- Configuration → Update configuration guides

### 4. Commit Your Changes

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "feat: add new feature description"

# Push to your fork
git push origin feature/your-feature-name
```

---

## 📤 Submitting a Pull Request

### 1. Prepare Your PR

- Ensure all tests pass
- Update documentation
- Rebase on latest main if needed

```bash
# Update your branch
git fetch upstream
git rebase upstream/main
```

### 2. Create Pull Request

1. Go to your fork on GitHub
2. Click "New Pull Request"
3. Select your feature branch
4. Fill out the PR template

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement

## Testing
- [ ] Tests pass locally
- [ ] Added new tests
- [ ] Tested on multiple platforms

## Checklist
- [ ] Code follows style guidelines
- [ ] Documentation updated
- [ ] No breaking changes
- [ ] Commit messages are clear

## Related Issues
Fixes #123
Related to #456
```

### 3. Code Review Process

- Maintainers will review your PR
- Address feedback and comments
- Make requested changes
- Push updates to your branch

```bash
# Make changes based on feedback
git add .
git commit -m "Address review feedback"
git push origin feature/your-feature-name
```

---

## 🐛 Reporting Bugs

### Before Reporting

1. Check existing issues
2. Test on latest version
3. Gather relevant information

### Bug Report Template

```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Windows 11, Ubuntu 22.04]
- Python version: [e.g., 3.11.0]
- PyGPT version: [e.g., 2.0.0]

## Screenshots
If applicable

## Additional Context
Any other relevant information
```

---

## 💡 Suggesting Features

### Feature Request Template

```markdown
## Feature Description
Clear description of the feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should it work?

## Alternatives Considered
Other approaches you've thought about

## Additional Context
Any other relevant information
```

---

## 📚 Documentation Contributions

### Documentation Structure

```
docs/
├── source/           # RST source files
├── markdown/         # Markdown documentation
│   ├── user/        # User guides
│   ├── development/ # Developer docs
│   └── api/         # API reference
└── build/           # Built documentation
```

### Building Documentation

```bash
# Install documentation dependencies
pip install -r docs/requirements.txt

# Build English docs
cd docs
./build-en.sh

# Build Polish docs
./build-pl.sh
```

### Documentation Style

- Use clear, concise language
- Include code examples
- Add screenshots where helpful
- Keep formatting consistent
- Test all code examples

---

## 🌍 Translation Contributions

### Adding Translations

1. Copy existing language file
2. Translate strings
3. Test in application
4. Submit PR

```bash
# Language files location
src/pygpt_net/data/locale/
```

### Translation Guidelines

- Keep formatting placeholders intact
- Maintain consistent terminology
- Test UI with translations
- Check for text overflow

---

## 🔍 Code Review Guidelines

### For Contributors

- Be open to feedback
- Respond to comments promptly
- Ask questions if unclear
- Be patient during review

### For Reviewers

- Be respectful and constructive
- Explain reasoning for changes
- Acknowledge good work
- Focus on code, not person

---

## 📋 Development Workflow

### Typical Workflow

1. **Find or create an issue**
   - Check existing issues
   - Create new issue if needed
   - Discuss approach

2. **Fork and branch**
   - Fork repository
   - Create feature branch
   - Set up development environment

3. **Develop**
   - Write code
   - Add tests
   - Update documentation

4. **Test**
   - Run tests locally
   - Test manually
   - Check different scenarios

5. **Submit PR**
   - Push to your fork
   - Create pull request
   - Fill out template

6. **Review and iterate**
   - Address feedback
   - Make changes
   - Update PR

7. **Merge**
   - PR approved
   - Merged to main
   - Celebrate! 🎉

---

## 🎨 UI/UX Contributions

### Design Guidelines

- Follow existing design patterns
- Maintain consistency
- Consider accessibility
- Test on different screen sizes

### UI Changes

- Include screenshots in PR
- Test with different themes
- Check keyboard navigation
- Verify screen reader compatibility

---

## 🔐 Security

### Reporting Security Issues

**Do not** report security vulnerabilities through public GitHub issues.

Instead:
- Email: [security contact]
- Include detailed description
- Provide steps to reproduce
- Allow time for fix before disclosure

See [SECURITY.md](../../SECURITY.md) for details.

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

## 🤝 Community Guidelines

### Code of Conduct

- Be respectful and inclusive
- Welcome newcomers
- Focus on constructive feedback
- Help others learn and grow

### Communication

- GitHub Issues: Bug reports, feature requests
- GitHub Discussions: Questions, ideas
- Pull Requests: Code contributions

---

## 📞 Getting Help

### Resources

- [Documentation](../README.md)
- [API Reference](api-reference.md)
- [GitHub Issues](https://github.com/szczyglis-dev/py-gpt/issues)
- [GitHub Discussions](https://github.com/szczyglis-dev/py-gpt/discussions)

### Questions?

- Check existing documentation
- Search closed issues
- Ask in GitHub Discussions
- Create new issue if needed

---

## 🙏 Thank You!

Your contributions make PyGPT better for everyone. Whether you're fixing a typo, adding a feature, or helping others, every contribution matters.

Happy coding! 🚀