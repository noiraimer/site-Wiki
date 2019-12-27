---
layout: post
title: 安装 NVIDIA 驱动与配置 CUDA 开发环境
date: 2018-04-28
author: 熊猫小A
header-img: "img/post-default.jpg"
categories: 
  - 编程开发
  - 环境配置
  - Linux
tags:
 - Linux
 - CUDA
 - 环境配置
---

**Nvidia 驱动**

```
sudo add-apt-repository ppa:graphics-drivers/ppa    
sudo apt-get update    
sudo apt-get install nvidia-390 #此处要适当更改  
sudo apt-get install mesa-common-dev    
sudo apt-get install freeglut3-dev 
```

测试驱动是否安装成功：`nvidia-smi` ，若输出显卡信息则成功。

**CUDA**

官方文档：[NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#abstract)

VS Code 配置，安装 vscode-cudacpp 插件

```
{
    //CUDA
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "support.function.cuda-cpp",
                "settings":{
                    "foreground": "#56b6c2"
                }
            },
            {
                "scope": "keyword.function.qualifier.cuda-cpp",
                "settings":{
                    "foreground": "#56b6c2"
                }
            }
        ]
    }
}
```

