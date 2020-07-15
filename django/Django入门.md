### **Django入门**

> Java后端开发实在太麻烦了，还是转Django了，毕竟Python还是应该要简单一点，希望。

#### MVC**模型**

MVC模型将软件架构分为：

* 模型（Model）：编写程序应有的功能，负责业务对象与数据库的映射
* 视图（View）：图形界面，负责与用户的交互
* 控制器（Controller）：负责转发请求，对请求进行处理

#### **MTV模型**

尽管MVC模型非常出名，但是Django采用的是MTV模型：

* M：依旧是模型
* T：模板，负责如何将HTML页面展示给用户
* V：视图

当用户通过浏览器发起一个请求，这个请求会去访问视图函数：

* 当函数不涉及数据调用，视图函数直接返回事先制定好的HTML页面；
* 如果涉及到数据调用，视图函数就继续调用模型，模型则负责去数据库查找数据，然后逐级返回

#### **Django的安装**

果然，Django直接通过pip安装就可以了。但是直接`pip install Django`会很慢，需要使用镜像。

```python
pip install django -i https://pypi.tuna.tsinghua.edu.cn/simple
```

#### **Django创建项目**

Django下载后会莫名地出现一个django-admin.py文件，这个文件是django创建项目的关键。

现在创建一个HelloWorld项目

```python
django-admin.py startproject HelloWorld
```

创建后的文件树为

```bash
.
|-- HelloWorld
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
```

目录说明：

- **HelloWorld:** 项目的容器。
- **manage.py:** 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
- **HelloWorld/__init__.py:** 一个空文件，告诉 Python 该目录是一个 Python 包。
- **HelloWorld/asgi.py:** 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目。
- **HelloWorld/settings.py:** 该 Django 项目的设置/配置。
- **HelloWorld/urls.py:** 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
- **HelloWorld/wsgi.py:** 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。

启动服务器：

```bash
python3 manage.py runserver 0.0.0.0:9090
```

在浏览器输入`localhost:9090`或者`127.0.0.1`后就可以看到django的页面了。