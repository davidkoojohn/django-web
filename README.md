# Fuck-Django

## get start

1. 创建并激活虚拟环境

```
$ python3 -m venv venv      # 创建venv虚拟环境
$ source venv/bin/activate  # 激活venv
$ deactivate                # 退出 venv
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
(venv)$ django-admin startproject projectname .
```

* `manage.py`： 一个让你用各种方式管理 Django 项目的命令行工具。
* `projectname/__init__.py`: 一个空文件，告诉 Python 这个目录应该被认为是一个 Python 包
* `projectname/settings.py`: Django 项目的配置文件。
* `projectname/urls.py`: Django 项目的 URL 声明，就像你网站的“目录”。
* `projectname/wsgi.py`: 作为你的项目的运行在 WSGI 兼容的Web服务器上的入口。

6. start server

```
(venv)$ python manage.py migrate
(venv)$ python manage.py runserver
# ---
(venv)$ python manage.py help
```

---

## create app（注：一个项目可以包含多个应用）

```
(venv)$ python manage.py startapp appname
```

* `appname/admin.py`：可以用来注册模型，让Django自动创建管理界面。
* `appname/apps.py`：当前应用的配置
* `appname/migrations/`：存放与模型有关的数据库迁移信息
* `appname/models.py`：存放应用的数据模型，即实体类及其之间的关系（MVC/MVT中的M）
* `appname/tests.py`：包含测试应用各项功能的测试类和测试函数。
* `appname/views.py`：处理请求并返回响应的函数（MVC中的C，MVT中的V）

---

# 数据库配置(usage Mysql)

1. `settings.py`

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ...
    'appname',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sql_name',
        'HOST': 'localhost',
        'PORT': 1234,
        'USER': 'root',
        'PASSWORD': '123456',
    }
}
```

2. install mysql

```
(venv)$ pip install pymysql

# Python 3需要修改项目的__init__.py

import pymysql
pymysql.install_as_MySQLdb()
```

3. `python manage.py migrate` & create database

```
mysql> drop database if exists sql_name;
mysql> create database sql_name default charset utf8;
```

1. 编辑 models.py 文件，改变模型。
2. 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
3. 运行 python manage.py migrate 来应用数据库迁移。

---

## [使用ORM完成模型的CRUD操作](./ORM.CRUD.md)

```
(venv)$ python manage.py shell

>>> from polls.models import Choice, Question
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
>>> q.question_text
>>> q.pub_date
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()

>>> Question.objects.filter(id=1)
>>> Question.objects.filter(question_text__startswith='What')
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
>>> Question.objects.get(pk=1)
>>> q.was_published_recently()

>>> q.choice_set.all()
>>> q.choice_set.create(choice_text='Not much', votes=0)
>>> q.choice_set.create(choice_text='The sky', votes=0)
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
>>> c.question
>>> q.choice_set.count()
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()
```

---

# createsuperuser

```
(venv)$ python manage.py createsuperuser
```

# add model to admin

```python
class ChoiceAdmin(admin.ModelAdmin):
  list_display = ('question', 'choice_text', 'votes')
  ordering = ('id',)
admin.site.register(Choice, ChoiceAdmin)
```

# static

```python
# setting.py
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_URL = '/static/'

# *.html
{% load static %}
<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />

{% load '***/***.***' %}
```

# [自定义后台界面和风格](https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial07/#customize-the-admin-look-and-feel)

> 在 templates 目录内创建名为 admin 的目录，随后，将存放 Django 默认模板的目录（django/contrib/admin/templates）内的模板文件 admin/***.html 复制到这个目录内。

如果你不知道 Django 源码在你系统的哪个位置，运行以下命令：

```
(venv)$ python -c "import django; print(django.__path__)"
```

# requirements.txt


```
# 生成requirements.txt
(venv)$ pip freeze > requirements.txt

# 安装requirements.txt依赖
pip install -r requirements.txt
```


## [Django模型最佳实践](https://github.com/jackfrued/Python-100-Days/blob/master/Day41-55/02.%E6%B7%B1%E5%85%A5%E6%A8%A1%E5%9E%8B.md#django%E6%A8%A1%E5%9E%8B%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5)

* 正确的为模型和关系字段命名。
* 设置适当的related_name属性。
* 用OneToOneField代替ForeignKeyField(unique=True)。
* 通过“迁移操作”（migrate）来添加模型。
* 用NoSQL来应对需要降低范式级别的场景。
* 如果布尔类型可以为空要使用NullBooleanField。
* 在模型中放置业务逻辑。
* 用<ModelName>.DoesNotExists取代ObjectDoesNotExists。
* 在数据库中不要出现无效数据。
* 不要对QuerySet调用len()函数。
* 将QuerySet的exists()方法的返回值用于if条件。
* 用DecimalField来存储货币相关数据而不是FloatField。
* 定义__str__方法。
* 不要将数据文件放在同一个目录中。




## 参考

* [Django官方文档](https://docs.djangoproject.com/zh-hans/2.0/)
  
  * [get start](https://docs.djangoproject.com/zh-hans/2.0/intro/tutorial01/)

