# Installation Guide

PyGPT is available for Windows, Linux, and macOS. Choose the installation method that works best for you.

## 📋 System Requirements

- **Python**: 3.10 - 3.13
- **RAM**: 4GB minimum, 8GB+ recommended
- **Storage**: 500MB for PyGPT + model files
- **OS**: Windows 10/11, Linux, or macOS

## Installation Methods

### 1️⃣ Pre-built Binaries (Easiest)

#### Windows
- Download MSI installer from [pygpt.net/download](https://pygpt.net/#download)
- Run the installer
- Select installation directory
- Launch from Start Menu

#### Linux
- Download AppImage or ZIP from [pygpt.net/download](https://pygpt.net/#download)
- Make AppImage executable: `chmod +x PyGPT_*.AppImage`
- Run: `./PyGPT_*.AppImage`
- Or extract ZIP and run executable

#### Snap (Linux)
```bash
sudo snap install pygpt
pygpt
```

#### macOS
- Not available as pre-built binary
- Use [PyPI](#2%EF%B8%8F⃣-pypi-recommended-for-all-platforms) method below

---

### 2️⃣ PyPI (Recommended for All Platforms)

#### Prerequisites
- Python 3.10+ installed
- pip package manager

#### Installation
```bash
pip install pygpt-net
```

#### Launch
```bash
pygpt
```

#### Upgrade
```bash
pip install --upgrade pygpt-net
```

---

### 3️⃣ Microsoft Store (Windows)

- Open Microsoft Store
- Search for "PyGPT"
- Click Install
- Launch from Start Menu or Store

---

### 4️⃣ From Source

#### Prerequisites
- Python 3.10+
- Git
- Poetry (for dependency management)

#### Steps

```bash
# Clone repository
git clone https://github.com/szczyglis-dev/py-gpt.git
cd py-gpt

# Install dependencies
pip install -r requirements.txt

# Or with Poetry
poetry install

# Run
python run.py
```

---

## Verification

After installation, verify PyGPT works:

### Windows
```powershell
pygpt --version
```

### Linux/macOS
```bash
pygpt --version
```

Expected output: `PyGPT 2.7.10` (or your version)

---

## Troubleshooting Installation

### Issue: "pygpt command not found"
**Solution:**
- **PyPI**: Ensure pip is in your PATH
- **Windows**: Check if installed to Program Files
- Try: `python -m pygpt_net` to run directly

### Issue: "Python 3.10+ required"
**Solution:**
```bash
python --version  # Check version
python3 --version  # Try python3
```
- If too old, [upgrade Python](https://www.python.org/downloads/)

### Issue: Permission denied on Linux
**Solution:**
```bash
chmod +x PyGPT_*.AppImage
```

### Issue: Library not found errors
**Solution:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

---

## First Launch

1. **Start PyGPT**
   - Windows: Click icon in Start Menu
   - Linux: Run `pygpt` or `./PyGPT_*.AppImage`
   - macOS: Run `pygpt` or installed application

2. **License Agreement**
   - Accept the MIT License terms

3. **Initial Setup**
   - Choose interface style (Dark/Light)
   - Select default language
   - Configure basic settings

4. **Add API Key**
   - Go to Settings → API Keys
   - Add your first API key (OpenAI, Google, etc.)
   - See [Basic Configuration](./03-basic-configuration.md)

---

## Next Steps

After successful installation:

1. ✅ [Basic Configuration](./03-basic-configuration.md) - Set up your first API key
2. ✅ [First Steps](./02-first-steps.md) - Start your first chat
3. ✅ [API Key Setup Guide](../guides/02-api-key-setup.md) - Add more providers

---

## Platform-Specific Notes

### Windows
- Installed to `%PROGRAMFILES%\PyGPT` by default
- Configuration stored in `%APPDATA%\pygpt`
- Data directory: `%APPDATA%\pygpt\data`

### Linux
- AppImage runs without installation
- Configuration stored in `~/.pygpt`
- Data directory: `~/.pygpt/data`
- Snap installs to system directories

### macOS
- Installed via Homebrew (when available) or PyPI
- Configuration stored in `~/Library/Application Support/pygpt`
- Data directory: `~/Library/Application Support/pygpt/data`

---

## Uninstallation

### Windows (MSI)
- Settings → Apps → Uninstall PyGPT
- Or: `Control Panel → Programs → Uninstall a program`

### PyPI
```bash
pip uninstall pygpt-net
```

### Linux (Snap)
```bash
sudo snap remove pygpt
```

### Linux (AppImage)
- Simply delete the AppImage file

### macOS
- Delete from Applications folder (if installed)
- Or: `pip uninstall pygpt-net`

---

## Getting Help

- 📖 [Getting Started Guide](./02-first-steps.md)
- 🔧 [Troubleshooting](../reference/troubleshooting.md)
- 💬 [Discord Community](https://pygpt.net/discord)
- 🐛 [Report Issues](https://github.com/szczyglis-dev/py-gpt/issues)
- 🌐 [Official Website](https://pygpt.net)

---

**Next**: [Basic Configuration](./03-basic-configuration.md) →
