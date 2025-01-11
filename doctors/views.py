from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from doctors.forms import DoctorForm
from doctors.models import Doctor
from users.services import get_qs_from_cache


class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctors/home.html'

    def get_queryset(self):
        return get_qs_from_cache(qs=Doctor.objects.all(), key='doctor_list')


class DoctorCreateView(LoginRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('doctors:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class DoctorUpdateView(LoginRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    success_url = reverse_lazy('doctors:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class DoctorDeleteView(LoginRequiredMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy('doctors:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class DoctorDetailView(LoginRequiredMixin, DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'
    login_url = "users:login"
    redirect_field_name = "redirect_to"