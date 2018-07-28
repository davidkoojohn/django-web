from django.contrib import admin

from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
  # 通过 TabularInline（替代 StackedInline ），关联对象以一种表格式的方式展示，显得更加紧凑
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('id', 'question_text', 'pub_date', 'was_published_recently')
  # ordering = ('id',)

  inlines = [ChoiceInline]
  # “过滤器”侧边栏
  list_filter = ['pub_date']

  # 查询数据
  search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
  list_display = ('question', 'choice_text', 'votes')
  ordering = ('id',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

