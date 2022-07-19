from django.urls import path
from . import student_views as views

urlpatterns = [
    path('student/', views.home, name='student-home'),
    path('post-feedback/', views.postFeedback, name='post_feedback'),
    path('students/sem/1/delete', views.sem1StudentsDelete, name='sem1-delete'),
    path('students/sem/2/delete', views.sem2StudentsDelete, name='sem2-delete'),
    path('students/sem/3/delete', views.sem3StudentsDelete, name='sem3-delete'),
    path('students/sem/4/delete', views.sem4StudentsDelete, name='sem4-delete'),
    path('students/sem/5/delete', views.sem5StudentsDelete, name='sem5-delete'),
    path('students/sem/6/delete', views.sem6StudentsDelete, name='sem6-delete'),

]
