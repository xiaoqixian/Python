def coms():
    d = 'sd'
    while True:
        print("start")
        n = yield d
        print("n：", n)

g = coms()
g.send(None) #对于一个刚刚初始化的生成器，如果要调用send函数，必须要传送一个None,此时代码hi运行到第一个yield处。
