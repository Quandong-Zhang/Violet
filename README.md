# youtube-trans-bot
把YouTube视频自动搬运到B站的机器人，依靠B站消息触发，也支持命令行调用

# 使用方法 
1.使用biliup进行[命令行登陆](https://biliup.github.io/biliup-rs/index.html#windows-%E6%BC%94%E7%A4%BA)。  
2.将task_manager.py中的OWNER变量改为自己的mid(原来B站叫uid)。  
3.将new_downloader.py中的OWNER_NAME变量改为自己的用户名。  
4.运行。  
```shell
sudo bash setup.sh&&sudo bash start.sh 
```
# 触发消息格式 
```
$<url>$
```
如:
```
$https://www.youtube.com/watch?v=gqmsj7W2VGc$
```
直接向机器人所登陆的账号私信发送即可</br>
![image](https://user-images.githubusercontent.com/78526012/180583975-2bf90030-72b7-4da1-b700-dd82df63462b.png)
# 命令行调用方式
```shell
python3 new_downloader.py <url> <tid>
```
如:
```shell
python3 new_downloader.py https://www.youtube.com/watch?v=_0-ImzKqMO0 24
```
