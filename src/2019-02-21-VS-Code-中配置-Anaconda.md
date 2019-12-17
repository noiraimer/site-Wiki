---
layout: post
title: VS Code 中配置 Anaconda
date: 2019-02-21
author: 熊猫小A
toc: ture
categories: 
  - 编程开发
  - 环境配置
tags:
  - 深度学习
  - 环境配置
  - Anaconda
---

首先安装 Anaconda 与 VS Code，以及 Python 插件。然后在 VS Code 配置文件中增加两行：

```json
"python.pythonPath": "C:\\Users\\Alan\\Anaconda3\\python.exe",
"python.condaPath": "C:\\Users\\Alan\\Anaconda3"
```

其中路径更换为自己机器上的。这样配置可以无视掉系统上的其它 Python，另外诸如代码补全以及 `import` 等都可以正常工作。