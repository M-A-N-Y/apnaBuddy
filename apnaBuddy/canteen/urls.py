from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'apna-canteen'),
	path('login/', views.login, name='canteen-login'),
	path('orders/', views.orders, name='canteen-orders'),
	path('history/', views.history, name='canteen-history'),


]
