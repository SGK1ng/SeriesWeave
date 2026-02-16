import logging
import os

import config
from context_handler import create_save, get_context, load_save
from playlist import build_title_dict, generate_playlist, print_playlist

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

if __name__ == "__main__":
    try:
        playlist = load_save(config.save_path)
        if not playlist:
            title_dict = build_title_dict(config.main_dir)
            playlist = generate_playlist(title_dict)
            create_save(config.save_path, playlist)

    except ValueError as e:
        logging.error(f"Data error: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}", exc_info=True)
