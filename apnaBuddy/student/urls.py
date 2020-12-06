from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('student/', views.index, name = 'apna-student')
]
