from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import *
from student.models import Student

# Create your views here.
def index(request):
	return render(request, 'committee/index.html')

def committee_login(request):
    if request.method == 'POST':
        username=request.POST
        loginusername=request.POST.get('user')
        loginpassword=request.POST.get('password')
        print(loginpassword,loginusername)
        user=authenticate(username=loginusername,password=loginpassword)
        print(user)
        if user is not None:
            try:
                if Committee.objects.get(user = user).is_committee == True:
                    login(request,user)
                    messages.success(request,"Successfully Logged in")
                    return redirect('/committee')
                    #return render(request,'student/index.html')
            except:
                messages.error(request,"Wrong credentials,Please try again !")
                #return redirect('/canteen/')
                return render(request,'committee/login2.html')
        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'committee/login2.html')
    else:
        messages.success(request,"You need to login to access this")
        return render(request,'committee/login2.html')

def committee_logout(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("/")

def events(request):
    eve = Events.objects.all()
    params = {'eve':eve}
    return render(request,'committee/events.html',params)

def payment(request,pk):
    output=''
    user = request.user
    student = Student.objects.get(user=request.user)
    event = Events.objects.get(id=pk)
    if (student.spitcoin - event.cost>0) :
        event.name.balance += event.cost
        student.spitcoin -= event.cost
        event.paid.add(student)
        student.save()
        event.name.save()
        event.save()
        output = 'TRANSACTION SUCESSFUL'
        print("\n\n\n\n OK success!")

    else:
        output = 'TRANSACTION FAILED'
        print('\n\n\n\npayment failed')
    params = {'output':output,'balance':student.spitcoin}
    return render(request,'committee/payment.html',params)