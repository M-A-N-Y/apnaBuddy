from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'apna-student'),
	path('login/', views.student_login, name='student-login'),
	path('logout/', views.student_logout, name='student-logout'),
	# path('orders/', views.orders, name='student-orders'),
	# path('history/', views.history, name='student-history'),
	# path('lostfound/', views.lostfound, name='lostfound'),
	# path('portfolio/', views.portfolio, name='portfolio'),
	# path('academics/', views.academics, name='academics'),
	# path('library/', views.library, name='student-library'),
	# path('events/', views.events, name='events'),
	# path('vclass/', views.vclass, name='student-vclass'),
	# path('feedback/', views.feedback, name='student-feedback'),
	#path('/', views., name=''),
]
