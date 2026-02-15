import logging

import config
from playlist import build_title_dict, generate_playlist, print_playlist

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

if __name__ == "__main__":
    try:
        title_dict = build_title_dict(config.main_dir)
        playlist = generate_playlist(title_dict)
        print_playlist(playlist)
    except Exception as e:
        logging.error(f"{e}")
