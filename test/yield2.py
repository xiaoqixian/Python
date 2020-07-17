def func():
    print("start")
    while True:
        res = yield 4
        print("res:", res)
g = func()
print(next(g))
g.send(1)
