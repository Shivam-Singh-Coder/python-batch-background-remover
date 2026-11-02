from pathlib import Path

from PIL import Image
from rembg import new_session, remove

SUPPORTED = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tif', '.tiff'}


def main():
    raw_path = input('Enter the full path of the image folder: ').strip().strip('"').strip("'")
    folder = Path(raw_path).expanduser()
    if not folder.is_dir():
        print(f'Invalid folder: {folder}')
        return

    output = folder / 'background_removed'
    images = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED)
    if not images:
        print('No supported images found in the folder.')
        return

    output.mkdir(exist_ok=True)
    print(f'Found {len(images)} image(s). Loading AI model...')
    session = new_session('u2net')
    successful = 0
    for i, image_path in enumerate(images, 1):
        try:
            with Image.open(image_path) as image:
                result = remove(image.convert('RGBA'), session=session)
                target = output / f'{image_path.stem}.png'
                if target.exists():
                    target = output / f'{image_path.stem}_{image_path.suffix[1:].lower()}.png'
                result.save(target, format='PNG')
            successful += 1
            print(f'[{i}/{len(images)}] OK: {image_path.name} -> {target.name}')
        except Exception as exc:
            print(f'[{i}/{len(images)}] FAILED: {image_path.name}: {exc}')

    print(f'Finished: {successful}/{len(images)} successful. Output: {output}')


if __name__ == '__main__':
    main()
