from django.urls import path

from . import views

urlpatterns = [
  # route, view, kwargs, name
  path('', views.index, name='index')
]
