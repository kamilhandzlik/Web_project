from django.urls import path
from .views import (
    HomeView,
    ContactView,
    AboutUsView,
    ServiceTermsView,
    CooperationView,
    ParcelLockerView,
    PostPointView,
    WarehouseView,
    EmploymentView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('terms/', ServiceTermsView.as_view(), name='terms'),
    path('cooperation/', CooperationView.as_view(), name='cooperation'),
    path('parcel-locker/', ParcelLockerView.as_view(), name='parcel-locker'),
    path('post-point/', PostPointView.as_view(), name='post-point'),
    path('warehouse/', WarehouseView.as_view(), name='warehouse'),
    path('employment_page/', EmploymentView.as_view(), name='employment_page'),
]
