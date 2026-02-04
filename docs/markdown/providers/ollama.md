# Local Models with Ollama

Run AI models completely free on your computer with Ollama.

## 🎯 Quick Facts

| Aspect | Details |
|--------|---------|
| **Cost** | FREE ✅ |
| **Location** | Your computer (local) |
| **Internet** | Not required (offline) |
| **Privacy** | 100% (no data sent anywhere) |
| **Setup** | 5 minutes |
| **Performance** | Depends on hardware |
| **Models** | 50+ available |
| **Vision** | Limited |
| **Audio** | ❌ No |

---

## ✅ Why Use Ollama?

- 💰 **Free** - No costs ever
- 🔐 **Private** - Data never leaves your computer
- 🚀 **Fast** - No internet latency
- 📶 **Offline** - Works without internet
- ⚙️ **Local Control** - You control everything
- 🎮 **No GPU Required** - CPU works (slower)

---

## 📋 System Requirements

### Minimum (CPU only)
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 10GB+ free space
- **CPU**: Modern processor (Intel/AMD)

### Recommended (GPU acceleration)
- **NVIDIA**: GPU with 6GB+ VRAM
- **AMD**: RDNA GPU series
- **Mac**: M1/M2 or newer
- **RAM**: 16GB+

---

## 🚀 Installation

### Step 1: Download Ollama

**Windows:**
1. Go to [ollama.ai](https://ollama.ai)
2. Click "Download for Windows"
3. Run installer
4. Restart computer

**Mac:**
1. Download from [ollama.ai](https://ollama.ai)
2. Open DMG file
3. Drag Ollama to Applications
4. Restart

**Linux:**
```bash
curl https://ollama.ai/install.sh | sh
```

### Step 2: Verify Installation

```bash
ollama --version
# Should show version number
```

### Step 3: Start Ollama Service

**Windows/Mac:**
- Ollama starts automatically after install
- Check system tray for Ollama icon

**Linux:**
```bash
ollama serve
# Runs in background
```

---

## 📥 Download Models

### Popular Models

**Llama 2 (Recommended)**
```bash
ollama pull llama2
# ~4GB download
```
Best general-purpose model, fast

**Mistral**
```bash
ollama pull mistral
# ~4.2GB download
```
Very fast, good quality

**Neural Chat**
```bash
ollama pull neural-chat
# ~4GB download
```
Optimized for conversations

**Orca-Mini**
```bash
ollama pull orca-mini
# ~2GB download
```
Smaller, faster, good for basic tasks

### Larger Models

```bash
ollama pull llama2-13b    # 25GB - More capable
ollama pull neural-chat   # High quality
ollama pull openchat      # Fast and capable
```

### List Downloaded Models

```bash
ollama list
# Shows all installed models
```

### Remove Model

```bash
ollama rm llama2
# Frees up space
```

---

## 🔧 Using Ollama in PyGPT

### Method 1: Automatic Detection

1. Start Ollama (runs in background)
2. Open PyGPT
3. Go to Settings → Models
4. Select "Ollama" provider
5. Choose model from dropdown
6. Start chatting!

### Method 2: Manual Setup

1. Ensure Ollama is running
2. PyGPT should auto-detect on localhost:11434
3. If not, go to Settings → Providers → Ollama
4. Configure address (usually `http://localhost:11434`)
5. Select model

---

## 💬 Chat with Ollama

### Start Chatting

1. Select Ollama provider
2. Choose model (e.g., llama2)
3. Type message
4. First response slower (loading model into memory)
5. Subsequent responses faster

### Performance Tips

```
Faster responses:
1. Smaller models (Haiku vs Llama2-13b)
2. Shorter max_tokens setting
3. Lower temperature setting
4. Keep context smaller
5. Use GPU acceleration if available
```

### Keep Model in Memory

```bash
# Run specific model and keep running
ollama run llama2
```

Leave this terminal open for faster responses in PyGPT.

---

## 🎯 Model Comparison

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| **Orca-Mini** | 2GB | Very Fast | Basic | Quick answers |
| **Mistral** | 4GB | Fast | Good | General use |
| **Llama2** | 4GB | Fast | Good | Chat |
| **Neural-Chat** | 4GB | Medium | Good | Conversation |
| **Llama2-13b** | 25GB | Slow | Excellent | Complex tasks |
| **Orca-Dolphin** | 7GB | Medium | Very Good | Advanced |

---

## 🖥️ GPU Acceleration

### NVIDIA Cards

```bash
# Install NVIDIA CUDA
# Then Ollama auto-detects GPU

# Check if using GPU
ollama list  # Shows "GPU memory"
```

### AMD Cards

```bash
# Install AMD ROCm
# Then Ollama auto-detects

# Linux AMD setup
export CUDA_VISIBLE_DEVICES=0
ollama serve
```

### Mac M1/M2

```bash
# Auto-detected
# GPU acceleration enabled by default
# Check Activity Monitor for Metal usage
```

---

## 🔌 Advanced Configuration

### Custom Model File

Create `Modelfile`:
```
FROM llama2

PARAMETER temperature 0.7
PARAMETER top_p 0.9
PARAMETER num_ctx 4096
```

Then:
```bash
ollama create mymodel -f Modelfile
ollama run mymodel
```

### API Access

Ollama runs on `http://localhost:11434`

```bash
# Test API
curl http://localhost:11434/api/tags

# Generate response
curl -X POST http://localhost:11434/api/generate \
  -d '{"model":"llama2","prompt":"Hello"}'
```

---

## 💾 Storage Management

### Free Up Space

```bash
# Remove unused models
ollama rm llama2
ollama rm mistral

# Or delete manually
~/.ollama/models/
```

### Reduce Model Size

Use quantized versions:
```bash
ollama pull llama2:7b-q4_0
# Smaller, faster, less VRAM
```

---

## 🐛 Troubleshooting

### Model Not Found

```bash
# Check installed models
ollama list

# Download again
ollama pull llama2
```

### Out of Memory

- Use smaller model (Haiku vs 13b)
- Reduce `num_ctx` in settings
- Close other applications
- Add more RAM or enable swap

### Slow Responses

- Use GPU acceleration if available
- Choose smaller model
- Reduce max_tokens
- Close other apps using CPU

### Can't Connect

1. Check Ollama is running
2. Check address: `http://localhost:11434`
3. Check firewall not blocking port 11434
4. Restart Ollama service

---

## 🌐 Compare: Local vs Cloud

| Feature | Local (Ollama) | Cloud (OpenAI) |
|---------|---|---|
| **Cost** | Free | Paid |
| **Privacy** | Complete | No |
| **Speed** | Network latency | Cloud latency |
| **Offline** | Yes | No |
| **Quality** | Good | Excellent |
| **Latest Models** | Behind | Cutting edge |
| **GPU Required** | Optional | No |

---

## 📚 Resources

- **Official Site**: [ollama.ai](https://ollama.ai)
- **Models**: [Model Library](https://ollama.ai/library)
- **GitHub**: [ollama/ollama](https://github.com/ollama/ollama)
- **Discord**: [Ollama Community](https://discord.gg/ollama)

---

## ⚡ Quick Start Command

```bash
# Everything in one go:
1. Download Ollama from ollama.ai
2. Install and restart
3. Run: ollama pull llama2
4. Start PyGPT
5. Select Ollama + llama2
6. Start chatting!
```

---

**Next:** [All Providers](../guides/02-api-key-setup.md) →
