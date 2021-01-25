# !/usr/bin/python3
# -*- coding: utf-8 -*-
# > Author      : lunar
# > Email       : lunar_ubuntu@qq.com
# > Created Time: 2021年01月17日 星期日 14时31分35秒
# > Location    : Shanghai
# > Copyright @ https://github.com/xiaoqixian

import matplotlib.pyplot as plt
import numpy as np

def trans_func(x, zeros, polars):
    polars = polars + 0.01
    res = 1
    for zero in zeros:
        res *= (x - zero)
    for polar in polars:
        res /= (x - polar)
    return res

# 传递函数图像测试
def transfer_func_curve(zeros_num: int, polars_num: int, func = trans_func):
    x = np.linspace(0, 20, 1000)
    #zeros = np.random.randint(-12, 12, zeros_num)
    #polars = np.random.randint(-12, 12, size = polars_num)
    zeros = np.array([-0.5])
    polars = np.array([-1, -2])
    print("polars: ", polars)
    print("zeros: ", zeros)
    y = func(x, zeros, polars)
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    transfer_func_curve(3, 4)
