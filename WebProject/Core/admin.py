from django.contrib import admin
from .models import ContactForm, MainPage, AboutUsPage, ServiceTerms

# Register your models here.
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    pass

@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutUsPage)
class AboutUsAdmin(admin.ModelAdmin):
    pass

@admin.register(ServiceTerms)
class ServiceTermsAdmin(admin.ModelAdmin):
    pass