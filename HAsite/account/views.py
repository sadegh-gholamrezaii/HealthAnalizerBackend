from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from account.forms import RegisterForm, LoginForm
from account.models import CustomUser


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                user = CustomUser.objects.create_user(username=cd['Email'], password=cd['Password'])
                messages.success(request, 'Successfully Registration', 'success')
                login(request, user)
                return redirect('home')
            except:
                messages.error(request, 'Invalid Information', 'error')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['Email'], password=cd['Password'])
            if user:
                login(request, user)
                messages.success(request, 'Login Successfully', 'success')
                return redirect('home')
            else:
                messages.error(request, 'Invalid Password or Email address!', 'error')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out', 'success')
    return redirect('home')

# def cal_whr(request):
#     # whr = kamar/basan
#     # woman-> kamkhatar <= 0.8
#     #         motevaset 0.81 <= x <= 0.84
#     #         porkhatar x >= 0.85
#     # man-> kamkhatar <= 0.95
#     #         motevaset 0.96 <= x <= 1
#     #         porkhatar x >= 1.1
#     pass
#
#
# def cal_bmi(request):
#     # bmi = weight / height * height
#     # bmi < 18.5 -> kambood vazn
#     # 18.5 <= bmi < 24.5 -> vazn salamat
#     # 24.5 <= bmi < 30 -> ezafe vazn
#     # 30 <= bmi < 35 -> chaghi darage aval
#     # 35 <= bmi < 40 -> chaghi darage dovom
#     # 40 <= bmi -> chaghi darage sevom
#     pass
#
#
# def cal_bmr(request):
#     # woman-> (age*4.33)-(height.cm*3.098)+(weight*9.924)+447.593
#     # man-> (age*5.677)-(height.cm*4.799)+(weight*13.397)+88.362
#     pass
