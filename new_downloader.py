import yt_dlp
import json
import time
import os
import re
import shutil

OWNER_NAME = "Rerange"
TID=21

def get_double(s):
    return '"'+s+'"'

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

def main(vUrl):
    info = get_info(vUrl)
    title = info['title']
    author = info['uploader']
    id_ = info['id']
    description = info['description']
    tags = info['tags']
    tags.append(author)
    tags.append(OWNER_NAME)
    os.mkdir(path='./'+str(id_))
    download(vUrl,id_)
    title=re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\u3040-\u31FF\uFF00-\uFFA0\u0020\u3000])", '', title)
    if len(title)>=80:
        title=title[:80]
    if len(description)>=250:
        description=description[:250]
    if len(tags)>=10:
        tags=tags[:10]
    CMD="./biliup upload ./"+str(id_)+"/"+str(id_)+".mp4 --desc "+get_double(description)+" --copyright 2 --tag "+get_double(str(tags)[1:-2]+",youtube")+" --tid "+str(TID)+" --source "+get_double(vUrl)+" --line cos --dynamic "+get_double("@"+str(OWNER_NAME))+" --title "+get_double(title)
    print(CMD)
    os.system(CMD)
    shutil.rmtree('./'+str(id_))

if __name__ == '__main__':
    main("https://www.youtube.com/watch?v=zXdWWHjjx4c")
    # print(json.loads(get_info("https://www.youtube.com/watch?v=-uzuhqQIaTM")))