---
layout: post
title: 升级 CMake 与 ccmake
date: 2018-04-29
author: 熊猫小A
categories: 
  - 日常技巧
  - Linux
tags:
 - CMake
 - C/C++
 - 技巧
---

通过 `sudo apt install cmake` 安装的 CMake 往往不是最新版，使用 apt 安装的 ccmake 同理，并且不好升级。

安装最新的 CMake 与 ccmake ，首先去 [https://cmake.org/download/](https://cmake.org/download/) 下载最新的源码包，解压，进入源码目录。

```
sudo apt-get install libncurses5-dev
```

确保安装了 `libncurses5-dev` ，找到 libncurses.so 和 curses.h 所在目录，然后在 `<cmake source dir>/Modules/FindCurses.cmake` 顶部添加两条：

```
set( CMAKE_INCLUDE_PATH "/usr/include")
set( CMAKE_LIBRARY_PATH "/usr/lib/x86_64-linux-gnu/libncurses.so")
```

路径对应更改。

然后依次执行：

```
./bootstrap
make 
sudo make install
```

验证是否升级成功：

```
cmake --version
ccmake --version
```

