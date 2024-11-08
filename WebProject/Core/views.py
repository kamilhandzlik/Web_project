from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ContactForm

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def contact(request):
    contact_fields = ContactForm.objects.all()
    return render(request, 'contact.html', {'contact_fields': contact_fields})