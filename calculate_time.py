"""
input : 文件路径
output1 : 以秒为单位的总时间
output2 : 以 H:M:S 为格式的时间
另会导出excel文件
"""

import os
import pandas as pd
import datetime
from tinytag import TinyTag
from moviepy.editor import VideoFileClip


def get_filelist(target_dir, Filelist):
    """
    # 遍历文件夹及其子文件夹中的文件，并存储在一个列表中
    # 输入文件夹路径、空文件列表[]
    # 返回 文件列表Filelist,包含文件名（完整路径）
    :param target_dir:
    :param Filelist:
    :return:
    """
    newDir = target_dir

    if os.path.isfile(target_dir):

        Filelist.append(target_dir)

        # # 若只是要返回文件文，使用这个

        # Filelist.append(os.path.basename(dir))

    elif os.path.isdir(target_dir):

        for s in os.listdir(target_dir):
            # 如果需要忽略某些文件夹，使用以下代码

            # if s == "xxx":

            # continue

            newDir = os.path.join(target_dir, s)

            get_filelist(newDir, Filelist)

    return Filelist


def to_excel(file_name_list, file_time_list):
    """
    将文件名列表和文件时长列表合并并导出到excel文件
    :param file_name_list:
    :param file_time_list:
    :return:
    """
    to_excel_list = zip(file_name_list, file_time_list)  # 合并列表

    # list转dataframe
    df = pd.DataFrame(to_excel_list, columns=['音频标题', '录制时长'])

    # 保存到本地excel
    now = datetime.datetime.now()
    df.to_excel("time" + str(now.strftime("%Y_%m_%d_%H_%M_%S")) + ".xlsx", index=False)


def time_convert(old_time):
    """
    时间格式转换
    :param old_time: 以秒为单位的时间
    :return: 转换为 %d:%02d:%02d 格式的时间
    """
    m, s = divmod(old_time, 60)
    h, m = divmod(m, 60)
    new_time = "%d:%02d:%02d" % (h, m, s)
    return new_time


# 支持的文件格式
music_format = ['.m4a', '.mp3', '.wav']

video_format = ['.mp4', '.mov', '.avi']


def get_music_time(music_filepath):
    tag = TinyTag.get(music_filepath)
    return tag.duration


def get_video_time(video_filepath):
    clip = VideoFileClip(video_filepath)
    return clip.duration


def cal_time(filepath):
    # 加最后的文件符
    filepath = filepath + '\\'
    # 获取文件路径列表
    my_file_list = get_filelist(filepath, [])  # input

    # 初始化时间列表
    time_list = []
    converted_time_list = []

    final_file_list = []

    # 循环计算时间
    for file in my_file_list:
        time = 0
        if (str(file[-4:])) in music_format:
            # 获取每一个音频文件的时间，单位是秒
            time = get_music_time(file)

        if (str(file[-4:])) in video_format:
            # 获取每一个视频文件的时间，单位是秒
            time = get_video_time(file)
        if time != 0:
            # 添加文件及其对应的时间
            time_list.append(time)
            final_file_list.append(file)

            # 将每一个音频的时间转换为另一格式
            converted_time = time_convert(time)
            converted_time_list.append(converted_time)

    # 计算总时间
    all_time = round(sum(time_list), 3)  # output1

    # 转换后的总时间
    converted_all_time = time_convert(all_time)  # output2

    # 处理列表
    # 文件路径列表转换为文件名列表
    converted_file_list = [i.split('\\')[-1][:-4] for i in final_file_list]

    # 输出到excel文件
    to_excel(converted_file_list, converted_time_list)

    return all_time, converted_all_time
