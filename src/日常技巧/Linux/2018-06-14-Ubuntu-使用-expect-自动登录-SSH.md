---
layout: post
title: Ubuntu 使用 expect 自动登录 SSH
date: 2018-06-14
author: 熊猫小A
toc: true
categories: 
  - 日常技巧
  - Linux
tags:
  - Linux
  - Ubuntu
  - 技巧
  - SSH
---

首先安装 expect

```
sudo apt-get install expect
```

然后创建脚本文件并给予执行权限

```
cd ~
touch autossh.sh
chmod +x autossh.sh
```

然后 `gedit autossh.sh` 编辑脚本文件，增加命令

```
#!/usr/bin/expect
spawn ssh 【name】@【server】 -p 【port】
set timeout 60 
expect "*password:"
send "【password】\r"
expect "*#"
send "cd 【somedir】\r"
interact
```

第一次使用前需要手动 SSH 登录一次，在本地保存秘钥。