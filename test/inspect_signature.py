# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# > Author     : lunar
# > Email       : lunar_ubuntu@qq.com
# > Create Time: Tue 21 Jul 2020 11:44:24 PM CST

# inspect是一个可以看破函数本质的神奇的库，而其中的signature方法更是可以看透函数的参数
# 让老夫来试一试

import inspect

def func(a, *, b,c) -> str:
    return 1

def has_request_arg(fn):
     sig = inspect.signature(fn)
     params = sig.parameters
     found = False
     for name, param in params.items():
         print("loop")
         if name == 'request':
             print("request")
             found = True
             continue
         if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.     kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.         VAR_KEYWORD):
             raise ValueError('request parameter must be the last named parameter    in function: %s%s' % (fn.__name__, str(sig)))
     return found

def fun(request, *, name, summary, content):
    pass

print(has_request_arg(fun))

