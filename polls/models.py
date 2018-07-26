import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
  # 变量名（字段名）= 字段数据类型（验证数据，默认值）
  # ForeignKey（定义关系）
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  # 给模型增加 __str__() 方法是很重要的,不仅仅能给你在命令行里使用带来方便，自动生成的 admin 里也使用这个方法来表示对象。
  def __str__(self):
    return self.question_text

  # 添加自定义的方法
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text

