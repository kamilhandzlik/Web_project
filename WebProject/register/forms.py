from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth.models import User
import random


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def generate_activation_code(self, user):
        activation_code = random.randint(100000, 999999)
        return activation_code


class ActivationForm(forms.Form):
    activation_code = forms.CharField(max_length=6, required=True, label='Kod aktywacyjny')


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(required=True, label='Adres e-mail')


class PasswordResetForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput, label='Nowe hasło', required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Potwierdzenie hasła', required=True)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Hasła nie pasują do siebie.")
        return cleaned_data
