# Painter Tool

Simple drawing and image editing tool built into PyGPT.

## 🎨 Overview

Painter is a built-in drawing tool that allows you to create simple drawings, sketches, and annotations. Perfect for quick visual communication with AI or creating simple graphics.

**Key Features:**
- Drawing and sketching
- Multiple brush sizes
- Color selection
- Layers support
- Crop and resize
- Zoom and pan
- Save and export

**Location:** `Tools → Painter`

## 🚀 Getting Started

### Open Painter

1. Launch PyGPT
2. Menu: `Tools → Painter`
3. Canvas opens
4. Start drawing!

### Basic Controls

**Drawing:**
- Left mouse button: Draw
- Right mouse button: Erase
- Mouse wheel: Zoom in/out
- Middle mouse button: Pan canvas

**Keyboard:**
- Ctrl + Z: Undo
- Ctrl + Y: Redo
- Ctrl + S: Save
- Ctrl + N: New canvas

## 🎯 Use Cases

### Sketching Ideas
```
Quick sketches:
- Wireframes
- Diagrams
- Flowcharts
- Concepts
```

### Annotations
```
Mark up images:
- Highlight areas
- Add notes
- Circle important parts
- Draw arrows
```

### Visual Communication
```
Show AI what you mean:
- Draw shapes
- Sketch layouts
- Illustrate concepts
- Create examples
```

### Simple Graphics
```
Create graphics:
- Icons
- Logos
- Buttons
- Backgrounds
```

## 🔧 Tools

### Brush Tool

Draw freehand lines.

**Settings:**
- Size: 1-100 pixels
- Color: Any RGB color
- Opacity: 0-100%

**Usage:**
1. Select brush tool
2. Choose size and color
3. Click and drag to draw

### Eraser Tool

Remove drawn content.

**Settings:**
- Size: 1-100 pixels
- Hard/soft edge

**Usage:**
1. Select eraser tool
2. Choose size
3. Click and drag to erase

### Fill Tool

Fill enclosed areas with color.

**Settings:**
- Color: Any RGB color
- Tolerance: 0-100%

**Usage:**
1. Select fill tool
2. Choose color
3. Click area to fill

### Line Tool

Draw straight lines.

**Settings:**
- Width: 1-100 pixels
- Color: Any RGB color
- Style: Solid/dashed

**Usage:**
1. Select line tool
2. Click start point
3. Click end point

### Shape Tools

Draw basic shapes.

**Available Shapes:**
- Rectangle
- Circle/Ellipse
- Triangle
- Polygon

**Settings:**
- Fill color
- Border color
- Border width

**Usage:**
1. Select shape tool
2. Click and drag to create

### Text Tool

Add text to canvas.

**Settings:**
- Font family
- Font size
- Color
- Bold/italic

**Usage:**
1. Select text tool
2. Click where to place text
3. Type text
4. Click outside to finish

## 🎨 Canvas Controls

### Zoom

**Zoom In/Out:**
- Mouse wheel
- Ctrl + Plus/Minus
- Zoom slider

**Fit to Window:**
- View → Fit to Window
- Or double-click canvas

**Actual Size:**
- View → Actual Size (100%)

### Pan

**Move Canvas:**
- Middle mouse button + drag
- Or hold Space + left mouse drag

**Center Canvas:**
- View → Center

### Crop

**Crop Canvas:**
1. Select crop tool
2. Draw crop rectangle
3. Apply crop

**Auto-Crop:**
- Removes empty borders
- Trims to content

### Resize

**Resize Canvas:**
1. Canvas → Resize
2. Enter new dimensions
3. Choose scaling method:
   - Stretch
   - Fit (maintain aspect)
   - Fill

**Maintain Aspect Ratio:**
- Lock aspect ratio checkbox
- Proportional scaling

## 🎨 Layers

### Layer Basics

Work with multiple layers for complex drawings.

**Benefits:**
- Non-destructive editing
- Organize elements
- Easy modifications
- Reusable components

### Layer Operations

**Create Layer:**
```
Layers → New Layer
Or: Ctrl + Shift + N
```

**Delete Layer:**
```
Select layer → Delete
Or: Right-click → Delete
```

**Duplicate Layer:**
```
Right-click layer → Duplicate
Or: Ctrl + J
```

**Merge Layers:**
```
Select layers → Right-click → Merge
Or: Ctrl + E
```

### Layer Properties

**Opacity:**
- 0-100%
- Transparent to opaque

**Blend Mode:**
- Normal
- Multiply
- Screen
- Overlay

**Visibility:**
- Show/hide layer
- Eye icon toggle

**Lock:**
- Lock layer
- Prevent editing

## 💾 Save & Export

### Save Project

Save as Painter project file (.pygpt-paint).

**Save:**
```
File → Save
Or: Ctrl + S
```

**Save As:**
```
File → Save As
Or: Ctrl + Shift + S
```

**Project includes:**
- All layers
- Layer properties
- Canvas settings
- Undo history

### Export Image

Export as standard image format.

**Formats:**
- PNG (recommended)
- JPG
- BMP
- GIF

**Export:**
```
File → Export
Choose format
Select location
Save
```

**Export Options:**
- Quality (for JPG)
- Transparency (for PNG)
- Flatten layers
- Resize on export

## 🎨 Color Picker

### Select Colors

**Color Picker:**
- Click color swatch
- Choose from palette
- Or enter RGB/HEX

**Recent Colors:**
- Last 10 colors used
- Quick access

**Color Palette:**
- Predefined colors
- Custom palettes
- Save favorites

### Color Tools

**Eyedropper:**
- Pick color from canvas
- Click eyedropper tool
- Click color to sample

**Color History:**
- Recent colors
- Frequently used
- Quick selection

## 🔧 Advanced Features

### Auto-Resize Canvas

Automatically adjusts canvas size to content.

**Enable:**
```
Canvas → Auto-Resize
```

**Behavior:**
- Expands when drawing near edge
- Maintains content
- Prevents clipping

### Grid & Guides

Visual aids for precise drawing.

**Grid:**
```
View → Show Grid
Spacing: 10-100 pixels
```

**Guides:**
```
View → Show Guides
Drag from rulers
```

**Snap to Grid:**
```
View → Snap to Grid
Aligns to grid points
```

### Undo/Redo

Full undo history.

**Undo:**
```
Edit → Undo
Or: Ctrl + Z
```

**Redo:**
```
Edit → Redo
Or: Ctrl + Y
```

**History:**
- Unlimited undo levels
- View history panel
- Jump to any state

## 🎨 Integration with AI

### Send to AI

Send drawing to AI for analysis or discussion.

**How to:**
1. Complete drawing
2. Click "Send to AI" button
3. Or: File → Send to Chat
4. Drawing appears in chat
5. Ask AI about it

**Use cases:**
```
"What do you think of this design?"
"Can you improve this sketch?"
"Explain what this diagram shows"
"Generate code from this wireframe"
```

### Use AI Suggestions

AI can suggest improvements.

**Example:**
```
User: [Sends sketch]
"How can I improve this logo?"

AI: "Consider:
- Simplify the design
- Use fewer colors
- Increase contrast
- Make it more symmetrical"
```

### Generate from Description

AI can describe what to draw.

**Example:**
```
User: "Describe a simple logo for a coffee shop"

AI: "Draw:
- A coffee cup in the center
- Steam rising from the cup
- Circle border around it
- Brown and cream colors"

User: [Draws based on description]
```

## 🐛 Troubleshooting

### Brush Not Drawing
**Problem:** Brush doesn't draw

**Solutions:**
- Check layer is selected
- Verify layer not locked
- Check opacity not 0%
- Ensure brush size > 0

### Slow Performance
**Problem:** Laggy drawing

**Solutions:**
- Reduce canvas size
- Merge layers
- Close other applications
- Reduce brush size

### Can't Save
**Problem:** Save fails

**Solutions:**
- Check disk space
- Verify write permissions
- Try different location
- Check filename valid

### Lost Work
**Problem:** Drawing disappeared

**Solutions:**
- Check undo history
- Verify correct layer selected
- Check layer visibility
- Look in auto-save folder

## 💡 Best Practices

### Organization

```
✅ Use layers for different elements
✅ Name layers descriptively
✅ Group related layers
✅ Delete unused layers
❌ Everything on one layer
❌ Generic layer names
```

### Performance

```
✅ Merge layers when done
✅ Reasonable canvas size
✅ Save regularly
✅ Close when not needed
❌ Hundreds of layers
❌ Huge canvas sizes
```

### Workflow

```
✅ Sketch rough first
✅ Refine details later
✅ Use guides for precision
✅ Save versions
❌ Perfect from start
❌ No planning
```

## 🔗 Related Features

- [Vision & Images](../guides/05-vision-images.md) - Image analysis
- [Image Generation](../guides/05-vision-images.md) - AI image creation
- [File Attachments](../guides/03-working-with-files.md) - File handling

## ⚠️ Limitations

- **Simple tool** - Not a full image editor
- **Basic features** - Limited compared to Photoshop/GIMP
- **Performance** - Large canvases may be slow
- **File formats** - Limited export options

## 🆘 Need Help?

- Check [Vision & Images Guide](../guides/05-vision-images.md)
- Visit [Troubleshooting](../reference/troubleshooting.md)
- Ask on [Discord](https://pygpt.net/discord)
- Report issues on [GitHub](https://github.com/szczyglis-dev/py-gpt/issues)

---

**Next:** [Code Interpreter](../features/03-code-interpreter.md) →
