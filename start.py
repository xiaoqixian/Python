# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email      : lunar_ubuntu@qq.com
# > Create Time: Wed 07 Oct 2020 04:29:18 PM CST

from pyecharts.charts import Bar
from pyecharts.render import make_snapshot

# use snapshot_selenium to help rendering
from snapshot_selenium import snapshot

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
# render 会生成本地 HTML 文件，默认会在当前目录生成 render.html 文件
# 也可以传入路径参数，如 bar.render("mycharts.html")
make_snapshot(snapshot, bar.render(), "bar.png")
