from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')  # 重新導向到登入畫面
    context = {'form': form}
    return render(request, 'register.html', context)


def logout(request):
    auth.logout(request)
    return render(request, 'logout.html')


def login(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)


def account_index(request):
    return render(request, 'account_index')
