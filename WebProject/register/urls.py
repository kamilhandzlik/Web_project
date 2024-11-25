from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('forgot-password/', views.ForgotPassword.as_view(), name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.PasswordResetSent.as_view(), name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.ResetPassword.as_view(), name='reset-password'),
    path('activate/', views.ActivateAccount.as_view(), name='activate-account'),
]
