import json
import os
import sys

if getattr(sys, "frozen", False):
    APP_DIR = os.path.dirname(sys.executable)
else:
    APP_DIR = os.path.dirname(__file__)

CONFIG_PATH = os.path.join(APP_DIR, "config.json")

DEFAULT_CONFIG = {
    "player_path": "C:/Program Files/VideoLAN/VLC/vlc.exe",
    "save_path": "./playlist_save.txt",
    "video_extensions": ["mp4", "avi", "mkv"],
}


def load_config():
    if not os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Failed to load config: {e}")


config = load_config()

player_path = config.get("player_path", "")
save_path = config.get("save_path", "./playlist_save.txt")
video_extensions = tuple(config.get("video_extensions", ["mp4", "avi", "mkv"]))
