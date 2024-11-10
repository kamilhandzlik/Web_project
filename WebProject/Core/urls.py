from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about-us/', views.about_us, name='about-us')
]
