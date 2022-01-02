> ## 简介

简称：**_adb_oprapp_**  

![](https://img.shields.io/badge/Development%20Language-Python-FF0000)  
![GitHub stats](https://github-readme-stats.vercel.app/api?username=GIS90&theme=highcontrast&show_icons=true&hide=contribs,prs&count_private=true)

ADB（Android Debug Bridge）是一种允许模拟器或已连接的Android设备进行通信的命令行工具，用这个工具可以直接操作管理Android模拟器或者真实的Android设备。


### 手机设置

1.开启指针点击位置功能：  
显示触摸操作  
指针位置


### 问题
1.failed to connect to '192.168.3.2:5555': Connection refused
- 设备开启：
  - USB调试
  - 无限调试
- 用USB线连上电脑
- 控制台执行：
```
adb tcpip 5555
adb connect 192.168.2.166
adb devices
```
- 关闭设置中"USB调试"选项, Over.

> ## 其他

### 学习参考
adb命令：https://juejin.cn/post/6844903645289398280?utm_campaign=sembaidu&utm_medium=sem_baidu_jj_pc_dc01&utm_source=bdpcjjwz04776#heading-3