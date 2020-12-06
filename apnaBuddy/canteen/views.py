from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
#from .forms import OrderForm

# Create your views here.
def index(request):
	return render(request, 'canteen/index.html')

def login(request):
	pass
	'''
	if request.method=="POST":
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            if Belongs.objects.get(user = user).is_ngo:
                login(request,user)
                messages.success(request,"Successfully Logged in")
                return render(request,'canteen/loginpage.html')
            else:
                messages.error(request,"Wrong credentials,Please try again !")
                return render(request,'canteen/login.html')
        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'canteen/login.html')
    else:
        messages.success(request,"You need to login to access this")
        return render(request,'canteen/login.html')
	'''

def logout_u(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("canteen/orders")

def orders(request):
	pass

def history():
	pass
