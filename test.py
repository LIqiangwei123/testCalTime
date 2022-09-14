# from calculate_time import cal_time
#
# path = input()
#
# # 计算
# all_time, converted_all_time = cal_time(path)
# print(all_time)

# 获取音频文件时长
from tinytag import TinyTag

tag = TinyTag.get('F:\Desktop\\test\新月集\开篇词.m4a')
print(tag.duration)


# 获取视频文件时长
# from moviepy.editor import VideoFileClip
# clip = VideoFileClip('F:\other\极光公益喜马拉雅汇总\朝花夕拾\\123\8月31日.mov')  # 创建 from moviepy.editor import VideoFileClip 对象
# total_seconds = clip.duration # 获取时长返回的单位是秒
# print(total_seconds)
