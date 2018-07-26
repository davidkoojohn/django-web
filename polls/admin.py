from django.contrib import admin

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
  list_display = ('id', 'question_text', 'pub_date')
  ordering = ('id',)

class ChoiceAdmin(admin.ModelAdmin):
  list_display = ('question', 'choice_text', 'votes')
  ordering = ('id',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)

