from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.models import User
from users.forms import LoginForm, RegisterForm, UserProfile

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
    context = {
        'title': 'Store - Авторизация',
        'form': form
    }
    return render(request,'users/login.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = RegisterForm()
    context = {
        'title': 'Store - Регистрация',
        'form': form
    }
    return render(request,'users/register.html', context)


def profile(request):
    form = UserProfile()
    context = {
        'title': 'Store - Профиль',
        'form': form
    }
    return render(request,'users/profile.html', context)