# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email      : lunar_ubuntu@qq.com
# > Create Time: Wed 07 Oct 2020 07:11:13 PM CST

import csv
from pyecharts import Pie
from pyecharts import Bar

filename = "/home/lunar/Documents/taxi_data.csv"
# processed_data = [{}, {}]

def load(process):
    with open(filename) as f:
        reader = csv.reader(f)
        num = 0
        total = 0
        rows = []
        for row in reader:
            rows.append(row)
        process(rows)
        total += len(rows)
        print("%d rows data processed" % (total))
        del rows
        f.close()

# 处理不同行政区出发与到达订单数量占比数据的函数
# 出发行政区和到达行政区分别在每一行的第6和第9的位置
def process_percent(rows):
    if not processed_data:
        raise Exception("processed_data is None")
    if rows[0][1] == 'CARID':
        del rows[0]
    for row in rows:
        if row[5] in processed_data[0]:
            processed_data[0][row[5]] += 1
        else:
            processed_data[0][row[5]] = 1
        if row[9] in processed_data[1]:
            processed_data[1][row[9]] += 1
        else:
            processed_data[1][row[9]] = 1

# 将已经处理好的数据进行绘图的函数
def echarts_perent(pd):
    attr = pd[1].keys()
    vl = pd[1].values()
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
    pie.render("bar.html")

def orders_per_hour(rows):
    del rows[0]
    processed_data = [[0]*24, [0]*24]
    for row in rows:
        processed_data[0][time_process(row[2])] += 1
        processed_data[1][time_process(row[6])] += 1
    hours = list(range(24))
    bar = Bar("每小时产生的到达和离开的订单数量")
    bar.add("离开", hours, processed_data[0])
    bar.add("到达", hours, processed_data[1])
    bar.render("bar.html")

def time_process(t):
    day, time = t.split(" ")
    hour, minute, sec = time.split(":")
    return int(hour)

if __name__ == "__main__":
    load(orders_per_hour)
