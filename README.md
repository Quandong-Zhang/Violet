# 「自动书记人偶/Auto Memories Doll」
把YouTube视频自动搬运到B站的机器人，依靠B站消息触发，也支持命令行调用。  
名称来源是「紫罗兰永恒花园」中的女主——薇尔莉特·伊芙加登(Violet Evergarden)。  
关于鄙人为什么要制造出这只可爱的人偶，请看下面的故事 *(出自 紫罗兰永恒花园 第一卷 上 「小说家与自动书记人偶」)* ：  
> 由这个名字引起的轰动已经是很久以前的事情了。它的制作者是Rerange，屎山代码方面的权威。  
> 起初是由于他的孝子，名为陈睿的叔叔，因后天的原因导致丧失了马。  
> 陈睿在失去马之后，因无法再进行那在他生命中举足轻重的二次元事业而变得无比消沉、日渐衰弱。  
> 无法眼睁睁地看著自己的孝子这样下去，Rerange便发明了自动书记人偶。  
> 这是一种有可以将YouTube视频全自动搬运到B站，将B站变成YouTube的天朝CDN所谓「搬运」这般功能的机械。  
> 当初为了孝子制作的机械，之后却成为了更多人的支柱，因而大受欢迎。  
> 如今，也出现了可低价租借自动书记人偶的机构。  
# 如何租借自动书记人偶（快速开始）
```shell
sudo apt install git
sudo git clone https://github.com/Quandong-Zhang/Violet.git
cd Violet
sudo bash setup.sh
./biliup login
sudo bash start.sh #在运行这行之前请先参照下文的"正经的使用方法"中的2，3步对task_manager.py 和 new_downloader.py 做出更改
```
***
# 正经的使用方法 
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
