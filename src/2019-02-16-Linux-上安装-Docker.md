---
layout: post
title: Linux 上安装 Docker
date: 2019-02-16
author: 熊猫小A
toc: ture
categories: 
  - 编程开发
  - 环境配置
  - Linux
tags:
  - Linux
  - 环境配置
---

## CentOS 安装 Docker

系统要求：

* CentOS 7 （64bit）
* CentOS 6.5 （64bit）或更高

安装必要工具：

```bash
sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```

添加软件源：

```bash
sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
```

更新 yum 缓存：

```bash
sudo yum makecache fast
```

安装 Docker-ce

```bash
sudo yum -y install docker-ce
```

启动 Docker 后台服务：

```bash
sudo systemctl start docker
```

测试安装：

```bash
docker run hello-world
```

此时会拉取一个 hello-world 镜像，并输出以下字样：

```bash
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

## Ubuntu 安装 Docker

获取安装包：

```bash
cd ~ && wget -qO- https://get.docker.com/ | sh
```

若要以非 root 身份（例如 alan）运行 Docker，需要：

```bash
sudo usermod -aG docker alan
```

启动后台服务

```bash
sudo service docker start
```

测试：

```bash
docker run hello-world
```

效果同上。