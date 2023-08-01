from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest
from users.models import User
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def register_page(request: HttpRequest):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрированы")
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form, 'title': 'Store - Регистрация'}
    return render(request, 'users/register.html', context=context)

def login_page(request: HttpRequest):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "Вы успешно вошли")
                return HttpResponseRedirect(reverse('home'))
        
    else:
        form = UserLoginForm()
    context = {'form': form, 'title': 'Store - вход'}
    return render(request, 'users/login.html', context)

def profile(request: HttpRequest):
    if request.user.is_authenticated:

        if request.method == 'POST':
            form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('users:profile'))
        else:
            form = UserProfileForm(instance=request.user)

        context = {
            'title': 'Store - профиль',
            'form': form,
        }
        
        return render(request, 'users/profile.html', context)
    else:
        raise PermissionError("You don't have access to view this page!")
    
def logout(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('home'))