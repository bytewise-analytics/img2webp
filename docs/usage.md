# Usage Guide

This guide covers all the ways you can use `img2webp` to convert images to WebP format.

## Graphical User Interface (GUI)

### Starting the GUI

Launch the graphical interface by running:

```bash
img2webp
```

### Using the GUI

1. **Select Input Files**
   - Click the "Browse" button next to "Input Files"
   - Select one or more images (HEIC, JPG, JPEG, or PNG)
   - Selected files will appear in the input field

2. **Choose Output Directory**
   - Click the "Browse" button next to "Output Directory"
   - Select where you want to save the WebP files

3. **Adjust Compression**
   - Use the slider to set compression level
   - Lower values = smaller files, lower quality
   - Higher values = larger files, higher quality
   - Recommended: 0.75-0.85 for good balance

4. **Convert**
   - Click the "Convert" button
   - Progress bar will show conversion status
   - Status messages appear at the bottom

### GUI Tips

- Hover over the "?" button for compression level help
- Multiple files can be selected at once
- The status bar shows current operation details
- Green status indicates successful conversion

## Command Line Interface (CLI)

### Basic Usage

```bash
img2webp-cli [input files] -o [output directory] [options]
```

### Common Commands

1. **Convert a Single File**
   ```bash
   img2webp-cli input.jpg -o output_dir
   ```

2. **Convert Multiple Files**
   ```bash
   img2webp-cli image1.jpg image2.png -o output_dir
   ```

3. **Set Quality Level**
   ```bash
   img2webp-cli input.jpg -o output_dir -q 90
   ```

4. **Convert All JPGs in Directory**
   ```bash
   img2webp-cli *.jpg -o output_dir
   ```

5. **Enable Verbose Output**
   ```bash
   img2webp-cli input.jpg -o output_dir -v
   ```

### CLI Options

```
-o, --output    Output directory (required)
-q, --quality   Quality level 1-100 (default: 80)
-v, --verbose   Enable verbose output
```

### CLI Tips

- Use wildcards to convert multiple files
- Quality of 80-90 is recommended for web use
- Check verbose output (-v) for detailed information
- Exit codes indicate success (0) or failure (1)

## Python API

### Basic Usage

```python
from img2webp import convert_image, process_files

# Convert single image
convert_image(
    input_path="input.jpg",
    output_path="output.webp",
    quality=80
)

# Convert multiple images
successful, failed = process_files(
    input_files=["image1.jpg", "image2.png"],
    output_dir="output_directory",
    quality=80
)
```

### Error Handling

```python
try:
    convert_image("input.jpg", "output.webp")
except Exception as e:
    print(f"Conversion failed: {e}")
```

### Best Practices

1. **Quality Settings**
   - 80-90: High quality, good compression
   - 60-80: Medium quality, better compression
   - Below 60: Visible quality loss

2. **Performance**
   - Process files in batches using `process_files`
   - Monitor successful/failed conversions
   - Use try-except for error handling

3. **File Management**
   - Check input file existence
   - Ensure output directory exists
   - Handle existing files appropriately

## Troubleshooting

### Common Issues

1. **File Not Found**
   - Check file paths
   - Ensure proper permissions
   - Use absolute paths if needed

2. **Conversion Fails**
   - Verify input file format
   - Check available disk space
   - Ensure write permissions

3. **Quality Issues**
   - Increase quality setting
   - Check input image quality
   - Verify output file size

### Getting Help

1. **Check Logs**
   - Enable verbose mode in CLI
   - Check error messages
   - Look for Python exceptions

2. **Report Issues**
   - Visit GitHub repository
   - Create detailed bug report
   - Include error messages

## Advanced Usage

### Batch Processing

```python
from pathlib import Path
from img2webp import process_files

# Convert all images in a directory
input_dir = Path("images")
image_files = [
    str(f) for f in input_dir.glob("*.jpg")
]
process_files(image_files, "output_dir")
```

### Custom Processing

```python
from PIL import Image
from img2webp import convert_image

# Pre-process before conversion
img = Image.open("input.jpg")
img = img.rotate(90)
img.save("rotated.jpg")
convert_image("rotated.jpg", "output.webp")
```