### **Python装饰器**

> 装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象。它经常用于有切面需求的场景如：插入日志、性能测试、事务处理、缓存、权限校验等场景。
>
> 有了装饰器，我们可以抽离出大量与函数功能本身无关的雷同代码并继续重用。

众所周知，Python允许在函数里面定义函数，如果我们有一个函数func，这时需要在函数运行中间打印日志。如果直接加入日志打印的代码当然方便，但是如果非常多的函数都需要这个功能的话就不方便了。这时，我们可以这样写：

```python
def func():
    #do something
    
def log(func):
    def wrapper(*args, **kwargs):
        logging.warn("this is the log function") #正式打印日志的函数
        return func(*args)
    return wrapper

#神操作来了。这时我们发现：如果再令func = log(func)的话就可以实现通过一个函数的包装的方式来加一行代码，
#而且不会破坏函数原来的代码结构
func = log(func)
func() #这时候如果打印func.__name__的话将会显示wrapper
```

而我们经常见到的装饰器都是通过`@`语法糖实现的：

```python
@log
def func():
    #do something
#这里的@log就直接等于func = log(func)
```

这都要归功于万能的Python允许将函数如同变量一样传来传去，并且允许函数里面定义函数。C语言虽然允许传递函数指针，但是不允许函数套函数。

#### **带参数的装饰器**

在上述代码中，装饰器函数本身只允许带有一个参数，就是需要装饰的那个函数。而通过再一层的包装，可以实现带参数的装饰器：

```Python
def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                loggin.warn("%s is running"%func.__name__)
            return func(*args)
        return wrapper
    return decorator

@log(level = "warn")
def func():
    #do something
func()
```

#### **类装饰器**

在类的内部，通过私有函数\__call__的可以实现装饰器，当通过@形式加装装饰器时，就会调用这个方法。

```python
class Foo(object):
    def __init__(self, func):
        self._func = func
    def __call__(self):
        #do something
        self._func()
        #do something
@Foo
def func():
    #do something
```

#### **functools.wraps**

由于装饰器设计函数的变换，看起来是同一个函数，但实际是名字一样，函数变了。所以函数的元信息也没了。

通过functools.wraps可以把原函数的元信息拷贝到装饰器函数中

```python
from functools import wraps
def log(func):
    @wraps(func)
    def with_log(*args, **kwargs):
        return func(*args, **kwargs)
    return with_log

```

#### **内置装饰器**

`@staticmethod  @classmethod @property`

