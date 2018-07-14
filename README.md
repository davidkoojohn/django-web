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
