### **异步IO**

#### **协程**

协程是一种在一个线程内，由程序员自己控制，在不同函数之间切换的机制。Python对于协程的支持是通过generator实现的。yield关键字可以用于生成generator。

#### **asyncio**

`asycio`是Python用于支持异步IO的标准库。其编程模型是一个消息循环，从`asycio`模块获取一个`EventLoop`的引用，然后把需要执行的协程扔到`EventLoop`中执行，就实现了异步IO。

```python
import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()
```

在这个程序中，首先通过`@asyncio.coroutine`的代码将hello函数标记为`coroutine`类型，这样就可以将其放到`EventLoop`中执行。在hello中，通过`asyncio.sleep(1)`来代表一些耗时比较久的操作，由于耗时较久，所以需要提前释放CPU，这时就可以通过一个`yield from`，告诉其他协程：我这里没有执行完，但是我将CPU让出来。当`yield from`返回时，`EventLoop`就会安排继续执行。

所以协程相比于多线程那种“抢CPU”的操作，协程都是每个函数都遵守“君子协定”，在自己不用CPU的时候就提前返回。这样程序就能更高效。

#### **async/await**

`async`和`await`是Python3.5以后引入的新语法。

1. 将之前代码的`@asyncio.coroutine`换成`async`
2. 将`yield from`换成`await`

```python
async def hello():
    print("hello")
    r = await asyncio.sleep(1)
    print("world")
```



