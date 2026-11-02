
# Python Batch Background Remover

A simple, AI-powered Python tool that automatically removes backgrounds from multiple images in a selected folder and saves the results as transparent PNG files.

Built using **Python, rembg, and Pillow**, this tool makes bulk image background removal easy without manually editing each image.

## Features

- AI-powered background removal
- Batch processing of multiple images
- Supports JPG, JPEG, PNG, WEBP, BMP, and TIFF
- Automatically creates an output folder
- Saves processed images as transparent PNG files
- Preserves original images
- Accepts folder paths directly from the user
- Runs locally without requiring an API key
- Supports recursive folder processing
- Handles individual image processing errors

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| rembg | AI-powered background removal |
| Pillow | Image processing |
| ONNX Runtime | AI model inference |
| Virtual Environment | Dependency isolation |

## Project Structure

```text
python-batch-background-remover/
│
├── bgrmv/                  # Virtual environment (not committed)
├── images/                 # Input images (optional)
│   ├── image1.jpg
│   ├── image2.png
│   └── image3.webp
│
├── remove_backgrounds.py   # Main Python script
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
└── .gitignore              # Git ignored files
```

The `background_removed` output directory is automatically created inside the selected input folder.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/python-batch-background-remover.git
cd python-batch-background-remover
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

Python 3.11 or 3.12 is recommended.

```bash
python -m venv bgrmv
```

### 3. Activate the Virtual Environment

**Windows CMD:**

```cmd
bgrmv\Scripts\activate
```

**Windows PowerShell:**

```powershell
.\bgrmv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source bgrmv/bin/activate
```

### 4. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
rembg[cpu]
Pillow
```

## Usage

### Interactive Mode

Run the script:

```bash
python remove_backgrounds.py
```

When prompted, enter the full path of the folder containing your images:

```text
Enter the full path of the image folder: E:\MyImages
```

The script automatically detects supported images and removes their backgrounds.

### Command-Line Mode

You can also provide the folder path directly:

```bash
python remove_backgrounds.py "E:\MyImages"
```

### Recursive Processing

To process images inside subfolders as well:

```bash
python remove_backgrounds.py "E:\MyImages" --recursive
```

## Input and Output Example

**Before processing:**

```text
E:\MyImages\
│
├── product1.jpg
├── product2.jpeg
└── product3.webp
```

**After processing:**

```text
E:\MyImages\
│
├── product1.jpg
├── product2.jpeg
├── product3.webp
│
└── background_removed\
    ├── product1.png
    ├── product2.png
    └── product3.png
```

All processed images are saved in PNG format with transparent backgrounds.

The original images remain unchanged.

## Example Terminal Output

```text
Enter the full path of the image folder: E:\MyImages

Found 3 image(s).
Loading background removal model...

[1/3] OK: product1.png
[2/3] OK: product2.png
[3/3] OK: product3.png

Finished: 3/3 successful.
```

## Supported Image Formats

| Input Format | Output Format |
|--------------|---------------|
| JPG | PNG |
| JPEG | PNG |
| PNG | PNG |
| WEBP | PNG |
| BMP | PNG |
| TIFF | PNG |

## How It Works

1. The user provides an image folder path.
2. The script scans the folder for supported image files.
3. The rembg library loads an AI background removal model.
4. Each image is processed to separate the foreground from its background.
5. Processed images are saved as transparent PNG files.
6. The script displays the processing results.

## Important Notes

- An internet connection is required for the initial AI model download.
- Subsequent processing can run offline once the model is cached.
- Processing speed depends on image resolution and system hardware.
- Complex backgrounds, fine hair, and transparent objects may affect output quality.
- Large image batches may require additional RAM.

## Troubleshooting

### Virtual Environment Activation Error

Make sure the environment directory exists:

```cmd
dir bgrmv
```

If necessary, recreate it:

```cmd
python -m venv bgrmv
```

### Missing Module Error

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### Incorrect Folder Path

Make sure the provided path exists and contains supported images.

For paths containing spaces, use quotation marks when passing the path as a command-line argument.

## Future Improvements

- Graphical user interface (GUI)
- Drag-and-drop folder selection
- Background replacement with custom colors
- Image resizing and compression
- GPU acceleration support
- Progress bar for large batches
- Before-and-after image previews

## Contributing

Contributions, bug reports, and feature suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Commit your changes.
5. Open a pull request.

## License

No license is specified yet. Add a LICENSE file if you want to define how others may use, modify, and distribute this project.

---

**Python Batch Background Remover**

Automate background removal and simplify bulk image processing with Python.
