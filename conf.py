# -*- coding: utf-8 -*-
"""Configuration for Wiki
"""

# For Maverick
site_prefix = "/"
source_dir = "../src/"
build_dir = "../dist/"
template = {
    "name": "Kepler",
    "type": "local",
    "path": "../Kepler"
}
index_page_size = 20
archives_page_size = 30
enable_jsdelivr = {
    "enabled": True,
    "repo": "noiraimer/site-wiki@gh-pages"
}
category_by_folder = True
for_manual_build_trigger = 1

# 站点设置
site_name = "解语知音"
site_logo = "${static_prefix}logo.png"
site_build_date = "2020/1/31 16:51"
author = "无尽藏海"
email = ""
author_homepage = "https://wiki.noiramr.cn"
description = "温故而知新"
key_words = ['blog']
language = 'zh-CN'



external_links = [
    {
        "name": "部落格",
        "url": "https://noiramr.cn",
        "brief": "温故而知新",
        "target": "_self"
    }
]
nav = [
    {
        "name": "首页",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "归档",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "关于",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
]

head_addon = r'''
<meta name="theme-color" content="#ffffff">
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//wiki.noiramr.cn" />
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/noiraimer/site-Wiki@gh-pages/css/custom.css">
<script src="https://cdn.jsdelivr.net/gh/noiraimer/Blog-With-GitHub-Boilerplate@gh-pages/js/instant.js" type="module" defer integrity="sha384-OeDn4XE77tdHo8pGtE1apMPmAipjoxUQ++eeJa6EtJCfHlvijigWiJpD7VDPWXV1"></script>
<script src="https://cdn.jsdelivr.net/gh/noiraimer/Blog-With-GitHub-Boilerplate@gh-pages/js/email-decode.min.js"></script>
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
'''

footer_addon = r'''
'''

body_addon = r'''
'''