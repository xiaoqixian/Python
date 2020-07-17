# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:21:50 2020

@author: xqx
"""


import csv

filename = "C:/Data/BusData.csv" #这里改成你存放数据的路径

STATION_INDEX = -4
DATE_INDEX = 1
WAY_INDEX = 2

results = {}
out_stations = {}
in_stations = {}

def load():

    with open(filename) as f:
        reader = csv.reader(f)
        num = 0
        total = 0
        rows = []
        for row in reader:
            rows.append(row)
            num += 1
            if num >= 100000:#一次处理10000行的数据并释放内存
                process(rows)
                del rows
                rows = []
                num = 0
                total += 100000
                print("已处理%d行数据"%(total))
        process(rows)
        f.close()

def process(rows):
    if rows[0][0] == '卡号':
        del rows[0]
    for row in rows:
        if row[WAY_INDEX] == '巴士':
            continue
        time_section = time_process(row[DATE_INDEX])

        if row[STATION_INDEX] in results:#如果结果中存在相应地铁站
            station_time_sections = results[row[STATION_INDEX]]

            if time_section in station_time_sections:
                if row[WAY_INDEX] == '地铁入站':
                    station_time_sections[time_section][0] += 1
                else:
                    station_time_sections[time_section][1] += 1
            else:
                if row[WAY_INDEX] == '地铁入站':
                    station_time_sections[time_section] = [1,0]
                else:
                    station_time_sections[time_section] = [0,1]
        else:
            if row[WAY_INDEX] == '地铁入站':
                results[row[STATION_INDEX]] = {time_section:[1,0]}
            else:
                results[row[STATION_INDEX]] = {time_section:[0,1]}



def time_process(time):
    #首先取得小时的时间
    hour = int(time[8:10])
    if hour != 23:
        return time[:10] + '-' + time[:8] + str(hour+1)
    else:
        #如果是23点的话，时间段就要到下一天了
        #本来是要判断是否到月末什么的，但是从前部分数据看来都是集中在10月份左右，先留个报警
        if time[6:8] == '30':
            raise Exception("存在30号的日期")
        date = int(time[6:8])
        return time[:10] + '-' + time[:6] + str(date+1) + '00'

def time_process2(time):
    #在全数字表示的时间中插入中文
    return time[:4] + '年' + time[4:6] + '月' + time[6:8] + '日' + time[8:10] + '点-' + time[:4] + '年' + time[4:6] + '月' + time[17:19] + '日' + time[19:21] + '点'

def output():
    op_file = 'C:/Data/result.txt'
    f = open(op_file, 'w')
    in_num = 0
    out_num = 0
    for station, times in results.items():
        in_num = 0
        out_num = 0
        f.write("地铁站：%s\n"%(station))
        for section, number in times.items():
            section = time_process2(section)
            f.write(section + '  进站:%d     出站:%d\n'%(number[0], number[1]))
            in_num += number[0]
            out_num += number[1]
        in_stations[station] = in_num
        out_stations[station] = out_num
        f.write("进站人数总计：%d  ----------------  出站人数总计：%d\n"%(in_num, out_num))
        f.write("-------------------------------------------------------------\n")
    new_in_stations = sorted(in_stations.items(), key = lambda d:d[1], reverse = True)
    new_out_stations = sorted(out_stations.items(), key = lambda d:d[1], reverse = True)

    f.write("-----------进站人数站点排序----------------\n")
    for t in new_in_stations:
        f.write("%s： %d\n"%(t[0], t[1]))
    f.write("-----------出站人数站点排序----------------\n")
    for t in new_out_stations:
        f.write("%s： %d\n"%(t[0], t[1]))

    f.close()

if __name__ == '__main__':
    load()
    output()
