import logging
import os
import sys

logger = logging.getLogger(__name__)


def get_context():
    try:
        if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
            return sys.argv[1]
        else:
            logger.warning("No directory passed or path is not a directory")
            return None
    except Exception as e:
        logger.warning(f"Some error: {e}")
        return None


def create_save(save_path, playlist):
    try:
        parent_dir = os.path.dirname(save_path)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)

        with open(save_path, "w", encoding="utf-8") as f:
            f.write("\n".join(playlist))

        logger.info(f"Playlist saved to {save_path}")

    except Exception as e:
        logger.error(f"Error saving playlist: {e}")


def load_save(save_path):
    try:
        if not os.path.exists(save_path):
            logger.warning(f"Save file does not exist: {save_path}")
            return []

        with open(save_path, "r", encoding="utf-8") as f:
            content = f.read()

        playlist = [line.strip() for line in content.split("\n") if line.strip()]

        logger.info(f"Loaded {len(playlist)} items from {save_path}")
        return playlist

    except Exception as e:
        logger.error(f"Error loading playlist: {e}")
        return []
