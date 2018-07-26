from django.db import models

class Question(models.Model):
  # 变量名（字段名）= 字段数据类型（验证数据，默认值）
  # ForeignKey（定义关系）
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

