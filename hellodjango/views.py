from django.shortcuts import render
from hellodjango.models import Subject, Teacher
import requests
import json
from django.http import HttpResponse

def login(req):
  print(req)


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

def comment(request, no):
  print(request, no)

  ctx = {'code': 200}
  try:
    teacher = Teacher.objects.get(pk=no)
    if request.path.startswith('/good'):
      teacher.good_count += 1
      ctx['result'] = f'好评({teacher.gcount})'
    else:
      teacher.bad_count += 1
      ctx['result'] = f'差评({teacher.bcount})'
    teacher.save()

  except Teacher.DoesNotExist:
    ctx['code'] = 404

  print('---------')
  print(ctx)
  print('---------')

  return HttpResponse(json.dumps(ctx), content_type='application/json; charset=utf-8')

