import ctypes
import os
import subprocess

import json_loader
from context_handler import create_save, get_context, load_save
from playlist import build_title_dict, generate_playlist


def create_new_playlist():
    title_dict = build_title_dict(get_context())
    playlist = generate_playlist(title_dict)
    create_save(json_loader.save_path, playlist)
    return playlist


if __name__ == "__main__":
    try:
        if (
            os.path.exists(json_loader.save_path)
            and os.path.getsize(json_loader.save_path) > 0
        ):
            result = ctypes.windll.user32.MessageBoxW(
                0, "Saved playlist found. Continue?", "SeriesWeave", 0x03 | 0x20
            )
            if result == 6:  # Yes
                playlist = load_save(json_loader.save_path)
            elif result == 7:  # No
                playlist = create_new_playlist()
            else:  # Cancel
                exit(0)
        else:
            playlist = create_new_playlist()

        if playlist:
            match json_loader.player_path.split("/")[-1].lower():
                case "mpc-hc64.exe" | "mpc-hc.exe":
                    subprocess.Popen(
                        [
                            json_loader.player_path,
                            *playlist,
                        ]
                    )
                case "vlc.exe":
                    subprocess.Popen(
                        [
                            json_loader.player_path,
                            "--playlist-autostart",
                            *playlist,
                        ]
                    )
                case "kmplayer64.exe" | "kmplayer.exe":
                    subprocess.Popen(
                        [
                            json_loader.player_path,
                            "/play",
                            *playlist,
                        ]
                    )
                case _:
                    ctypes.windll.user32.MessageBoxW(0, "Wrong player", "Error", 0x10)

    except ValueError as e:
        ctypes.windll.user32.MessageBoxW(0, f"Data error: {e}", "Error", 0x10)
    except Exception as e:
        ctypes.windll.user32.MessageBoxW(0, f"Unexpected error: {e}", "Error", 0x10)
