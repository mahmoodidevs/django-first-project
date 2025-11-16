from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.views import View

def home(request):
    return render(request , "accounts.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            user = User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password']
            )
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            user.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request=request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "نام کاربری یا رمز عبور اشتباه است")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request , "You have successfully logged out." , "success")
    return redirect('home')
