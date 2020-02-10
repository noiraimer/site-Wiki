---
layout: post
title: Linux 使用 WebDAV
slug: using-webdav-on-linux
date: 2020-02-10 19:58
status: publish
author: 熊猫小A
categories: 
  - 
tags:
  - 技巧
  - Linux
  - WebDAV 
excerpt: 在 Linux 上配置与使用 WebDAV
---

Centos & Fedora & RedHat

```
yum -y install davfs2
```

其他的比如Ubuntu之类的

```
apt-get -y install davfs2
```

安装完davfs2之后执行

```
sed -i 's/# use_locks       1/use_locks       0/g' /etc/davfs2/davfs2.conf
echo "你的WebDAV地址 用户名 密码" >> /etc/davfs2/secrets #保存用户名密码，以后可以直接免密码挂载
mount.davfs 你的WebDAV地址 你想要挂载到的目录
```

即可成功挂载

注意1：挂载目录必须提前创建好！
注意2：如果你不执行第二句保存用户名密码，那么你以后挂载的时候都会要求输入用户名密码！

---

来自：[如何在各个平台下挂载WebDAV](https://moe.best/linux-memo/mount-webdav.html)。