# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email       : lunar_ubuntu@qq.com
# > Create Time: Mon 28 Sep 2020 07:09:58 PM CST

import math

def cal_entrpy(nums):
    res = 0
    for num in nums:
        res += num*math.log(num,2)
    return res

if __name__ == "__main__":
    print(cal_entrpy([0.9,0.1]))
