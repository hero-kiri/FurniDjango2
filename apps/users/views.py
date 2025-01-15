from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

import random

from .models import CustomUser
from .utils import send_code_email


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Пароли не совпадают')
            return redirect('register')
        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким именем уже существует!')
            return redirect('register')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с такий почтой уже существует!')
            return redirect('register')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            messages.error(request, 'Пользователь с таким номером уже существует!')
            return redirect('register')

        user = CustomUser.objects.create(
            username=username, 
            email=email,
            phone_number=phone_number,
            password=password1)
        user.auth_code = str(random.randint(100000,999999))
        user.save()
        # Отправка кода на почту
        send_code_email(user)
        messages.success(request, 'Регистрация прошла успешно! Проверьте вашу почту для активации аккаунта.')
        return redirect('verify_email', id=user.id)
    
    return render(request, 'users/register.html')

def verify_email(request, id):
    user = CustomUser.objects.get(id=id)
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == user.auth_code:
            user.is_active = True
            user.save()
            # Авторизуем пользователя 
            login(request, user)
            messages.success(request, 'Аккаунт успешно активирован!')
            return redirect('/')
        else:
            return render(request, 'users/verify_email.html', {'error': 'Неверный код'})
    return render(request, 'users/verify_email.html')
    

def login_view(request):
    # ...
    return render(request, 'users/login.html')
