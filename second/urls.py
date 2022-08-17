from django.urls import path

from . import views

app_name='second'
urlpatterns=[
    #/polls/
    path('', views.index, name='index'),
    
]
