from django.shortcuts import render
# from users.models import User
# Create your views here.

def login(request):
    return render(request,'users/login.html')

def register(request):
    return render(request,'users/register.html')