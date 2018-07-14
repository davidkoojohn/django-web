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
