
#作为ORM框架，向数据库添加数据需要创建对象，然后执行save函数，相当于SQL中的INSERT

from django.http import HttpResponse

from Model.models import Test

def testdb(request):
    test1 = Test(name='hello')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
