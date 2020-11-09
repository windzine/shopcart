from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')  # 重新導向到登入畫面
    else:
        context = {'form': form }
        return render(request, 'register.html', context)


def log_out(request):
    auth.logout(request)
    return render(request, 'logout.html')


def log_in(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/accounts/')  #重新導向到首頁
    context = {'form': form}
    return render(request, 'login.html', context)


def account_index(request):
    if request.user.is_authenticated:
        return render(request, 'account_index.html')
    else:
        return redirect('/accounts/login/')
    return render(request, 'account_index.html')
