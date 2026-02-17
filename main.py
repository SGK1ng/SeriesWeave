import ctypes
import os

import config
from context_handler import create_save, get_context, load_save
from playlist import build_title_dict, generate_playlist


def create_new_playlist():
    title_dict = build_title_dict(get_context())
    playlist = generate_playlist(title_dict)
    create_save(config.save_path, playlist)
    return playlist


if __name__ == "__main__":
    try:
        if os.path.exists(config.save_path) and os.path.getsize(config.save_path) > 0:
            result = ctypes.windll.user32.MessageBoxW(
                0, "Saved playlist found. Continue?", "SeriesWeave", 0x03 | 0x20
            )
            if result == 6:  # Yes
                playlist = load_save(config.save_path)
            elif result == 7:  # No
                playlist = create_new_playlist()
            else:  # Cancel
                exit(0)
        else:
            playlist = create_new_playlist()

        print(playlist)

    except ValueError as e:
        ctypes.windll.user32.MessageBoxW(0, f"Data error: {e}", "Error", 0x10)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f"Unexpected error: {e}", "Error", 0x10)
