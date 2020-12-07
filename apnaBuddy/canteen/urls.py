from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'apna-canteen'),
	path('login/', views.canteen_login, name='canteen-login'),
	path('logout/', views.canteen_logout, name='canteen-logout'),
	path('orders/', views.orders, name='canteen-orders'),
	path('history/', views.history, name='canteen-history'),
	path('bill/', views.bill, name='canteen-bill'),
]
