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
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')


        user_data_has_error = False


        if User.objects.filter(username=username).exists():
            user_data_has_error = True
            messages.error(request, 'Taki użytkownik już istnieje.')


        # if User.objects.filter(email=email).exists():
        #     user_data_has_error = True
        #     messages.error(request, 'Użytkownik z takim mailem już istnieje.')


        if len(password) < 8:
            user_data_has_error = True
            messages.error(request, 'Twoje hasło jest za krótkie. Musi mieć minimum 8 znaków.')

        if password != confirm_password:
            user_data_has_error = True
            messages.error(request, 'Hasła nie pasują do siebie.')


        if user_data_has_error:
            return redirect('register')


        new_user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )


        messages.success(request, 'Konto zostało utworzone poprawnie. Teraz się zaloguj.')
        return redirect('login')


    return render(request, 'register.html')


def LoginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.')
            return redirect('login')

    return render(request, 'login.html')


def LogoutView(request):
    logout(request)

    return redirect('login')


def ForgotPassword(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        # verifying if email exist
        try:
            user = User.objects.get(email=email)

            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})

            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'

            email_body = f"Zresetuj hasło używając poniższego linku:\n\n\n{full_password_reset_url}"

            email_message = EmailMessage(
                'Zresetuj swoje hasło',  # Email subject.
                email_body,
                settings.EMAIL_HOST_USER,  # Email sender.
                [email]  # Email reciever.
            )
            email_message.fail_silently = True
            email_message.send()

            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f"Nie znaleziono takiego '{email}' adresu.")
            return redirect('forgot-password')

    return render(request, 'forgot_password.html')


def PasswordResetSent(request, reset_id):
    if PasswordReset.objects.filter(reset_id=reset_id).exists():
        return render(request, 'password_reset_sent.html')
    else:
        # redirect to forgot password page if code does not exist
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')


def ResetPassword(request, reset_id):
    try:
        password_reset_id = PasswordReset.objects.get(reset_id=reset_id)
        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            password_have_error = False

            if password != confirm_password:
                password_have_error = True
                messages.error(request, 'Hasła nie pasują do siebie.')

            if len(password) < 8:
                password_have_error = True
                messages.error(request, 'Twoje hasło jest zakrótkie. Musi mieć minimum 8 znaków')

            expiration_time = password_reset_id.create_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:

                reset_id.delete()

                password_have_error = True
                messages.error(request, 'Token wygasł.')

            # Reset of password
            if not password_have_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()

                # Delete reset id after use
                password_reset_id.delete()

                # Redirect to login
                messages.success(request, 'Hasło zresetowano pomyślnie. Teraz się zaloguj.')
                return redirect('login')
            else:
                return redirect('reset-password', reset_id=reset_id)


    except PasswordReset.DoesNotExist:
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')

    return render(request, 'reset_password.html')
