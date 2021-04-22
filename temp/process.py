# !/usr/bin/python3
# -*- coding: utf-8 -*-
# > Author          : lunar
# > Email           : lunar_ubuntu@qq.com
# > Created Time    : Fri 12 Mar 2021 08:52:22 PM CST
# > Location        : Shanghai
# > Copyright@ https://github.com/xiaoqixian

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
font_path = "PingFang-Medium.ttf"
prop = fm.FontProperties(fname = font_path)

def import_data(file_name: str):
    index = 0
    f = open(file_name)
    flag = True
    res = list(list())
    for line in f.readlines():
        if flag:
            flag = False
            continue
        data = line.split(" ")
        temp = []
        for i in range(1, 3):
            temp.append(int(data[i]))
        res.append(temp)
    return np.array(res)

def plot(arrs, title = "None", legends = None):
    if not legends:
        return
    index = 0
    for arr in arrs:
        x = np.linspace(0, 1020, len(arr))
        plt.plot(x, arr[:,0], label = legends[index])
        index += 1
    space = [0, 90, 240, 690, 840, 1020]
    labels = ["5:30", "7:00", "9:30", "17:00","19:30", "22:30"]
    plt.xticks(space, labels=labels, rotation = 45)
    plt.xlabel("时间", fontProperties = prop)
    plt.ylabel("感染人数", fontProperties = prop)
    plt.title(title, fontProperties = prop)
    plt.legend(prop = prop)
    plt.show()

def test1():
    names = []
    for k in ["30", "70", "90"]:
        for i in ["percent.txt", "testpercent.txt"]:
            names.append(k+i)
    data = list(map(lambda x: import_data(x), names))
    legends = []
    for k in [30, 70, 90]:
        for i in ["%d%%感染者戴口罩", "单向人流%d%%感染者戴口罩"]:
            legends.append(i % k)
    plot(data, title = "出入口单双向人流不同戴口罩比例下被感染者数量变化图", legends = legends)

if __name__ == "__main__":
    test1()
