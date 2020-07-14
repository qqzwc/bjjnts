# 环境配置：
1.有Python环境
* 安装selenium库
* 安装FireFox version>=60
* geckodriver和WatchBot.py需位于同一目录

2.没有Python环境
* 安装Python环境，然后参考1
* 不想安装Python环境，等我打包exe

# 使用方法：
在设备管理器中禁用系统自带的摄像头，安装VCam，拖一张自拍进去，点击播放键，运行WatchBot.py，在打开的页面中登录并进入课程视频播放页面，给予摄像头权限（勾选remember this decision），这时你看到的应该是拖进VCan的那张照片，点击人脸识别对话框中的开始验证，视频开始播放后返回程序输入ok，你就可以去做自己喜欢的事了，WatchBot会帮你处理接下来的事。

# 已知问题：
* 有时上一级播放完了下一集未解锁，需要重新运行
* 网络较差出现视频格式错误，需要重新运行