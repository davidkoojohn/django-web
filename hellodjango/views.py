from django.shortcuts import render
from hellodjango.models import Subject, Teacher

def index(request):
  print(Subject.objects.all())
  ctx = {'subjects': Subject.objects.all()}
  return render(request, 'hello.html', ctx)


def show(req, no):
  print('-----')
  print(no)
  print('-----')

  teachers = Teacher.objects.filter(subject__no=no)

  print(teachers)

  ctx = {'teachers': teachers}
  return render(req, 'show.html', ctx)
