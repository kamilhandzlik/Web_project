from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views import View
from .models import *
import random

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
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
        new_user.is_active = False
        new_user.save()

        activation_code = random.randint(100000, 999999)
        request.session['activation_code'] = activation_code
        request.session['user_id'] = new_user.id

        email_body = f"Witaj {first_name}! Twój kod aktywacyjny to: {activation_code}"
        email_message = EmailMessage(
            'Kod aktywacyjny konta',
            email_body,
            settings.EMAIL_HOST_USER,
            [email]
        )
        email_message.send(fail_silently=True)

        messages.success(request, 'Konto zostało utworzone. Sprawdź swoją skrzynkę e-mail, aby aktywować konto.')
        return redirect('activate-account')


class ConfirmRegistration(View):
    def get(self, request, confirmation_id):
        confirmation = get_object_or_404(RegistrationConfirmation, confirmation_id=confirmation_id)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()

        messages.success(request, 'Twoje konto zostało potwierdzone. Możesz się teraz zalogować.')
        return redirect('login')


class ActivateAccount(View):
    def get(self, request):
        return render(request, 'activate_account.html')

    def post(self, request):
        input_code = request.POST.get('activation_code')
        user_id = request.session.get('user_id')
        activation_code = request.session.get('activation_code')

        if input_code == str(activation_code):
            user = User.objects.get(id=user_id)
            user.is_active = True
            user.save()

            del request.session['activation_code']
            del request.session['user_id']

            messages.success(request, "Twoje konto zostało pomyślnie aktywowane!")
            return redirect('login')
        else:
            messages.error(request, "Kod aktywacyjny jest nieprawidłowy.")
            return redirect('activate-account')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Witaj {request.user.username}!")
            return redirect('home')
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.')
            return redirect('login')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class ForgotPassword(View):
    def get(self, request):
        return render(request, 'forgot_password.html')

    def post(self, request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password_reset = PasswordReset(user=user)
            new_password_reset.save()

            password_reset_url = reverse('reset-password', kwargs={'reset_id': new_password_reset.reset_id})
            full_password_reset_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'
            email_body = f"Zresetuj hasło używając poniższego linku:\n\n\n{full_password_reset_url}"

            email_message = EmailMessage(
                'Zresetuj swoje hasło',
                email_body,
                settings.EMAIL_HOST_USER,
                [email]
            )
            email_message.fail_silently = True
            email_message.send()

            return redirect('password-reset-sent', reset_id=new_password_reset.reset_id)
        except User.DoesNotExist:
            messages.error(request, f"Nie znaleziono takiego '{email}' adresu.")
            return redirect('forgot-password')


class PasswordResetSent(View):
    def get(self, request, reset_id):
        if PasswordReset.objects.filter(reset_id=reset_id).exists():
            return render(request, 'password_reset_sent.html')
        else:
            messages.error(request, 'Invalid reset id')
            return redirect('forgot-password')


class ResetPassword(View):
    def get(self, request, reset_id):
        return render(request, 'reset_password.html')

    def post(self, request, reset_id):
        try:
            password_reset_id = PasswordReset.objects.get(reset_id=reset_id)
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            password_have_error = False

            if password != confirm_password:
                password_have_error = True
                messages.error(request, 'Hasła nie pasują do siebie.')

            if len(password) < 8:
                password_have_error = True
                messages.error(request, 'Twoje hasło jest za krótkie. Musi mieć minimum 8 znaków.')

            expiration_time = password_reset_id.create_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:
                password_reset_id.delete()
                password_have_error = True
                messages.error(request, 'Token wygasł.')

            if not password_have_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()
                password_reset_id.delete()

                messages.success(request, 'Hasło zresetowano pomyślnie. Teraz się zaloguj.')
                return redirect('login')
            else:
                return redirect('reset-password', reset_id=reset_id)
        except PasswordReset.DoesNotExist:
            messages.error(request, 'Invalid reset id')
            return redirect('forgot-password')
