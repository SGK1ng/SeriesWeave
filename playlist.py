import copy
import os
import random

from file_utils import find_subdir, get_episodes, natural_sort


def build_title_dict(main_dir):
    title_list = []
    for name in os.listdir(main_dir):
        path = os.path.join(main_dir, name)
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

        if episodes:
            title_dict[cur]["root"] = episodes

        if not title_dict[cur]:
            del title_dict[cur]

    if not title_dict:
        raise ValueError("No video files found")

    return title_dict


def generate_playlist(title_dict):
    if not title_dict:
        raise ValueError("The episode dictionary is empty")

    title_dict = copy.deepcopy(title_dict)
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

    return playlist_files
