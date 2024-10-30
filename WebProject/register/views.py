from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import *

# Create your views here.

def RegisterView(request):

    if request.method =="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # password2 = request.POST.get('password2')

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Taka nazwa użytkownika jest zajęta.')

        # if User.object.filter(email=email).exists():
        #     user_data_has_error = True
        #     messages.error(request, 'Ten email jest zajęty.')

        if len(password) < 8:
            user_data_has_error = True
            messages.error(request, 'Twoje hasło jest zakrótkie.Minimum 8 znaków')

        # if password2 != password1:
        #     user_data_has_error = True
        #     messages.error(request, 'Hasła nie pasują do siebie.')

        if user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password1=password,
                # password2=password2
            )
            messages.success(request, 'Konto zostało utworzone poprawnie. Teraz się zaloguj.')
            return render(request, 'login.html')


    return  render(request, 'register.html')

def LoginView(request):
    return  render(request, 'login.html')