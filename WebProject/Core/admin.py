from django.contrib import admin
from .models import ContactForm, MainPage

# Register your models here.
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    pass

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    pass
