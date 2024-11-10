from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ContactForm, MainPage, AboutUsPage

# Create your views here.
def Home(request):
    mainpages = MainPage.objects.all()
    return render(request, 'home.html',  {'mainpages': mainpages})

def about_us(request):
    mainpages = AboutUsPage.objects.all()
    return render(request, 'about_us.html',  {'mainpages': mainpages})

def contact(request):
    contact_fields = ContactForm.objects.all()
    return render(request, 'contact.html', {'contact_fields': contact_fields})