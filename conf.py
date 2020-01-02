# -*- coding: utf-8 -*-
"""Configuration for Wiki
"""

# For Maverick
site_prefix = "https://wiki.imalan.cn/"
source_dir = "../src/"
build_dir = "../dist/"
template = "Kepler"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": True,
    "repo": "AlanDecode/site-Wiki@gh-pages"
}
category_by_folder = True

# 站点设置
site_name = "Panda Wiki"
site_logo = "${static_prefix}android-chrome-512x512.png"
site_build_date = "2017-06-29T12:00+08:00"
author = "熊猫小A"
email = "hi@imalan.cn"
author_homepage = "https://www.imalan.cn"
description = "熊猫小A的Wiki站点"
key_words = ['Maverick', '熊猫小A', 'Galileo', 'wiki']
language = 'zh-CN'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "Kepler",
        "url": "https://github.com/AlanDecode/Maverick-Theme-Kepler",
        "brief": "A wiki theme for Maverick"
    },
    {
        "name": "三無計劃",
        "url": "https://www.imalan.cn",
        "brief": "三是虚指。至于是哪三无，我唔知。"
    },
    {
        "name": "無文字",
        "url": "https://blog.imalan.cn",
        "brief": "熊猫小A的博客。隶属于「三无计划」。"
    },
    {
        "name": "無項目",
        "url": "https://lab.imalan.cn",
        "brief": "熊猫小A的实验室。隶属于「三无计划」。"
    },
    {
        "name": "無消息",
        "url": "https://t.me/triple_null",
        "brief": "熊猫小A的广播。隶属于「三无计划」。"
    }
]
nav = [
    {
        "name": "HOME",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "ARCHIVES",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "ABOUT",
        "url": "${site_prefix}about/",
        "target": "_self"
    },
    {
        "name": "GITHUB",
        "url": "https://github.com/AlanDecode",
        "target": "_blank"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/AlanDecode",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/AlanDecode",
        "icon": "gi gi-github"
    },
    {
        "name": "Weibo",
        "url": "https://weibo.com/5245109677/",
        "icon": "gi gi-weibo"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
<link rel="dns-prefetch" href="//static.imalan.cn" />
<link rel="stylesheet" href="${static_prefix}brand_font/embed.css" />
<style>.brand{font-family:FZCuJinLFW,serif;font-weight: normal!important;}</style>
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<link rel="apple-touch-icon" sizes="180x180" href="${static_prefix}apple-touch-icon.png?v=PY43YeeEKx">
<link rel="icon" type="image/png" sizes="32x32" href="${static_prefix}favicon-32x32.png?v=yyLyaqbyRG">
<link rel="icon" type="image/png" sizes="16x16" href="${static_prefix}favicon-16x16.png?v=yyLyaqbyRG">
<link rel="mask-icon" href="${static_prefix}safari-pinned-tab.svg?v=yyLyaqbyRG" color="#505050">
<link rel="shortcut icon" href="${static_prefix}favicon.ico?v=yyLyaqbyRG">
<meta name="application-name" content="無知識">
<meta name="apple-mobile-web-app-title" content="無知識">
<meta name="msapplication-TileColor" content="#000000">
<meta name="theme-color" content="#000000">
<meta name="baidu-site-verification" content="Or6aUYr0De" />
'''

body_addon = r'''
<script>
(function(){
    var bp = document.createElement('script');
    var curProtocol = window.location.protocol.split(':')[0];
    if (curProtocol === 'https') {
        bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
    }
    else {
        bp.src = 'http://push.zhanzhang.baidu.com/push.js';
    }
    var s = document.getElementsByTagName("script")[0];
    s.parentNode.insertBefore(bp, s);
})();
</script>
'''