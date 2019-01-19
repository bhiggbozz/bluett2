from django.urls import path
from . import views

urlpatterns = [
   # path('', views.index, name='index'),
    path('', views.Logins, name='Logins'),
    #path('', views.bars, name='list'),
    path('aaah/', views.men, name='detail2'),
    path('student/view/', views.TCATT, name='catt'),
    path('teacher/subj/', views.subj_page, name='subj_details'),
    path('teacher/subj/subject/', views.subby, name='subjects'),
    path('student/CAT/', views.CAT, name='CAT'),
    path('student/weekly/', views.weekly, name='weekly'),
    path('teacher/CAT/', views.second_page, name='teacher_CAT'),
    path('teacher/CAT/scores/', views.third_page, name='scores_CAT'),
    path('student/Exam/', views.Exam, name='Exam'),
    path('chg_password/', views.Logins_pass, name='pass'),
    path('chg_username/', views.Logins_user, name='user'),
    path('student/', views.mid, name='stud'),
    path('student/<name>/', views.mid),
    path('home/', views.index),




    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
