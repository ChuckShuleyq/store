from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.
def register_page(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form, 'title': 'Store - Регистрация'}
    return render(request, 'users/register.html', context=context)

def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': UserLoginForm(), 'title': 'Store - вход'}
    return render(request, 'users/login.html', context)

def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm()

    context = {
        'title': 'Store - профиль',
        'form': form,
    }
    return render(request, 'users/profile.html', context)