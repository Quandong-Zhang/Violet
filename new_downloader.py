import json
import os
import re
import shutil
import sys
import time
import base64

import requests
import yt_dlp
from PIL import Image

import title_unsearch

OWNER_NAME = "Rerange"
REMOVE_FILE=True #是否删除投稿后的视频文件

def get_double(s):
    return '"'+s+'"'

def cover_webp_to_jpg(webp_path, jpg_path):
    """
    将webp格式的图片转换为jpg格式的图片
    :param webp_path: webp格式的图片路径
    :param jpg_path: jpg格式的图片路径
    :return: None
    """
    im = Image.open(webp_path).convert('RGB')
    im.save(jpg_path, 'jpeg')
    im.close()

def download(youtube_url,folder_name):
    ydl_opts = {
        # outtmpl 格式化下载后的文件名，避免默认文件名太长无法保存
        'outtmpl': './'+str(folder_name)+'/%(id)s.mp4'
    }
 
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def get_info(url):
    ydl_opts = {
        #'proxy': 'http://127.0.0.1:10809',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info
    
def getVideoPath(id_):  
    path="./"+str(id_)
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.find(id_)!=-1:
                return os.path.join(root,file)

def download_image(url,id_):
    r = requests.get(url, stream=True)
    f = open("./"+str(id_)+"/cover.webp", "wb")
    # chunk是指定每次写入的大小，每次只写了100kb
    for chunk in r.iter_content(chunk_size=102400):
        if chunk:
            f.write(chunk)

def judge_chs(title):
    for i in title:
        if u'\u4e00' <= i <= u'\u9fa5':
            return True
    return False

def get_base64(string):
    return str(base64.b64encode(string.encode('utf-8')).decode('utf-8'))

def get_chs_title(title):
    while True:
        publish_title = get_base64(title)
        if len(publish_title)>80:
            title = title[:-1]
            continue
        else:
            return publish_title

def cut_tags(tags):
    i=0
    while len(tags)>i:
        if len(tags[i])>20:
            tags[i]=tags[i][:20]
        i+=1
    return tags

def main(vUrl,TID,plain_title=True):
    info = get_info(vUrl)
    title = info['title']
    dynamic_title = title
    author = info['uploader']
    id_ = info['id']
    description = info['description']
    tags = info['tags']
    cover = info['thumbnail']
    tags.append(author)
    tags.append(OWNER_NAME)
    # init youtube video info
    try:
        os.mkdir(path='./'+str(id_))
    except FileExistsError:
        shutil.rmtree('./'+str(id_))
    download(vUrl,id_)
    download_image(cover, id_)
    cover_webp_to_jpg("./"+str(id_)+"/cover.webp", "./"+str(id_)+"/cover.jpg")
    if plain_title:
        if judge_chs(title):
            title = get_chs_title(title)
        else:
            title=title_unsearch.plain_title(title)
    title=re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\u3040-\u31FF\uFF00-\uFFA0\u0020\u3000])", '', title)
    if len(title)>80:
        title=title[:80]
    if len(description)>250:
        description=description[:250]
    if len(tags)>10:
        tags=tags[:10]
    tags = cut_tags(tags)
    strTags = ','.join(tags)
    videoPath=getVideoPath(id_)
    CMD="./biliup upload "
    + videoPath 
    + " --desc "+get_double(description)
    + " --copyright 2 "
    + "--tag "+get_double(strTags+",youtube")
    + " --tid "+str(TID)
    + " --source "+get_double(vUrl)
    + " --line cos "
    + "--dynamic "+get_double("原标题的base64编码： "+get_base64(dynamic_title))
    + " --title "+get_double(title)
    + " --cover "+str("./"+str(id_)+"/cover.jpg")
    print("Start to using biliup,with these CMD commend:\n",CMD)
    biliupOutput="".join(os.popen(CMD).readlines())
    if biliupOutput.find("投稿成功")==-1:
        if biliupOutput.find("标题相同")==-1:
            print(biliupOutput)
            print("投稿失败,是bug或biliup出了问题。ask issues on https://github.com/Quandong-Zhang/youtube-trans-bot/issues or https://github.com/ForgQi/biliup-rs/issues ")
            exit(1)
        else:
            print("这个视频好像之前投过了的说......")
            if REMOVE_FILE:
                shutil.rmtree('./'+str(id_))
    print("投稿成功")
    if REMOVE_FILE:
        shutil.rmtree('./'+str(id_))

if __name__ == '__main__':
    #在此命令行调用该脚本，参数1为视频链接，如：https://www.youtube.com/watch?v=dQw4w9WgXcQ 参数2为TID，如：21
    main(sys.argv[1],sys.argv[2])
    exit(0)
