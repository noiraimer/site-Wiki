---
layout: post
title: 解决WPS for Linux 字体不全的问题
date: 2018-04-29
author: 熊猫小A
toc: true
categories: 
  - 日常技巧
  - Linux
tags:
  - 技巧
  - 字体
---

找一台 Windows 电脑，到 `C：/Windows/Fonts/` 路径下拷贝以下字体文件：

```
*.ttf	*.TTF	*.otf	simsun.ttc
```

到 Ubuntu 中，将以上字体文件复制到 `/usr/share/fonts/wps_symbol_fonts/`路径下，没有该路径的话就创建一个。

然后

```
sudo chmod 755 /usr/share/fonts/wps_symbol_fonts/
sudo chmod 644 /usr/share/fonts/wps_symbol_fonts/*
cd /usr/share/fonts/wps_symbol_fonts
sudo mkfontscale
sudo mkfontdir
sudo fc-cache
```

