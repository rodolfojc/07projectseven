#3
from django.urls import path

#5
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
]
