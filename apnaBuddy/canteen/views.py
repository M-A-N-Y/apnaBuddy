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

def canteen_login(request):
    if request.method == 'POST':
        username=request.POST
        loginusername=request.POST.get('user')
        loginpassword=request.POST.get('password')
        print(loginpassword,loginusername)
        user=authenticate(username=loginusername,password=loginpassword)
        print(user)
        if user is not None:
            try:
                if Manager.objects.get(user = user).is_manager == True:
                    login(request,user)
                    messages.success(request,"Successfully Logged in")
                    return redirect('/canteen')
                    #return render(request,'student/index.html')
            except:
                messages.error(request,"Wrong credentials,Please try again !")
                #return redirect('/canteen/')
                return render(request,'canteen/login2.html')
        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'canteen/login2.html')
    else:
        messages.success(request,"You need to login to access this")
        return render(request,'canteen/login2.html')


def canteen_logout(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("/")

def orders(request):
	pass

def history():
	pass
