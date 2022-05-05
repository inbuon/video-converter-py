import moviepy.editor as moviepy
import os

wmvVideos = './videos/girls/'
mp4Videos = './mp4/'
ext = '.mp4'


for x in os.listdir(wmvVideos):
    newMp4Video = x.split('.')
    clip = moviepy.VideoFileClip(wmvVideos+x)
    clip.write_videofile(mp4Videos+newMp4Video[0]+ext)