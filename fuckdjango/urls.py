from django.contrib import admin
from django.urls import path, include

from hellodjango import views

urlpatterns = [
  path('admin/', admin.site.urls),
  # path('hrs/', include('hrs.urls')),
  # path('', include('hellodjango.urls')),

  path('', views.index),
  path('subject/<int:no>/', views.show)
]
