import shutil
from pathlib import Path

FILE_TYPES = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "documents": [".pdf", ".doc", ".docx", ".txt", ".md", ".ppt", ".pptx"],
    "audio": [".mp3", ".wav", ".ogg"],
    "video": [".mp4", ".mov", ".avi", ".mkv"],
    "archives": [".zip", ".tar", ".gz", ".rar"],
    "code": [".py", ".js", ".java", ".c", ".cpp", ".json", ".html", ".css"],
}

def categorize_file(file_path: Path) -> str:
    """Return the category directory for a file based on its extension."""
    ext = file_path.suffix.lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "other"

def organise_directory(directory: Path) -> None:
    """Organise files in the given directory into type-based folders."""
    for item in directory.iterdir():
        if item.is_file():
            category = categorize_file(item)
            target_dir = directory / category
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), target_dir / item.name)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Organise files in a directory by type")
    parser.add_argument("path", type=Path, help="Directory to organise")
    args = parser.parse_args()

    if not args.path.exists() or not args.path.is_dir():
        raise SystemExit(f"{args.path} is not a valid directory")

    organise_directory(args.path)
