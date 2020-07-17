# 测试一下继承了metaclass的类在实例化时，相应的metaclass会不会执行__new__方法

class TestMetaClass(type):

    def __new__(cls, bases, name, attrs):
        print("__new__ method in metaclass")
        return type.__new__(cls, bases, name, attrs)

    def __init__(self):
        print("not much to init")

class TestClass(object, metaclass = TestMetaClass):
    pass
tc = TestClass()
