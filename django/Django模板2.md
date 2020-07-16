### **Django模板2**

#### **配置静态文件**

1. 在项目根目录下创建statics目录

2. 在settings文件的最下方配置添加：

   ```python
   STATIC_URL = '/static/' #别名
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'statics'),
   ]
   ```

3. 在statics目录下设立css,js,images,plugins的目录，用来存放相对应的文件。

4. 把bootstrap框架放入插件目录plugins中

5. 在HTML文件的head标签中引入bootstrap

   `<link rel="stylesheet" href = "/staitc/plugins/bootstrap-3.3.7-dist/css/bootstrap.css">`

   注意这里要使用配置文件中的别名

6. 在模板使用中要加入`{% load static%}`的代码

   ```html
   {% load static %}
   {{name}}<img src="{% static "images/runoob-logo.png" %}" alt="runoob-logo">
   ```

#### **模板继承**

当两个模板HTML文件非常相近，只有模板需要改动时，这时就可以通过模板继承的方式进行导入。

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>菜鸟教程 Django 测试。</p>
    {% block mainbody %}
       <p>original</p>
    {% endblock %}
</body>
</html>
```

如图是原始的HTML文件，main block部分是可以被替换的。

```html
{%extends "base.html"%}
{% block mainbody %}
<p>继承了 base.html 文件</p>
{% endblock %}
```

只要在子文件中重新定义mainbody就可以替换了。