from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.shortcuts import render, redirect
from account.forms import RegisterForm, LoginForm, ForgetPasswordForm
from account.models import CustomUser, Bmi, Bmr, Whr, Bfp
from account.utils import send_code
import math


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

def home(request):
    if request.user.is_authenticated:
        user = request.user
        bmi_list = Bmi.objects.all().order_by('-created_time')
        bmr_list = Bmr.objects.all().order_by('-created_time')
        whr_list = Whr.objects.all().order_by('-created_time')
        bfp_list = Bfp.objects.all().order_by('-created_time')
    else:
        user = None
        bmi_list = None
        bmr_list = None
        whr_list = None
        bfp_list = None
    if request.method == 'POST':
        bmi_result = cal_bmi(request)
        bmr_result = cal_bmr(request)
        whr_result = cal_whr(request)
        bfp_result = cal_bfp(request)
        return render(request, 'index.html',
                      {'bmi': bmi_result, 'bmr': bmr_result, 'whr': whr_result, 'bfp': bfp_result, 'user': user,
                       'bmi_list': bmi_list, 'bmr_list': bmr_list, 'whr_list': whr_list, 'bfp_list': bfp_list})
    return render(request, 'index.html',
                  {'user': user, 'bmi_list': bmi_list, 'bmr_list': bmr_list, 'whr_list': whr_list,
                   'bfp_list': bfp_list})


def cal_whr(request):
    try:
        waist = float(request.POST.get('whr-waist'))
        hip = float(request.POST.get('whr-hip'))
        gender = request.POST.get('whr-gender')
        whr = waist / hip
        if gender == 'female':
            if whr <= 0.8:
                result = "Low risk"
            elif 0.8 < whr <= 0.84:
                result = "Balanced"
            else:
                result = "Dangerous"
        else:
            if whr <= 0.95:
                result = "Low risk"
            elif 0.95 < whr <= 1:
                result = "Balanced"
            else:
                result = "Dangerous"
        whr = round(whr, 2)
        whr_result = f"{whr} ({result})"
        if whr_result:
            gender_type = 1 if gender == 'male' else 2
            try:
                Whr.objects.create(
                    user=request.user,
                    hip=hip,
                    waist=waist,
                    gender=gender_type,
                    result=whr_result
                )
            except:
                messages.error(request, 'Invalid Inputs!', 'error')
        return whr_result
    except:
        return None


def cal_bmi(request):
    try:
        weight = float(request.POST.get('bmi-weight'))
        height = float(request.POST.get('bmi-height')) / 100
        bmi = weight / (height * height)
        if bmi < 18.5:
            result = "Underweight"
        elif 18.5 <= bmi < 24.5:
            result = "Normal"
        elif 24.5 <= bmi < 30:
            result = "Overweight"
        elif 30 <= bmi < 35:
            result = "Grade 1 obesity"
        elif 35 <= bmi < 40:
            result = "Grade 2 obesity"
        else:
            result = "Grade 3 obesity"
        bmi = round(bmi, 2)
        bmi_result = f"{bmi} ({result})"
        if bmi_result:
            try:
                Bmi.objects.create(
                    user=request.user,
                    height=height * 100,
                    weight=weight,
                    result=bmi_result
                )
            except:
                messages.error(request, 'Invalid Inputs!', 'error')
        return bmi_result
    except:
        return None


def cal_bmr(request):
    try:
        gender = request.POST.get('bmr-gender')
        age = float(request.POST.get('bmr-age'))
        height = float(request.POST.get('bmr-height'))
        weight = float(request.POST.get('bmr-weight'))
        if gender == 'female':
            result = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        else:
            result = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
        result = round(result, 2)
        bmr_result = f"{result} (Cal/day)"
        if bmr_result:
            gender_type = 1 if gender == 'male' else 2
            try:
                Bmr.objects.create(
                    user=request.user,
                    age=age,
                    height=height,
                    weight=weight,
                    gender=gender_type,
                    result=bmr_result
                )
            except:
                messages.error(request, 'Invalid Inputs!', 'error')
        return bmr_result
    except:
        return None


def cal_bfp(request):
    try:
        gender = request.POST.get('bfp-gender')
        # age = float(request.POST.get('bfp-age'))
        height = float(request.POST.get('bfp-height'))
        # weight = float(request.POST.get('bfp-weight'))
        waist = float(request.POST.get('bfp-waist'))
        neck = float(request.POST.get('bfp-neck'))
        hip = float(request.POST.get('bfp-hip'))
        if gender == 'female':
            bfp = 495 / (1.29579 - 0.35004 * math.log10(waist + hip - neck) + 0.221 * math.log10(height)) - 450
            if bfp < 14:
                result = 'Essential'
            elif bfp < 21:
                result = 'Athletes'
            elif bfp < 25:
                result = 'Fitness'
            elif bfp < 32:
                result = 'Average'
            else:
                result = 'Obese'
        else:
            bfp = 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
            if bfp < 6:
                result = 'Essential'
            elif bfp < 14:
                result = 'Athletes'
            elif bfp < 18:
                result = 'Fitness'
            elif bfp < 25:
                result = 'Average'
            else:
                result = 'Obese'
        bfp = round(bfp, 1)
        bfp_result = f"{bfp} % ({result})"
        if bfp_result:
            gender_type = 1 if gender == 'male' else 2
            try:
                Bfp.objects.create(
                    user=request.user,
                    height=height,
                    neck=neck,
                    waist=waist,
                    hip=hip,
                    gender=gender_type,
                    result=bfp_result
                )
            except:
                messages.error(request, 'Invalid Inputs!', 'error')
        return bfp_result
    except:
        return None
