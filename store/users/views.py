from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.urls import reverse
from users.forms import LoginForm, RegisterForm, ProfileForm
from products.models import Basket
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
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = RegisterForm()
    context = {
        'title': 'Store - Регистрация',
        'form': form
    }
    return render(request,'users/register.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = ProfileForm(instance=request.user)\
    
    baskets = Basket.objects.filter(user=request.user)
    context = {
        'title': 'Store - Профиль',
        'form': form,
        'baskets': baskets,
    }
    return render(request,'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))