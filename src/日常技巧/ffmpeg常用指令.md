---
layout: post
title: ffmpeg 常用指令
slug: ffmpeg-cheat-sheet
date: 2020-02-13 10:38
status: publish
author: 熊猫小A
categories: 
  - 
tags: 
  - ffmpeg
  - 视频处理
excerpt: 
---

**视频格式转换：**

```bash
ffmpeg -i input.flv output.mp4
```

**视频截取：**

```bash
ffmpeg -ss 00:00:00 -t 00:00:30 -i input.mp4 -vcodec copy -acodec copy output.mp4
# -ss 指定从什么时间开始
# -t 指定需要截取多长时间
# -i 指定输入文件
```

**视频去除音频：**

```bash
ffmpeg -i input.mp4 -map 0:0 -vcodec copy output.mp4
```

**视频提取音频：**

```bash
ffmpeg -i input.mp4 -f mp3 -vn output.mp3
```

**视频剪裁：**

```bash
ffmpeg -i input.mp4 -filter:v "crop=out_w:out_h:x:y" output.mp4
# out_w: 输出宽度
# out_h: 输出高度
# (x, y): 左上角坐标，横向为x轴
```

**视频拼接：**

先准备文本文件 filelist.txt，写入要合并的文件名：

```bash
file input1.mp4
file input2.mp4
file input3.mp4
```

然后：

```bash
ffmpeg -f concat -i filelist.txt -c copy output.mp4
```

注意尺寸与格式等。