from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact/', views.contact, name='contact'),
]
