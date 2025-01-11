from django.urls import path
from django.views.decorators.cache import cache_page

from doctors.apps import DoctorsConfig
from doctors.views import (DoctorDetailView, DoctorListView, DoctorCreateView, DoctorUpdateView,
                           DoctorDeleteView)

app_name = DoctorsConfig.name

urlpatterns = [
    path('create/', DoctorCreateView.as_view(), name='create'),
    path('', DoctorListView.as_view(), name='home'),
    path('edit/<int:pk>/', DoctorUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', DoctorDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'), ]
