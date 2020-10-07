# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email      : lunar_ubuntu@qq.com
# > Create Time: Wed 07 Oct 2020 08:34:21 PM CST

from pyecharts import Pie

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
v2 = [19, 21, 32, 20, 20, 33]
pie = Pie("饼图-玫瑰图示例", title_pos='center', width=900)
pie.add("商品A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
pie.add("商品B", attr, v2, center=[75, 50], is_random=True, radius=[30, 75], rosetype='area',
        is_legend_show=False, is_label_show=True)
pie.render("bar.html")
