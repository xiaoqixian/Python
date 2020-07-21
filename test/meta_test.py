# 测试一下继承了metaclass的类在实例化时，相应的metaclass会不会执行__new__方法

class TestMetaClass(type):

    def __new__(cls, name, bases, attrs):
        print("__new__ method in metaclass")
        print("cls:", cls)
        print("name: ", name)
        print("attrs: ", str(attrs))
        return type.__new__(cls, name, bases, attrs)


class TestClass(object, metaclass = TestMetaClass):

    def ___init__(self,a,b,c):
        pass
    df = 1

    def sd(self):
        print("sd")

class ChildClass(TestClass):
    ed = 1

# 当子类继承时，metaclass的__new__方法会执行两遍
t = ChildClass()
