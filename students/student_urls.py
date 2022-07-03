from django.urls import path
from . import student_views as views

urlpatterns = [
    path('student/', views.home, name='student-home'),
    path('post-feedback/', views.postFeedback, name='post_feedback'),
]
