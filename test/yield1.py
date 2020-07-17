def foo():
    print("foo start")
    res = yield 4
    print("res:", res)

g = foo()
print(next(g))
next(g)
