# 常见Linux命令
## 文件操作
---
* 解压缩文件 tar xvf *.tar dst
* 查看文件个数 /bin/ls -l |grep ^-|wc -l 
## 系统状态
---
* nvidia-smi 查询显卡状态 
* 设置双系统启动项 \
1).进入ubuntu系统 \
2).打开终端。\
3).输入sudo gedit /boot/grub/grub.cfg (注意空格) \
4).成功打开 grub.cfg。\
5).set default="x"; (x为系统启动项的排列顺序)。\
* ncdu 磁盘清理工具 \
df -h 查看磁盘使用情况
## 环境配置
---
* [Linux下安装codeblocks与配置opencv](https://blog.csdn.net/u012559520/article/details/51313932)
* [Linux下输入法安装](https://blog.csdn.net/zhangjunhit/article/details/80364230)
* [Linux利用Cmake编译opencv程序](https://blog.csdn.net/w113691/article/details/79723694)
* [关于Cmake知识补充](http://blog.sina.com.cn/s/blog_8af106960102ydkm.html)
* [TX2开发板自带摄像头的使用](https://blog.csdn.net/wangyanchao151/article/details/84998606?utm_source=app,https://blog.csdn.net/piaopiaopiaopiaopiao/article/details/83342434?utm_source=app)

* [Linux下安装opencv3.4.7+contrib3.4.7](https://www.cnblogs.com/needybeerlxy/p/8979238.html)
* [cuda](https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=ubuntuu_cb&wd=opencv%E5%88%A9%E7%94%A8cuda%E5%8A%A0%E9%80%9F&oq=%25E7%25A8%258B%25E5%25BA%258F%25E8%25A8%25AA%25E5%2595%258F%25E6%25A0%25B9%25E7%259B%25AE%25E9%258C%2584&rsv_pq=b09e2b0d000052b6&rsv_t=b9d0oLqrh009J3WMCBPz4Ulrh5DJB%2BP1zeA7yc1Qnto9e1CEvj2uJVUcBKG1fPN6Ug&rqlang=cn&rsv_enter=1&rsv_dl=tb&inputT=40608&rsv_sug3=100&rsv_sug1=13&rsv_sug7=100&rsv_sug2=0&rsv_sug4=40608,https://blog.csdn.net/red_ear/article/details/82556269?from=singlemessage)

