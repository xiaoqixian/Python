# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email      : lunar_ubuntu@qq.com
# > Create Time: Wed 07 Oct 2020 07:11:13 PM CST

import csv
from pyecharts import Pie
from pyecharts import Bar
from pyecharts import Line
from pyecharts import Scatter
from math import radians, cos, sin, asin, sqrt

filename = "/home/lunar/Documents/taxi_data.csv"

# 负责从文件中读取数据
# 传入一组画图函数
def load(*paint_funcs):
    with open(filename) as f:
        reader = csv.reader(f)
        num = 0
        total = 0
        rows = []
        for row in reader:
            rows.append(row)
        for func in paint_funcs:
            func(rows)
        total += len(rows)
        print("%d rows data processed" % (total))
        del rows
        f.close()

# 处理不同行政区出发与到达订单数量占比数据的函数
# 出发行政区和到达行政区分别在每一行的第6和第9的位置
def district_percent(rows:list):
    del rows[0]
    processed_data = [{},{}]
    for row in rows:
        if row[5] in processed_data[0]:
            processed_data[0][row[5]] += 1
        else:
            processed_data[0][row[5]] = 1
        if row[9] in processed_data[1]:
            processed_data[1][row[9]] += 1
        else:
            processed_data[1][row[9]] = 1
    attr = list(processed_data[0].keys())
    vl = list(processed_data[0].values())
    pie = Pie("各行政区离开订单数量占比", title_pos = "center")
    pie.add(
        "离开订单",
        attr,
        vl,
        radius=[40,75],
        label_text_color = None,
        is_label_show = True,
        legend_orient = "vertical",
        legend_pos = "left"
    )
    pie.render("depart_pie.html")
    attr = list(processed_data[1].keys())
    vl = list(processed_data[1].values())
    pie = Pie("各行政区到达订单数量占比", title_pos = "center")
    pie.add(
        "到达订单",
        attr,
        vl,
        radius=[40,75],
        label_text_color = None,
        is_label_show = True,
        legend_orient = "vertical",
        legend_pos = "left"
    )
    pie.render("arrive_pie.html")

# 每小时产生的订单数量, 直方图版
def orders_per_hour(rows:list):
    del rows[0]
    processed_data = [[0]*24, [0]*24]
    for row in rows:
        processed_data[0][time_process(row[2])] += 1
        processed_data[1][time_process(row[6])] += 1
    hours = list(range(24))
    bar = Bar("每小时产生的到达和离开的订单数量", title_pos = "right")
    bar.add("离开", hours, processed_data[0])
    bar.add("到达", hours, processed_data[1], xaxis_name = "时段/小时", yaxis_name = "订单数量/个")
    bar.render("bar.html")

# 每小时产生的订单数量，折线图版
def orders_per_hour2(rows:list):
    del rows[0]
    processed_data = [[0]*24, [0]*24]
    for row in rows:
        processed_data[0][time_process(row[2])] += 1
        processed_data[1][time_process(row[6])] += 1
    hours = list(range(24))
    line = Line("每小时产生的离开和到达订单数量折线图", title_pos = "right")
    line.add("离开", hours, processed_data[0], xaxis_name = "时段/小时", yaxis_name = "订单数量/个")
    line.add("到达", hours, processed_data[1], xaxis_name = "时段/小时", yaxis_name = "订单数量/个")
    line.render("line.html")

# 时间处理函数
# 根据数据中的时间，返回小时
def time_process(t:str) -> int:
    day, time = t.split(" ")
    hour, minute, sec = time.split(":")
    return int(hour)

# 订单时长的分布规律
def order_duration_distribution(rows:list):
    del rows[0]
    time_diffs = [0]*24;
    hours = [i*10 for i in range(24)]
    for row in rows:
        time_diff = time_process2(row[2], row[6], 10)
        time_diffs[time_diff] += 1
    bar = Bar("订单时长的分布规律", title_pos = "center")
    bar.add("", hours, time_diffs,  xaxis_name = "时长/min", yaxis_name = "订单数量/个", is_label_show = True)
    bar.render("duration.html")


# 根据两个时间点得到时间差,返回一个整数
# 将函数更改可以更改的时间差, diff的单位是minute
def time_process2(t1:str, t2:str, diff:int) -> int:
    day, t1 = t1.split(" ")
    day, t2 = t2.split(" ")
    h1, m1, s1 = t1.split(":")
    h2, m2, s2 = t2.split(":")
    hour_diff = int(h2) - int(h1)
    min_diff = int(m2) - int(m1)
    if int(s2) < int(s1):
        sec_diff = -1
    elif int(s2) == int(s1):
        sec_diff = 0
    else:
        sec_diff = 1
    return (60*hour_diff + min_diff + sec_diff)//diff

# 距离计算函数
# 参考: https://www.cnblogs.com/liangto/p/6287957.html
def dist_process(lon1:str, lat1:str, lon2:str, lat2:str) -> float:
    lon1, lat1, lon2, lat2 = map(radians, [float(lon1), float(lat1),float(lon2), float(lat2)])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    return 2*sin(sqrt(a))*6371*1000

# 直线距离分布函数
# 数据中最长距离74公里，最短137米
def dist_distribution(rows:list):
    del rows[0]
    dists = list(range(75))
    counts = [0]*75
    for row in rows:
        dist = int(dist_process(row[3], row[4], row[7], row[8])//1000)
        # 由于大于40公里以上的订单数量比较少
        # 所以这里将40公里以上的订单作为一个分类
        counts[dist] += 1
    line = Line("直线距离订单数量分布规律", title_pos = "center")
    line.add("", dists, counts, xaxis_name = "距离/公里", yaxis_name = "订单数量/个", is_label_show = True)
    line.render("distance.html")

def taxi_orders(rows):
    del rows[0]
    taxis = {}
    counts = {}
    for row in rows:
        if row[1] not in taxis:
            taxis[row[1]] = 1
        else:
            taxis[row[1]] += 1
    for num in taxis.values():
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    counts = sorted(counts.items(), key = lambda item: item[0])
    orders = list(map(lambda x: x[0], counts))
    counts = list(map(lambda x: x[1], counts))
    bar = Bar("所有出租车一天完成的订单数", title_pos = "center")
    bar.add("", orders, counts, xaxis_name = "一天完成订单数/个", yaxis_name = "对应出租车数/个", interval = 0)
    bar.render("taxi_orders.html")

if __name__ == "__main__":
    load(district_percent, orders_per_hour, order_duration_distribution, dist_distribution, taxi_orders)
