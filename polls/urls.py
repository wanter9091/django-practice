from django.urls import path

from . import views

app_name='polls'
urlpatterns=[
    #/polls/
    path('', views.index, name='index'),
    #/polls/5
    path('<int:question_id>/', views.detail, name='detail'),
    #/polls/5/result/
    path('<int:question_id>/result/', views.results, name='results'),
    #/polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
