from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from account.forms import RegisterForm, LoginForm, ForgetPasswordForm
from account.models import CustomUser
from account.utils import send_code


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = CustomUser.objects.filter(username=cd['Email']).first()
            if user:
                messages.error(request, 'Someone has registered with this email', 'error')
                return redirect('register')
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


def forget_password(request):
    if request.method == "POST":
        form = ForgetPasswordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['Email']
            new_password = CustomUser.objects.make_random_password(length=8)
            try:
                user = CustomUser.objects.get(username=email)
                user.set_password(new_password)
                user.save()
                send_code(email, new_password)
                messages.success(request, 'The password has been sent to your email', 'success')
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid Email Address!', 'error')
                return redirect('forget_password')
            return redirect('login')
    else:
        form = ForgetPasswordForm
    return render(request, 'account/forget_password.html', {'form': form})


# def change_password(request, pk):
#     if request.method == "POST":
#         form = ChangePasswordForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             email = cd['Email']
#             password = cd['Password']
#             try:
#                 CustomUser.objects.get(username=email).objects.update(password=password)
#             except CustomUser.DoesNotExist:
#                 raise Http404
#     else:
#         try:
#             user = CustomUser.objects.get(id=pk)
#         except CustomUser.DoesNotExist:
#             raise Http404
#         form = ChangePasswordForm({'Email': user.username})
#     return render(request, 'account/change_password.html', {'form': form})


def cal_whr(request):
    if request.method == 'POST':
        kamar = request.POST.get('kamar')
        basan = request.POST.get('basan')
        gender = request.POST.get('gender')
        whr = kamar / basan
        if gender is 'woman':
            if whr <= 0.8:
                result = "kamkhatar"
            elif 0.8 < whr <= 0.84:
                result = "motevaset"
            else:
                result = "porkhatar"
        else:
            if whr <= 0.95:
                result = "kamkhatar"
            elif 0.95 < whr <= 1:
                result = "motevaset"
            else:
                result = "porkhatar"
    pass


def cal_bmi(request):
    if request.method == 'POST':
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        bmi = weight / height * height
        if bmi < 18.5:
            result = "kambood vazn"
        elif 18.5 <= bmi < 24.5:
            result = "vazn salamat"
        elif 24.5 <= bmi < 30:
            result = "ezafe vazn"
        elif 30 <= bmi < 35:
            result = "chaghi darage aval"
        elif 35 <= bmi < 40:
            result = "chaghi darage dovom"
        else:
            result = "chaghi darage sevom"
    pass


def cal_bmr(request):
    if request.method == "POST":
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        if gender is 'woman':
            result = (age*4.33)-(height.cm*3.098)+(weight*9.924)+447.593
        else:
            result = (age*5.677)-(height.cm*4.799)+(weight*13.397)+88.362
    pass
