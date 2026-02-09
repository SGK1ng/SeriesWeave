import os
import random
import re
import subprocess

import config


def natural_sort(items):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
    return sorted(items, key=alphanum_key)


def get_episodes(title_dir, extensions=("mp4", "avi", "mkv")):
    if title_dir == ".":
        full_path = config.main_dir
    else:
        full_path = os.path.join(config.main_dir, title_dir)

    if not os.path.isdir(full_path):
        return []

    video_files = []

    for item in os.listdir(full_path):
        item_path = os.path.join(full_path, item)

        if os.path.isfile(item_path):
            file_extension = item.split(".")[-1].lower()
            if file_extension in extensions:
                video_files.append(item)

        elif os.path.isdir(item_path):
            for subitem in os.listdir(item_path):
                subitem_path = os.path.join(item_path, subitem)

                if os.path.isfile(subitem_path):
                    file_extension = subitem.split(".")[-1].lower()
                    if file_extension in extensions:
                        video_files.append(os.path.join(item, subitem))

    return natural_sort(video_files)


title_list = [
    item
    for item in os.listdir(config.main_dir)
    if os.path.isdir(os.path.join(config.main_dir, item))
]
title_list = natural_sort(title_list)

title_dict = {}
root_episodes = get_episodes(".")
if root_episodes:
    title_dict["!"] = root_episodes

for title in title_list:
    episodes = get_episodes(title)
    if episodes:
        title_dict[title] = episodes

print(title_dict)

playlist_files = []
while title_dict:
    cur_title = random.choice(list(title_dict.keys()))
    ep = title_dict[cur_title].pop(0)
    if cur_title != "!":
        file_path = os.path.join(config.main_dir, cur_title, ep)
    else:
        file_path = os.path.join(config.main_dir, ep)
    playlist_files.append(file_path)
    if not title_dict[cur_title]:
        del title_dict[cur_title]

print(playlist_files)

# subprocess.Popen(["vlc", "--play-and-exit"] + playlist_files)
