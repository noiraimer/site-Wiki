---
layout: post
title: 解决 Ubuntu gnome-soft+ 占用过高 CPU 的问题
date: 2018-05-09
author: 熊猫小A
toc: true
categories: 
  - 日常技巧
  - Linux
tags:
  - 技巧
  - Linux
  - Ubuntu
---

`top` 命令发现：

```
  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND 
 2069 alan      20   0 1651248 484744  29904 R 109.0  3.0 133:04.82 gnome-soft+ 
```

gnome-soft+ 这个进程占用了大量的 CPU 资源。

解决方法：

检查 `/var/log/syslog` 这个文件，不出所料的话里面有大量的访问错误信息，例如：

```
dconf-CRITICAL **: unable to create file '/run/user/1000/dconf/user': 权限不够.  dconf will not work properly.]
```

权限上的问题，所以：

```
sudo chmod 777 /run/user/1000/dconf/user
```

即可，更多的错误继续解决就好。