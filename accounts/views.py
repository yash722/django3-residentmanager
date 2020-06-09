from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

def home(request):
    return render(request, 'accounts/home.html', {})

def signupform(request):
    if request.method == "GET":
        return render(request, 'accounts/signupform.html', {'form':RegisterForm()})
    else:
        if request.POST['password1'] != request.POST['password2']:
            return render(request, 'accounts/signupform.html', {'form':RegisterForm(), 'error':'Passwords do not match'})
        else:
            try:
                user = User.objects.create_user(request.POST['society_name'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'accounts/signupform.html',{'form':RegisterForm(), 'error':'Society Name is not unique'})

def loginform(request):
    if request.method == "GET":
        return render(request, 'accounts/loginform.html', {'form':LoginForm()})
    else:
        user = authenticate(request, society_name=request.POST['society_name'], password=request.POST['password'])
        if user is None:
            return render(request, 'accounts/loginform.html', {'form':LoginForm(), 'error':'Society Name and password entered do not match.'})
        else:
            login(request, user)
            return redirect('home')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
