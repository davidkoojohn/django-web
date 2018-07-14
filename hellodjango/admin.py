from django.contrib import admin
from hellodjango.models import Subject, Teacher

class SubjectAdmin(admin.ModelAdmin):
  list_display = ('no', 'name', 'intro')
  ordering = ('no',)

class TeacherAdmin(admin.ModelAdmin):
  list_display = ('no', 'name', 'intro', 'motto', 'photo', 'subject', 'manager', 'good_count', 'bad_count')
  ordering = ('no',)

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Teacher, TeacherAdmin)
