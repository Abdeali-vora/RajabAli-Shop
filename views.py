from django.shortcuts import render, redirect
from .models import MyAccountManager
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate
from .models import Account
from .forms import AccountForm, AccountLoginForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return render(request, 'Home.html')


def register(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"you are Already authenticated as {user.email}")
    context = {}
    if request.POST:
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                auth_login(request, user)
                print("You Can LogIn")
                return redirect("Home")
            print("Data Saved")
            return redirect("Home")
        else:
            context['registration_form'] = form
    return render(request, 'Register.html', context)


def login(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"you are Already authenticated as {user.email}")
    context = {}
    if request.POST:
        form = AccountLoginForm(request.POST)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(email=email, password=password)
            if user:
                auth_login(request, user)
                if user.is_superuser:
                    return redirect('admin/')
                return redirect("Home")
        else:
            context['login_form'] = form
    return render(request, 'Login.html', context)


def logout(request):
    auth_logout(request)
    return redirect("Home")
