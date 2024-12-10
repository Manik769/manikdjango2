from http.client import HTTPResponse
from django.contrib.auth import authenticate,login as auth_login,logout
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse


@login_required
# Create your views here.
def homepage(request):
    return render(request, 'result.html',{})
def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username,email,password)
        new_user.first_name = fname
        new_user.last_name = lname

        new_user.save()
        return redirect('login-page')

    return render(request, 'register.html',{})

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home-page')
            #return render(request, 'result.html', {})
        else:
            return HTTPResponse('Error,user does not exist')

    return render(request, 'login.html',{})
def index(request):
    return render(request, 'index.html',{})