from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'apna-committee'),
	path('login/', views.committee_login, name='committee-login'),
	path('logout/', views.committee_logout, name='committee-logout'),
	path('events/', views.events, name='events'),
	path('payment/<str:pk>/', views.payment, name='payment'),

]
