from django.urls import path
from hellodjango import views

urlpatterns = [
  path('', views.login),
  path('subject/', views.index),
  path('subject/<int:no>/', views.show),
  path('good/<int:no>/', views.comment),
  path('bad/<int:no>/', views.comment),
]


