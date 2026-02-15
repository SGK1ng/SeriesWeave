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


def find_subdir(dir_list):
    finded_dirs = []
    for dir in dir_list:
        sub_dirs = []
        for sub_dir in os.listdir(dir):
            path = os.path.join(dir, sub_dir)
            if os.path.isdir(path):
                sub_dirs.append(path)
        finded_dirs.append(sub_dirs)
    return finded_dirs


title_list = []
for name in os.listdir(config.main_dir):
    path = os.path.join(config.main_dir, name)

    if os.path.isdir(path):
        title_list.append(path)

title_list = natural_sort(title_list)

sub_dirs = find_subdir(title_list)
title_list_with_subs = []

for i in range(len(title_list)):
    title = title_list[i]
    subs = sub_dirs[i]
    title_list_with_subs.append([title] + subs)


title_dict = {}

for dir_group in title_list_with_subs:
    cur = dir_group[0]
    title_dict[cur] = {}

    for sub_dir in dir_group[1:]:
        episodes = get_episodes(sub_dir)
        if episodes:
            title_dict[cur][os.path.basename(sub_dir)] = episodes

    episodes = get_episodes(cur)
    title_dict[cur]["root"] = episodes

playlist_files = []

while title_dict:
    cur_title = random.choice(list(title_dict.keys()))
    season_key = list(title_dict[cur_title].keys())[0]

    ep = title_dict[cur_title][season_key][0]
    playlist_files.append(ep)

    title_dict[cur_title][season_key].pop(0)

    if not title_dict[cur_title][season_key]:
        del title_dict[cur_title][season_key]

    if not title_dict[cur_title]:
        del title_dict[cur_title]

for i in playlist_files:
    print(i)

# subprocess.Popen(["vlc", "--play-and-exit"] + playlist_files)
