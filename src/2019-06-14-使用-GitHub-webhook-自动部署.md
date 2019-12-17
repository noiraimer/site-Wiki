---
layout: post
title: 使用 GitHub webhook 自动部署
date: 2019-06-14 09:20
author: 熊猫小A
toc: true
categories: 
  - 日常技巧
  - Linux
tags:
  - 技巧
  - Linux
  - Git
  - PHP
---

我的三个静态站点：[三無計劃](https://www.imalan.cn)，[無知識](https://wiki.imalan.cn)，[無項目](https://lab.imalan.cn)均使用 Travis-CI 自动构建。在此之前，三个站点都托管在 GitHub Pages 或者 Coding Pages 上，但前者在大陆速度缓慢，后者时常抽风，总体表现都不如我自己的服务器，因此决定将站点放在自己这里。

GitHub webhook 可在仓库发生某些事件（例如 push）时向某指定 URL 发起 POST 请求，请求 body 就是详细的 push 事件内容，因此可以在服务器上根据请求部署站点，比如直接从 Github 拉取最新源码然后构建，或者由 CI 服务构建好之后拉取最新的 build 到服务器上。

---

首先保存以下 PHP 到服务器上可从外部访问的地方，并在 Github 对应仓库设置中添加一个 hook，URL 就填该 PHP 的网址，例如 `https://api.imalan.cn/somepath/hook.php`。

```php
<?php
/**
 * GitHub Webhook 服务端处理
 * 根据 Repo 与 Branch 的 push 事件运行脚本
 * 
 * @author 熊猫小A | AlanDecode
 * @link https://www.imalan.cn
 */

function run($data, $config) {
    foreach ($config['endpoints'] as $endpoint) {
        // check repository and branch
        if ($data['repository']['full_name'] != $endpoint['repo']) {
            continue;
        }
        if ($data['ref'] != 'refs/heads/' . $endpoint['branch']) {
            continue;
        }

        // excute
        try {
            echo shell_exec($endpoint['run']);
            echo $endpoint['action'];
        } catch (Exception $e) {
            echo $e->getMessage();
        }
    }
}

try {
    // data
    $rawInput = file_get_contents('php://input');
    $data = json_decode($rawInput, true);

    // config
    $config_path = __DIR__.'/config.json';
    if (!file_exists($config_path)) {
        throw new Exception("Can't find ".$config_path);
    }
    $config = json_decode(file_get_contents($config_path), true);
    
    // verify
    if (!empty($config['key'])) {
        if (!isset($_SERVER['HTTP_X_HUB_SIGNATURE'])) {
            die('No signature presented.');
        }

        list($algo, $hash) = explode('=', $_SERVER['HTTP_X_HUB_SIGNATURE'], 2);
        $signature = hash_hmac($algo, $rawInput, $config['key']);

        if ($signature != $hash) {
            die("Signature doesn't match.");
        }
    }
    
    // excute
    run($data, $config);

} catch (Exception $e) {
    echo $e->getMessage();
}
```

在同一目录下创建 config.json 文件，形如：

```json
{
    "key": "xxxxxxxx",
    "endpoints": [
        {
            "repo": "AlanDecode/some-Repo",
            "branch": "build",
            "action": "Deploy site from latest build.",
            "run": "/path/to/your.sh"
        }
    ]
}
```

其中，`key ` 字段用于鉴权，自己设置一个，然后填写到 GitHub webhook 设置的 secret 字段那里。这是可选的，但建议设置。

`endpoints` 中保存了所有要处理的东西。`repo` 是仓库名，`branch` 是分支名，`action` 是备注，可以随意填，`run` 填写要运行的脚本文件路径。

脚本可以很简单：

```shell
#!/bin/bash
cd /home/sites/wiki.imalan.cn && git pull --rebase
```

……也可以很复杂，不演示了。

---

实际上，还有可能遇到权限问题，另开一篇说。