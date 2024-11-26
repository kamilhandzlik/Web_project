from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import (
    ContactForm,
    MainPage,
    AboutUsPage,
    ServiceTerms,
    CooperationPage,
    ParcelLockerPage,
    PostPointPage,
    WarehousePage,
    EmploymentPage,
)


class HomeView(ListView):
    model = MainPage
    template_name = 'home.html'
    context_object_name = 'mainpages'


class AboutUsView(ListView):
    model = AboutUsPage
    template_name = 'about_us.html'
    context_object_name = 'aus_pages'


class ContactView(ListView):
    model = ContactForm
    template_name = 'contact.html'
    context_object_name = 'contact_fields'


class ServiceTermsView(TemplateView):
    template_name = 'terms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['term'] = ServiceTerms.load()
        return context


class CooperationView(ListView):
    model = CooperationPage
    template_name = 'cooperation.html'
    context_object_name = 'coop_fields'


class ParcelLockerView(ListView):
    model = ParcelLockerPage
    template_name = 'parcel_locker.html'
    context_object_name = 'parcels'


class PostPointView(ListView):
    model = PostPointPage
    template_name = 'post_point.html'
    context_object_name = 'postpoints'


class WarehouseView(ListView):
    model = WarehousePage
    template_name = 'warehouse.html'
    context_object_name = 'warehouses'


class EmploymentView(ListView):
    model = EmploymentPage
    template_name = 'employment-page.html'
    context_object_name = 'employment_fields'
