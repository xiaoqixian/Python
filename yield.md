### **yield**

yield是一个在异步IO和协程编程中经常使用的关键字。

**初步理解**

使用了yield关键字的函数就不再是一个函数了，而是一个生成器（generator）。当直接使用函数名加括号运行时，函数实际并不会运行，而是返回一个生成器，这时需要一个变量来承接。

要想函数运行，需要借助next函数。

```python
def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
"""output
starting...
4
********************
res: None
4
"""

"""————————————————
版权声明：本文为CSDN博主「冯爽朗」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/mieleizhi0522/java/article/details/82142856"""
```

在上面的代码中，g就是一个生成器，当使用next函数调用g时，程序会一直运行，知道遇到yield关键字，然后返回，这里说的返回和return是等效的。但是函数并没有真正的结束，而是**停在了yield处**。所以继续调用next函数，从yield处开始运行，由于res右边的结果在上一次运行时return出去了，所以res实际没有被赋值。所以就会输出一个None。

生成器和迭代器很像，但是又不像。迭代器要想获得，必须先要对象有实现。但是yield自己就可以生成生成器，而且每一次next，yield占用的内存都会被释放。在用于读取大量的文件时，非常实用。

#### **send**

send函数是另一个在使用yield时经常使用的函数。在上文中提到，如果直接使用next函数调用生成器时，如果yield前面有变量承接，则变量会无法被正确赋值。这时就可以使用send函数进行赋值。

如下面代码：

```python
def func():
    print("start")
    while True:
        res = yield 4
        print("res:", res)
g = func()
print(next(g))
g.send(1)

"""output
start
4
res: 1
"""
```

可以看到，res的值不再是None，而是通过send函数传过去的1。

#### **yield from**

yield from后面接一个迭代器或者生成器，被称为**委托生成器**。实际就相当于将另一个函数的生成器的yield搬到本函数。如：

```python
def gen():
    yield "haha"
    yield "gaga"

def foo():
    yield from gen()


f = foo()
print(f.__next__())  # f调用__next__是直接和gen通信的，不需要通过foo
```

总之，yield是返回一个一般的变量，yield from则是将一个生成器变量的yield返回给yield出来。