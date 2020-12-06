from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('committee/', views.index, name = 'apna-committee')
]
