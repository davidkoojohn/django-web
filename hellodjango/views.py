from django.shortcuts import render
from hellodjango.models import Subject

def index(request):
  print(Subject.objects.all())
  ctx = {'subjects': Subject.objects.all()}
  return render(request, 'hello.html', ctx)

