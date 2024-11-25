from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact/', views.Contact, name='contact'),
    path('about-us/', views.AboutUs, name='about-us'),
    path('terms/', views.ServiceTermsView, name='terms'),
]
