---
layout: post
title: Ubuntu 开启 Samba 文件共享
date: 2018-04-29
author: 熊猫小A
toc: true
categories: 
  - 日常技巧
  - Linux
tags:
  - Linux
  - 技巧
  - Ubuntu
---

安装 Samba 服务：

```
sudo apt-get install samba
sudo apt-get install smbclient
```

为 Samba 服务创建用户：

```
sudo smbpasswd -a <username>
```

即可新建一个 `<username>` 账户。用户名与对应密码不必与 Linux 用户密码对应，二者间没有联系。

重启 Samba 服务：

```
sudo /etc/init.d/samba restart
```

在要共享的文件夹上右键-属性-本地网络共享，勾选共享此目录，点击创建共享。

