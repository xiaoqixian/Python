### **Django模型**

安装mysql驱动，通过下列命令：

```sudo pip3 install pymysql```

#### **Django ORM**

Django自带ORM框架，所谓ORM（Object Relational Mapping），**即对象关系映射**。可以根据特定的对象执行特定的SQL语句，而不用程序员亲自去写SQL语句。缺点就是其写入的SQL语句都是固定的，难以根据特定对象进行优化。

![图来自菜鸟教程](https://www.runoob.com/wp-content/uploads/2020/05/orm-object.png)

#### **为Django配置MySQL数据库**

在配置文件settings.py文件中，找到DATABASES项：

```python
DATABASES = { 
    'default': 
    { 
        'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
        'NAME': 'hello', # 数据库名称，数据库需要事先在MySQL命令行下面创建好，django不会帮你做，除非你用的是sqlite
        'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1 
        'PORT': 3306, # 端口 
        'USER': 'root',  # 数据库用户名
        'PASSWORD': '123456', # 数据库密码
    }  
}
```

django好像默认是使用SQLite作为数据库的，现在要改为MySQL的数据库引擎。在`__init__.py`文件中加入：

```python
import pymysql
pymysql.install_as_MySQLdb()
```

同时，由于pymysql只支持Python2，所以还需要在~/.local/lib/python3.8/site-packages/django/db/backends/mysql
/base.py路径下找到如下代码并注释掉：

```python
if version < (1, 3, 13):
    raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__)
```

#### **创建APP**

通过命令`django-admin.py startapp Model`可以创建一个Model文件夹。找到settings.py文件，找到INSTALLED_APPS列表，里面有：

- django.contrib.admin：admin管理后台站点
- django.contrib.auth：身份认证系统
- django.contrib.contenttypes：内容类型框架
- django.contrib.sessions：会话框架
- django.contrib.messages：消息框架
- django.contrib.staticfiles：静态文件管理框架

加入一个刚刚创建的数据库

输入命令：

`python manage.py migrate`

migrate命令将遍历`INSTALLED_APPS`设置中的所有项目，在数据库中创建对应的表，并打印出每一条动作信息。如果你感兴趣，可以在你的数据库命令行下输入：`\dt` (PostgreSQL)、 `SHOW TABLES;`(MySQL)或 `.schema`(SQLite) 来列出 Django 所创建的表。

#### **创建模型**

在Django中，模型用类来表示，一个类代表一个数据表，类的属性则代表了数据表里面的字段。

创建一个models.py文件。

```python
from django.db import models
```

这个代码是必要的，因为类的所有的属性都是models里面的，比如如果字段ID是整数类型的：

```python
class Person(models.Model):
    ID = models.IntegerField(default = 0)
    name = models.CharField(max_length = 20)
```

#### **修改模型**

修改模型的步骤分为三步：

1. 在models.py中修改模型
2. 运行`python manage.py makemigration`，为改动创建迁移记录
3. 运行`python manage.py migrate`，讲改动同步到数据库