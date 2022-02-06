from . import views
from django.urls import path 

urlpatterns=[
    path('', views.index, name='index'),
    path('room', views.room, name='room')
]