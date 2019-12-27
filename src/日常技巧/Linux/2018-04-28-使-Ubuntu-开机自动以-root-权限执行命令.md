---
layout: post
title: 使 Ubuntu 开机自动以 root 权限执行命令
date: 2018-04-28
author: 熊猫小A
categories: 
  - 日常技巧
  - Linux
tags:
 - Linux
 - Ubuntu
 - 技巧
---

```
sudo gedit /etc/rc.local
```

在 `exit 0` 之前添加要执行的命令或者脚本。