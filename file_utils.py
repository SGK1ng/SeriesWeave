import os
import re


def natural_sort(items):
    def generate_sort_key(item):
        parts = re.split(r"(\d+)", item)
        return [int(part) if part.isdigit() else part.lower() for part in parts]

    return sorted(items, key=generate_sort_key)


def get_episodes(path, extensions=("mp4", "avi", "mkv")):
    video_files = []
    for item in os.listdir(path):
        file = os.path.join(path, item)
        if os.path.isfile(file):
            file_extension = file.split(".")[-1].lower()
            if file_extension in extensions:
                video_files.append(file)
    return natural_sort(video_files)


def find_subdir(dir_list):
    found_dirs = []
    for dir in dir_list:
        sub_dirs = []
        for sub_dir in os.listdir(dir):
            path = os.path.join(dir, sub_dir)
            if os.path.isdir(path):
                sub_dirs.append(path)
        found_dirs.append(sub_dirs)
    return found_dirs
