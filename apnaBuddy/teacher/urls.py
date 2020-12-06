from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'apna-teacher'),
	path('login/', views.teacher_login, name='teacher-login'),
]
