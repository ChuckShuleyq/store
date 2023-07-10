from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm
from django.contrib.auth import authenticate, login
from django.urls import reverse
# Create your views here.
def register_page(request):
    return render(request, 'users/register.html')

def login_page(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password= password)
            if user:
                login(request, user)
    else:
        form = UserLoginForm()
    context = {'form': UserLoginForm()}
    return render(request, 'users/login.html', context)