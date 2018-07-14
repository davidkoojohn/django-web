# Fuck-Django


## dev workflow

1. 创建并激活虚拟环境

```
$ python3 -m venv venv
$ source venv/bin/activate
```
2. 更新包管理工具pip

```
(venv)$ python -m pip install --upgrade pip
```

3. install Django

```
(venv)$ pip install django

||

(venv)$ pip install django==2
```

4. 检查Django的版本

```
(venv)$ python -m django --version
(venv)$ django-admin --version

||

(venv)$ python
>>> import django
>>> django.get_version()
```

5. 使用django-admin创建项目

```
(venv)$ django-admin startproject projectName .
```

> `manage.py`： 一个让你用各种方式管理 Django 项目的命令行工具。

> `x/__init__.py`: 一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包

> `x/settings.py`: Django 项目的配置文件。

> `x/urls.py`: Django 项目的 URL 声明，就像你网站的“目录”。

> `x/wsgi.py`: 作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。


6. start server

```
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
# ---
(venv)$ python manage.py help
```

---

## create pages

1. create page(创建名为hrs（人力资源系统）的应用（注：一个项目可以包含多个应用）)

```
(venv)$ python manage.py startapp hrs
```

* `admin.py`：可以用来注册模型，让Django自动创建管理界面。
* `apps.py`：当前应用的配置
* `migrations/`：存放与模型有关的数据库迁移信息
* `models.py`：存放应用的数据模型，即实体类及其之间的关系（MVC/MVT中的M）
* `tests.py`：包含测试应用各项功能的测试类和测试函数。
* `views.py`：处理请求并返回响应的函数（MVC中的C，MVT中的V）

---

> create modal file then run makemigrations

```
(venv)$ python manage.py makemigrations hrs(package name)
```

> createsuperuser

```
(venv)$ python manage.py createsuperuser
```

## [使用ORM完成模型的CRUD操作](./ORM.CRUD.md)

```
(venv)$ python manage.py shell
```






## 参考

* [Django官方文档](https://docs.djangoproject.com/zh-hans/2.0/)


