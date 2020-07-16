from django.db import models

# Create your models here.
# 如下面代码，Test类继承于models.Model，可以代表数据表
class Test(models.Model): #类名代表了数据库表名
    name = models.CharField(max_length=20) #name代表字段，数据类型为CharField(相当于varchar)，max_length代表限定长度
