# img2webp Documentation

`img2webp` is a Python package that provides both GUI and command-line interfaces for converting images to the WebP format. WebP offers superior compression for images on the web while maintaining quality.

## Features

- **Dual Interface**: Choose between a graphical user interface or command-line tool
- **Multiple Format Support**: Convert from HEIC, JPG, JPEG, and PNG formats
- **Batch Processing**: Convert multiple images at once
- **Quality Control**: Adjust compression level to balance size and quality
- **Progress Tracking**: Monitor conversion progress in both GUI and CLI modes
- **Python API**: Use the converter programmatically in your Python scripts

## Installation

Install using pip:

```bash
pip install img2webp
```

## Quick Start

### GUI Mode

Launch the graphical interface:

```bash
img2webp
```

### Command Line Mode

Convert images using the CLI:

```bash
img2webp-cli input.jpg -o output_dir
```

### Python API

Use in your Python code:

```python
from img2webp import convert_image

convert_image("input.jpg", "output.webp", quality=80)
```

## Documentation Sections

- [Usage Guide](usage.md): Detailed instructions for all interfaces
- [API Reference](#api-reference): Complete API documentation
- [Examples](#examples): Common usage examples
- [Contributing](#contributing): How to contribute to the project

## Requirements

- Python 3.7 or higher
- Pillow library (installed automatically)
- Operating System: Windows, macOS, or Linux

## API Reference

### convert_image

```python
def convert_image(input_path: str, output_path: str, quality: int = 80) -> None
```

Convert a single image to WebP format.

**Parameters**:
- `input_path`: Path to input image
- `output_path`: Path to save WebP image
- `quality`: WebP quality (1-100, default: 80)

### process_files

```python
def process_files(
    input_files: List[str],
    output_dir: str,
    quality: int = 80
) -> tuple[int, int]
```

Process multiple image files.

**Parameters**:
- `input_files`: List of input image paths
- `output_dir`: Directory to save converted images
- `quality`: WebP quality (1-100, default: 80)

**Returns**:
- Tuple of (successful conversions, failed conversions)

## Examples

### Basic Conversion
```python
from img2webp import convert_image

# Convert a single image
convert_image("photo.jpg", "photo.webp")
```

### Batch Processing
```python
from img2webp import process_files

# Convert multiple images
files = ["image1.jpg", "image2.png"]
successful, failed = process_files(files, "output_directory")
print(f"Converted: {successful}, Failed: {failed}")
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests: `pytest`
5. Submit a pull request

## License

This project is licensed under the MIT License. See the LICENSE file for details.