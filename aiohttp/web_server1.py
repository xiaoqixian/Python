# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email       : lunar_ubuntu@qq.com
# > Create Time: Mon 20 Jul 2020 06:22:12 PM CST

# 创建一个最简单的web服务器

from aiohttp import web

async def hello(request):
    return web.Response(text="Hello, world")

async def index(request):
    return web.Response(text = "index page")

app = web.Application()
app.router.add_get('/', hello)
app.router.add_route('GET', '/index', index)
web.run_app(app)

