from django.urls import path
from . import views

urlpatterns = [
    path('pathapp', views.index, name='index'),
]