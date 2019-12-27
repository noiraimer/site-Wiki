---
layout: post
title: TensorFlow、Keras、CUDA、CuDNN 之间的版本要求
date: 2019-02-21
author: 熊猫小A
toc: ture
categories: 
  - 编程开发
  - 环境配置
tags:
  - TensorFlow
  - 深度学习
  - Keras
---

配置 Keras 深度学习环境时需要注意 TensorFlow、Keras、CuDNN(GPU) 版本间的版本配对问题。

## TensorFlow 、CUDA、CuDNN

Linux 下：

![](./assets/TensorFlow-CUDA-CuDNN-Linux.png)

Windows 下：

![](./assets/TensorFlow-CUDA-CuDNN-Windows.png)

## TensorFlow、Keras

![](./assets/TensorFlow-Keras.png)

## pip 安装指定版本

```
pip install tensorflow-gpu==1.2.0
pip install keras==2.1.1 -U --pre
```

