from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    path('',views.index , name ="index"),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('student/', views.student_view, name='student'),
    path('teacher/', views.teacher_view, name='teacher'),
    path('course/', views.course_view, name='course'),
    path('subject/', views.subject_view, name='subject'),
    path('assign_teacher/', views.assign_teacher_view, name='assign_teacher'),

]