# Vision & Images Guide

Work with images, vision models, and image generation in PyGPT.

## 🖼️ Overview

PyGPT supports comprehensive image capabilities including image analysis (vision), image generation, and image editing. Use AI to understand images, create new ones, or modify existing images.

**Key Features:**
- Image analysis (vision)
- Image generation
- Camera capture
- Image editing
- Multiple formats
- Batch processing

## 🎯 Capabilities

### Image Analysis (Vision)

**What AI can do:**
- Describe images
- Extract text (OCR)
- Identify objects
- Analyze charts/graphs
- Read handwriting
- Answer questions about images
- Compare images
- Detect patterns

### Image Generation

**What AI can create:**
- Artwork and illustrations
- Logos and icons
- Diagrams and charts
- Product mockups
- Concept art
- Photo-realistic images
- Abstract designs
- Style variations

### Image Editing

**What AI can modify:**
- Remove backgrounds
- Change colors
- Add/remove objects
- Enhance quality
- Apply styles
- Resize/crop
- Combine images

## 🚀 Image Analysis (Vision)

### Supported Models

**OpenAI:**
- GPT-4V (GPT-4 Vision)
- GPT-4o (multimodal)
- GPT-4o-mini

**Google:**
- Gemini 1.5 Pro
- Gemini 1.5 Flash
- Gemini 2.0

**Anthropic:**
- Claude 3.5 Sonnet
- Claude 3 Opus
- Claude 3 Haiku

**xAI:**
- Grok Vision

### Enable Vision

**Method 1: Vision-Capable Model**
```
1. Select vision model (GPT-4V, Gemini, Claude)
2. Upload image
3. Ask question
4. AI analyzes image
```

**Method 2: Vision Plugin**
```
1. Enable "Vision (inline)" plugin
2. Works with any model
3. Upload image
4. Ask question
5. Plugin handles vision
```

### Upload Images

**From Disk:**
```
1. Click attachment button (📎)
2. Select image file
3. Image appears in chat
4. Type your question
5. Send
```

**From Camera:**
```
1. Click camera button (📷)
2. Camera preview opens
3. Capture image
4. Image attached
5. Ask question
```

**Drag & Drop:**
```
1. Drag image from file manager
2. Drop into chat
3. Image attached
4. Ask question
```

**Paste:**
```
1. Copy image to clipboard
2. Paste in chat (Ctrl+V)
3. Image attached
4. Ask question
```

### Supported Formats

**Image Formats:**
- JPG/JPEG
- PNG
- GIF
- WebP
- BMP
- TIFF

**Size Limits:**
- Max file size: 20MB
- Max dimensions: 4096x4096
- Recommended: < 5MB

### Vision Examples

**Describe Image:**
```
You: [Uploads photo of sunset]
"Describe this image"

AI: "This image shows a beautiful sunset over the ocean. 
The sky displays vibrant orange and pink hues, with 
clouds scattered across the horizon. The sun is partially 
visible, creating a golden reflection on the water's 
surface. The scene conveys a peaceful, serene atmosphere."
```

**Extract Text (OCR):**
```
You: [Uploads document photo]
"Extract all text from this image"

AI: "Here's the text from the image:

[Extracted text with formatting preserved]"
```

**Analyze Chart:**
```
You: [Uploads sales chart]
"Analyze this sales chart"

AI: "This chart shows quarterly sales data:
- Q1: $100K (baseline)
- Q2: $150K (+50% growth)
- Q3: $200K (+33% growth)
- Q4: $250K (+25% growth)

Key insights:
- Consistent upward trend
- Total annual growth: 150%
- Strongest growth in Q2
- Steady acceleration throughout year"
```

**Identify Objects:**
```
You: [Uploads room photo]
"What objects are in this room?"

AI: "I can see the following objects:
- Sofa (gray, L-shaped)
- Coffee table (wooden)
- TV (mounted on wall)
- Bookshelf (filled with books)
- Plants (2 potted plants)
- Rug (patterned, under coffee table)
- Lamp (floor lamp, corner)
- Artwork (2 framed pieces on wall)"
```

**Compare Images:**
```
You: [Uploads 2 images]
"What are the differences between these images?"

AI: "Comparing the two images:

Differences:
1. Lighting: Image 1 is brighter
2. Color: Image 2 has warmer tones
3. Composition: Image 1 is centered, Image 2 is off-center
4. Background: Different backgrounds
5. Objects: Image 2 has additional elements

Similarities:
1. Same subject
2. Similar angle
3. Same general setting"
```

## 🎨 Image Generation

### Supported Models

**OpenAI:**
- DALL-E 3
- DALL-E 2

**Google:**
- Imagen 3
- Imagen 4

**Other:**
- gpt-image-1
- gpt-image-1.5
- Nano Banana

### Enable Image Generation

**Method 1: Image Generation Mode**
```
1. Select mode: Image Generation
2. Choose image model
3. Enter prompt
4. Generate
```

**Method 2: Inline Plugin**
```
1. Enable "Image generation (inline)" plugin
2. Use any chat mode
3. Ask AI to generate image
4. Image created inline
```

**Method 3: Remote Tool**
```
1. Enable remote image generation
2. Available in Chat mode
3. AI decides when to generate
4. Automatic generation
```

### Generation Settings

**Image Size:**
```
Square: 1024x1024
Portrait: 1024x1792
Landscape: 1792x1024
Custom: Various sizes
```

**Quality:**
```
Standard: Faster, cheaper
HD: Higher quality, slower
```

**Style:**
```
Natural: Photo-realistic
Vivid: More artistic
```

**Number:**
```
Generate: 1-10 images
Default: 1
```

### Generation Examples

**Simple Prompt:**
```
You: "Generate an image of a sunset over mountains"

AI: [Generates image]
"Here's your sunset over mountains image."
```

**Detailed Prompt:**
```
You: "Generate a photo-realistic image of a modern office 
space with large windows, natural lighting, minimalist 
furniture, plants, and a city view"

AI: [Generates detailed image]
"I've created a modern office space with all the 
elements you requested."
```

**Artistic Style:**
```
You: "Generate an image of a cat in the style of Van Gogh"

AI: [Generates artistic image]
"Here's a cat painted in Van Gogh's distinctive style 
with swirling brushstrokes and vibrant colors."
```

**Logo Design:**
```
You: "Generate a minimalist logo for a coffee shop called 
'Morning Brew' using brown and cream colors"

AI: [Generates logo]
"I've created a minimalist coffee shop logo with your 
specified colors."
```

### Raw vs AI-Enhanced Prompts

**Raw Mode:**
```
Your prompt sent directly to model
No modifications
Exact control
```

**AI-Enhanced Mode:**
```
AI improves your prompt
Adds details
Better results
Recommended
```

**Example:**
```
Your prompt: "cat"

AI-enhanced: "A photorealistic image of a fluffy orange 
tabby cat sitting on a windowsill, natural lighting, 
soft focus background, professional photography"
```

## 📸 Camera Capture

### Enable Camera

**Requirements:**
- Webcam or camera
- Camera permissions granted
- Camera plugin enabled (if needed)

**Access Camera:**
```
1. Click camera button (📷)
2. Grant permissions if asked
3. Camera preview opens
4. Capture image
5. Image attached to message
```

### Camera Settings

**Resolution:**
```
Low: 640x480
Medium: 1280x720
High: 1920x1080
```

**Mirror:**
```
Enable: Mirror image (selfie mode)
Disable: Normal view
```

**Timer:**
```
None: Instant capture
3s: 3-second delay
5s: 5-second delay
10s: 10-second delay
```

### Camera Use Cases

**Real-Time Analysis:**
```
1. Capture object
2. Ask "What is this?"
3. Get instant identification
```

**Document Scanning:**
```
1. Capture document
2. Ask "Extract text"
3. Get OCR results
```

**Visual Questions:**
```
1. Capture scene
2. Ask specific question
3. Get contextual answer
```

**Product Information:**
```
1. Capture product
2. Ask "Tell me about this"
3. Get product details
```

## 🛠️ Image Tools

### Painter Tool

**Built-in drawing tool:**
```
Tools → Painter
- Draw sketches
- Create diagrams
- Annotate images
- Simple graphics
```

**Features:**
- Multiple brushes
- Color selection
- Layers
- Crop/resize
- Save/export

**Use Cases:**
- Quick sketches
- Wireframes
- Annotations
- Visual communication

### Image Viewer

**View and manage images:**
```
- Full-size viewing
- Zoom and pan
- Previous/next navigation
- Save to disk
- Copy to clipboard
```

**Access:**
```
Click any image in chat
Or: Right-click → View Image
```

## 🐛 Troubleshooting

### Image Not Uploading

**Problem:** Can't upload image

**Solutions:**
- Check file size (< 20MB)
- Verify format supported
- Check file not corrupted
- Try different image
- Check disk space

### Vision Not Working

**Problem:** AI can't see image

**Solutions:**
- Use vision-capable model
- Enable Vision plugin
- Check image uploaded correctly
- Verify image format
- Try re-uploading

### Generation Failed

**Problem:** Image won't generate

**Solutions:**
- Check API key valid
- Verify model available
- Review prompt (no violations)
- Check API quota
- Try different prompt

### Poor Quality Results

**Problem:** Generated images poor quality

**Solutions:**
- Use HD quality setting
- Improve prompt detail
- Try different model
- Use AI-enhanced prompts
- Add style specifications

### Camera Not Working

**Problem:** Can't access camera

**Solutions:**
- Grant camera permissions
- Check camera connected
- Close other camera apps
- Restart PyGPT
- Check system settings

## 💡 Best Practices

### Vision Prompts

```
✅ "Describe this image in detail"
✅ "Extract all text from this document"
✅ "What objects are visible in this photo?"
✅ "Analyze the data in this chart"
❌ "What is this?" (too vague)
❌ "Look" (no question)
```

### Generation Prompts

```
✅ "A photorealistic sunset over mountains with 
    vibrant orange and pink colors"
✅ "Minimalist logo for tech startup, blue and 
    white, modern, clean lines"
❌ "sunset" (too simple)
❌ "make it good" (not specific)
```

### Image Quality

```
✅ Use high-resolution images
✅ Good lighting
✅ Clear focus
✅ Appropriate format
❌ Blurry images
❌ Poor lighting
❌ Tiny images
```

## 🔗 Related Features

- [Chat Mode](./01-chat-modes.md) - Vision in chat
- [Painter Tool](../tools/painter.md) - Drawing tool
- [File Attachments](./03-working-with-files.md) - File handling

## 📚 Additional Resources

- [DALL-E Guide](https://platform.openai.com/docs/guides/images)
- [Gemini Vision](https://ai.google.dev/gemini-api/docs/vision)
- [Claude Vision](https://docs.anthropic.com/claude/docs/vision)

## 🆘 Need Help?

- Check [FAQ](../faq/general.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Plugins & Extensions](./06-plugins-extensions.md) →
