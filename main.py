import os
import random
import re
import subprocess

import config


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


title_list = []
for dir0 in os.listdir(config.main_dir):
    path_level1 = os.path.join(config.main_dir, dir0)
    if os.path.isdir(path_level1):
        title_list.append(path_level1)
        for dir1 in os.listdir(path_level1):
            path_level2 = os.path.join(path_level1, dir1)
            if os.path.isdir(path_level2):
                title_list.append(path_level2)
title_list = natural_sort(title_list)


title_dict = {}

root_episodes = get_episodes(config.main_dir)
if root_episodes:
    title_dict[config.main_dir] = root_episodes

for title in title_list:
    episodes = get_episodes(title)
    if episodes:
        title_dict[title] = episodes


playlist_files = []
while title_dict:
    cur_title = random.choice(list(title_dict.keys()))
    ep = title_dict[cur_title].pop(0)
    playlist_files.append(ep)

    if not title_dict[cur_title]:
        del title_dict[cur_title]


print(playlist_files)

# subprocess.Popen(["vlc", "--play-and-exit"] + playlist_files)
