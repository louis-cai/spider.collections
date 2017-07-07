android
qichacha app
http://www.qichacha.com/

v9.0.3

---

tcpdump抓包,wireshark分析,https协议,无法看到内容,无果

charles 抓包, 看到https内容

主要:url里面有: timestamp, sign字段
header里面有: Authorization 字段

---


apktool, dex2jar, jd-gui, 反编译app apk, 360加固了

---

http://blog.csdn.net/mingzznet/article/details/51850242
找到工具,脱去360壳,得到app 源码

---

分析源码, 源码有混淆

---

sign字段,计算,有用到阿里云的SDK包,
需要分析代码,获取sign的实现算法,或者python调用java,直接调用

---


到此分析完成,开始写代码

---

直接调用java失败,阿里的sdk里面有用到android的类,在电脑运行失败

---

重新分析sign的加密方法

阿里的加密,算法太复杂,浪费时间太多

最后访问的.so 库文件, ida无法载入,需要处理


放弃










