import os
import time
import sys
import re 
import shutil
import psutil

OWNER_NAME="rerange"
TID=21
INSIDE_GFW=False
PROXY="http://127.0.0.1:10809"

if not PROXY and INSIDE_GFW:
    print("Boss,you need a proxy if the server is inside gfw. \nif not,you can't download some website's videos.\n")
    sys.exit(1)

def get_double(s):
    return '"'+s+'"'

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            yield f

def main(url):
    DESC="@"+str(OWNER_NAME)+" MEMORY FREE="+str(float(psutil.virtual_memory().free))+" TIMESPEND="
    timeStartFlag = time.time()
    os.mkdir("./"+str(timeStartFlag))
    if not INSIDE_GFW:
        os.system("./yt-dlp --get-filename -o './"+str(timeStartFlag)+"/%%(title)s.%%(ext)s'"+url)#--restrict-filenames
    else:
        os.system("./yt-dlp --get-filename -o './"+str(timeStartFlag)+"/%%(title)s.%%(ext)s' "+url+" --proxy "+PROXY)
    timeEndFlag = time.time()
    DESC+=str(timeEndFlag-timeStartFlag)
    DESC+=" STARTFLAG"+str(timeStartFlag)+""

    for i in findAllFile("./"+str(timeStartFlag)+"/"):
        global title_up
        title_up=i#init title_up
        #ANSCII's bassic range: \u0000-\uFFFF
        title_up=re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a\u3040-\u31FF\uFF00-\uFFA0\u0020\u3000])", '', title_up)
        if titleup.find(".mp4")!=-1:
            title_up=title_up[:title_up.find(".mp4")]#rempve the .mp4
        else:
            title_up=title_up[:title_up.find(".webm")]#rempve the .webm
        if len(title_up)>=80:
            title_up=title_up[:80]
        print(title_up)
        os.rename("./"+str(timeStartFlag)+"/"+i, "./"+str(timeStartFlag)+"/"+title_up+".mp4")
    if not INSIDE_GFW:
        CMD="./biliup upload ./"+str(timeStartFlag)+"/*.* --desc "+get_double(DESC)+" --copyright 2 --tag "+get_double(""+str(OWNER_NAME)+",youtube")+" --tid "+str(TID)+" --source "+get_double(url)+" --line cos --dynamic "+get_double("@"+str(OWNER_NAME)+"")
    else:
        #IN GFW
        cmd="./biliup upload ./"+str(timeStartFlag)+"/*.* --desc "+get_double(DESC)+" --copyright 2 --tag "+get_double(""+str(OWNER_NAME)+",youtube")+" --tid "+str(TID)+" --source "+get_double(url)+" --line bda2 --dynamic "+get_double("@"+str(OWNER_NAME)+"")
    os.system(CMD)
    shutil.rmtree("./"+str(timeStartFlag))

if __name__=="__main__":
    if len(sys.argv)<1:
        print("Usage: python3 downloader.py [url]")
        sys.exit(1)
    main(sys.argv[1])