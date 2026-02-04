# Vision & Images Guide

Using image analysis and vision features in PyGPT.

## 🖼️ Vision Mode Basics

### What It Is
Upload images and ask AI to analyze them, describe content, extract text, or answer questions about visual content.

### Getting Started

1. Switch to **Vision Mode**
2. Click 📎 attachment button
3. Select image file
4. Type question about image
5. Send message
6. AI analyzes and responds

---

## 📸 Supported Image Formats

| Format | Extension | Support |
|--------|-----------|---------|
| **JPEG** | .jpg, .jpeg | ✅ Full |
| **PNG** | .png | ✅ Full |
| **GIF** | .gif | ✅ Full |
| **WebP** | .webp | ✅ Full |

### Size Limits
- Maximum: 20MB per image
- Recommended: Under 5MB for faster processing

---

## 🎯 Vision Capabilities

### Image Description
```
Upload: Any image
Ask: "Describe this image"
Result: Detailed text description
```

### Text Extraction (OCR)
```
Upload: Document/screenshot
Ask: "Extract all text from this image"
Result: All text transcribed
```

### Chart Analysis
```
Upload: Chart or graph
Ask: "What trends do you see?"
Result: Analysis of data visualization
```

### Object Recognition
```
Upload: Photo with objects
Ask: "What objects are in this image?"
Result: List of identified objects
```

### Handwriting Reading
```
Upload: Handwritten text
Ask: "What does this handwriting say?"
Result: Transcribed handwriting
```

### Question Answering
```
Upload: Image
Ask: Any question about content
Result: AI answers based on image
```

---

## 🖨️ Common Use Cases

### Document Scanning
1. Take photo of document
2. Upload to PyGPT
3. Ask for specific information
4. Get extracted/analyzed data

### Receipt Analysis
1. Upload receipt image
2. Ask for total or items
3. Get cost breakdown
4. Extract merchant info

### Screenshot Review
1. Capture screenshot
2. Upload to PyGPT
3. Get feedback or description
4. Extract information

### Travel Photos
1. Upload travel photo
2. Ask for location identification
3. Get historical/cultural information
4. Get recommendations

---

## ⚙️ Vision Settings

### Model Requirements
- Model must support vision
- Supported: GPT-4V, Gemini, Claude 3
- Not supported: Text-only models

### Quality Settings
1. Settings → Vision
2. Adjust image size (larger = more tokens)
3. Set detail level

---

## 💡 Pro Tips

### Tip 1: Clear Images Work Best
- Good lighting
- Sharp focus
- High contrast
- Larger text/objects

### Tip 2: Specific Questions
- Instead of: "What is this?"
- Better: "Extract the price from this receipt"
- More focused = better results

### Tip 3: Multiple Images
Attach multiple images:
1. Click 📎 multiple times
2. Ask comparison questions
3. AI analyzes all images

### Tip 4: Cropping First
For better results:
1. Crop image to relevant section
2. Removes irrelevant information
3. Faster processing
4. Lower token usage

---

## 🐛 Troubleshooting

### Image Not Uploading
**Check:**
- File size under 20MB?
- Format supported (JPG, PNG, GIF, WebP)?
- File not corrupted?

**Try:**
- Compress image
- Try different format
- Restart PyGPT

### Poor Recognition
**Improve:**
- Use higher resolution image
- Better lighting
- Crop to relevant area
- Ask more specific questions

### "Model doesn't support vision"
**Solution:**
- Switch to vision-capable model
- Try GPT-4V or Gemini
- Check provider dashboard

---

## 📊 Token Usage

Vision processing uses tokens:
- Image analysis: 500-1000 tokens
- Text extraction: 500-2000 tokens
- Complex analysis: 1000-2000 tokens

**Tip:** Crop images to reduce token usage

---

**Next:** [Plugins & Extensions Guide](./06-plugins-extensions.md) →
