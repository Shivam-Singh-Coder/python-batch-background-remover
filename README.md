# Python Batch Background Remover

A simple, locally run Python tool that removes backgrounds from every supported image in a folder and saves the results as transparent PNG files.

It uses [`rembg`](https://github.com/danielgatis/rembg) with the `u2net` model and Pillow for image handling. No API key is required.

## Features

- Processes multiple images in one folder (not subfolders).
- Supports `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tif`, and `.tiff` files (case-insensitive).
- Saves output as PNG in a `background_removed` subfolder inside the selected folder.
- Leaves the original images unchanged.
- Continues processing other images if an individual image fails.
- Prompts for a folder path and accepts paths wrapped in single or double quotes.

## Requirements

- Python installed and available as `python` (or use `python3` on systems where that is the Python command).
- An internet connection the first time the `u2net` model is needed so it can be downloaded. Once cached, model processing can work offline.

Dependencies are listed in `requirements.txt`:

```text
rembg[cpu]
Pillow
```

## Installation

Clone the repository and enter its directory:

```bash
git clone https://github.com/Shivam-Singh-Coder/python-batch-background-remover.git
cd python-batch-background-remover
```

Optionally create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the script:

```bash
python remove_backgrounds.py
```

When prompted, enter the path to the folder containing the images:

```text
Enter the full path of the image folder: "C:\Users\you\Pictures\products"
```

The script scans files directly in that folder, loads the `u2net` model, and writes the results to `background_removed` inside the input folder.

## Example

Before:

```text
products/
├── mug.jpg
├── shirt.png
└── logo.webp
```

After running the script:

```text
products/
├── mug.jpg
├── shirt.png
├── logo.webp
└── background_removed/
    ├── mug.png
    ├── shirt.png
    └── logo.png
```

When two input files would produce the same output name (for example, `photo.jpg` and `photo.png`), the later output uses the input extension in its name, such as `photo_jpg.png`. Existing outputs may be replaced when the script is run again.

Example terminal output:

```text
Enter the full path of the image folder: C:\Users\you\Pictures\products
Found 3 image(s). Loading AI model...
[1/3] OK: logo.webp -> logo.png
[2/3] OK: mug.jpg -> mug.png
[3/3] OK: shirt.png -> shirt.png
Finished: 3/3 successful. Output: C:\Users\you\Pictures\products\background_removed
```

## Notes

- The script does not scan subfolders or accept a folder path as a command-line argument; it asks for the path interactively.
- Processing time depends on image size and computer hardware. Large batches may use substantial memory.
- Results can vary, especially for fine details, complex backgrounds, or transparent objects.

## Troubleshooting

### `Invalid folder` or no supported images found

Check that the folder path is correct and that the supported image files are directly inside the folder (not only in subfolders).

### Missing module error

Activate your virtual environment if you created one, then install the dependencies:

```bash
python -m pip install -r requirements.txt
```

### Model download or network error

The model may need to download the first time it runs. Check your internet connection and run the script again.

## Contributing

Bug reports, suggestions, and pull requests are welcome.

## License

No license is specified yet. Add a `LICENSE` file to define how this project may be used, modified, and distributed.
