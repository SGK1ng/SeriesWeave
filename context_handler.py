import ctypes
import os
import sys


def get_context():
    if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
        return sys.argv[1]
    ctypes.windll.user32.MessageBoxW(
        0, "No directory passed or path is not a directory", "Error", 0x10
    )
    raise ValueError("No directory provided")


def create_save(save_path, playlist):
    try:
        parent_dir = os.path.dirname(save_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        with open(save_path, "w", encoding="utf-8") as f:
            f.write("\n".join(playlist))

    except Exception as e:
        ctypes.windll.user32.MessageBoxW(
            0, f"Error saving playlist: {e}", "Error", 0x10
        )


def load_save(save_path, extensions=("mp4", "avi", "mkv")):
    try:
        with open(save_path, "r", encoding="utf-8") as f:
            content = f.read()

        playlist = [line.strip() for line in content.split("\n") if line.strip()]

        valid_playlist = []

        invalid_files = []

        for file in playlist:
            if not os.path.exists(file):
                invalid_files.append(f"Missing: {file}")
                continue
            if file.split(".")[-1].lower() not in extensions:
                invalid_files.append(f"Invalid extension: {file}")
                continue
            valid_playlist.append(file)

        if len(valid_playlist) != len(playlist):
            ctypes.windll.user32.MessageBoxW(
                0,
                f"Removed {len(playlist) - len(valid_playlist)} invalid files",
                "Error",
                0x30,
            )

        return valid_playlist

    except Exception as e:
        ctypes.windll.user32.MessageBoxW(
            0, f"Error loading playlist: {e}", "Error", 0x10
        )
        return []
