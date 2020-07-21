# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email       : lunar_ubuntu@qq.com
# > Create Time: Tue 21 Jul 2020 11:44:24 PM CST

# inspect是一个可以看破函数本质的神奇的库，而其中的signature方法更是可以看透函数的参数
# 让老夫来试一试

import inspect

def func(a, *args,b, **kw):
    pass

a = inspect.signature(func)

params = a.parameters

print(str(params))

for k, v in params.items():
    kind = v.kind
    print("%s: %s-> %s" % (k, v, kind))
