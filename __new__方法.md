
### **Python `__new__`方法理解**

python面向对象机制里有一个非常神奇的静态方法叫`__new__`。

> 其实对于Python这种脚本语言我是不想花时间钻研这么深的，但是项目经常遇见，所以还是得过来了解一下。

首先，这个方法在默认情况下是继承了父类的。如果本类不去覆盖的话，就是一直使用父类的这个方法。

如果子类要去覆盖，那么首先要满足一个条件：**返回一个本类的示例**。为什么呢？因为`__new__`比`__init__`更早被调用，`__init__`是需要接受一个实例的，该方法本身并不产生实例。相信很多人都和我一样，一直认为`__init__`方法就如同Java/C++等语言中的构造器一样。然而，`__init__`真的只是接受参数并init一下。

好了说回`__new__`方法。先看下面的这个代码：

```python
#引自C语言中文网
class demoClass:
    instances_created = 0

    def __new__(cls,*args,**kwargs):
        print("__new__():",cls,args,kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instances_created
        cls.instances_created += 1
        return instance

    def __init__(self,attribute):
        print("__init__():",self,attribute)
        self.attribute = attribute

test1 = demoClass("abc")
test2 = demoClass("xyz")
print(test1.number,test1.instances_created)
print(test2.number,test2.instances_created)
```
这段代码的输出为：
```python
__new__(): <class '__main__.demoClass'> ('abc',) {}
__init__(): <__main__.demoClass object at 0x0000026FC0DF8080> abc
__new__(): <class '__main__.demoClass'> ('xyz',) {}
__init__(): <__main__.demoClass object at 0x0000026FC0DED358> xyz
0 2
1 2
```
看到没有？在`__new__`方法中输出的都是class，而在`__init__`方法中输出的是object。一个是类，一个是对象。

同时，观察一下`test.number`和`test.instance_created`这两个属性有什么不同？

一个是类的属性，一个是对象的属性。对象的属性是在每个对象实例化时所决定的，与其它的对象并无关联。
而类的属性是所有实例化对象所共享的，并且可以动态变化的。

### **Metaclass元类**

既然讲到了`__new__`方法，感觉不讲Metaclass都对不起自己。

众所周知，在创建一个Python类的时候，类名有时可以带一个括号，里面的类表示要被继承的。
但是很少有人知道括号里还可以指定一个metaclass，就像这样：
`class Student(Person, metaclass = ManMetaclass):`

要创建一个元类，必须满足下列条件：
1. 必须显式地继承自type类；
2. 类中需要定义并实现`__new__`方法，且一定要返回一个该类的实例对象。

创建一个元类：
```python
#定义一个元类
class FirstMetaClass(type):
    # cls代表动态修改的类
    # name代表动态修改的类名
    # bases代表被动态修改的类的所有父类
    # attr代表被动态修改的类的所有属性、方法组成的字典
    def __new__(cls, name, bases, attrs):
        # 动态为该类添加一个name属性
        attrs['name'] = "C语言中文网"
        attrs['say'] = lambda self: print("调用 say() 实例方法")
        return super().__new__(cls,name,bases,attrs)
```
这时，如果创建一个继承该元类的类，即使不写任何东西，依旧拥有name的属性和say方法。

> 对于MetaClass元类，一般用于创建API，几乎不会使用到它
