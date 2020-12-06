from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'apna-committee'),
	path('login/', views.committee_login, name='committee-login'),

]
