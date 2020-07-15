### **Django深入**

> Django便捷文档：https://docs.djangoproject.com/zh-hans/2.1/topics/http/shortcuts/#django.shortcuts.render

#### path()函数

`from django.urls import path`

这里的path其实是一个函数，用于解析浏览器输入的网站目录。其格式为

```path(route, view, kwags = None, name = None)```

- route: 字符串，表示 URL 规则，与之匹配的 URL 会执行对应的第二个参数 view。
- view: 用于执行与正则表达式匹配的 URL 请求。
- kwargs: 可选参数，视图使用的字典类型的参数。
- name: 可选参数，用来反向获取 URL。

所有可以解析的页面都放在一个`urlpatterns`的列表中

```python
from django.urls import path
 
from . import views
 
urlpatterns = [
    path('hello/', views.hello),
    path('unknown/', not_found.hello)
]
```

#### **Django模板**

作为MTV类型的web框架，模板是三层中必不可少的一层。

经过我的一番测试之后，django模板作用的流程如下：

1. 在urls.py中注册函数，对于每个路径，都注册一个调用函数。函数是注册在views.py文件里面的，要从views.py里面导出。在django解析完路径后，就去注册函数字典里面找，找到之后就调用相应函数。否则返回404
2. 在views.py文件里定义一些函数，函数的参数就是request。
3. 在template里面的前端文件中，有用双花括号包围的变量，这些变量在render函数的context参数都有注明，context是一个字典。下文有更详细的介绍。

**模板用于分离文档的表现形式和内容**。

#### **render函数**

将给定的模板与给定的上下文字典组合在一起，并以渲染的文本返回一个`HttpResponse`对象。

```python
from django.shortcuts import render
render(request, template_name, context, context_type, status, using)
```

前两个参数为必选参数

* request：用于生成此响应的请求对象
* template_name：要填写模板前端文件的路径，如果已经在`settings.py`文件中写入了父文件夹的话，就只要写模板名了。
* context：要添加到模板上下文的字典，默认情况下是一个空的字典。字典的键是HTML文件中的值，值则可以是各种类型的变量，可以是字符串，列表，字典。都会在最终页面中展示出来。

### **下面介绍模板的使用技巧**

#### **过滤器**

模板语法：

`{{变量名| 过滤器: 可选参数}}`

目前可选的有：

- truncatwords：语法：`{{bio| turncatwords: "30"}}`，这个将只展示bio的前30个词。

- turncatechars：如果传入字符串的长度长于指定的长度，则截取指定长度部分。

- addslashes：添加反斜杠到任何反斜杠、单引号或者双引号前面。

- date：按指定的格式字符串参数格式化date或datetime对象。

- default：默认值，在模板文件中，可以指定一个默认值，当views.py文件中传入一些false类的值时，使用默认值，false类的值包括：

  `0  0.0  False  0j  ""  []  ()  set()  {}  None`

- length：返回传入变量的长度

- safe：由于django会自动对传入HTML文件中的标签语法进行转义，如果不想转义，可以通过safe过滤器不转。

#### **if/else标签**

if/else标签可以对传入的数进行判断后再决定展示什么，如：

```python
{% if condition1 %}
   ... display 1
{% elif condition2 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}
```

#### **for标签**

for循环标签

#### **ifequal/ifnotequal标签**

#### **注释标签**

#### **自定义标签和过滤器**

