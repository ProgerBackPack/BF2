from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from services.forms import ServiceForm, RecordForm
from services.models import Service, Record, Diagnostic

class ServiceListView(ListView):
    model = Service
    template_name = 'services/home.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'У вас новое сообщение: {name}({phone}): {message}')
    return render(request, 'services/contacts.html')


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'У вас новое сообщение: {name}({phone}): {message}')
    return render(request, 'services/home_page.html')


def company(request):
    return render(request, 'services/company.html')


def mission(request):
    return render(request, 'services/mission.html')


class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Service
    form_class = ServiceForm
    success_url = reverse_lazy('services:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Service
    success_url = reverse_lazy('services:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class ServiceDetailView(LoginRequiredMixin, DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class RecordCreateView(LoginRequiredMixin, CreateView):
    """Record create """
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('services:home')
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecordListView(ListView):
    model = Record
    template_name = 'services/record_list.html'


class RecordUpdateView(LoginRequiredMixin, UpdateView):
    model = Record
    form_class = RecordForm
    success_url = reverse_lazy('services:record_list')
    login_url = "users:login"
    redirect_field_name = "redirect_to"

    def get_form_class(self):
        user = self.request.user
        if user == self.object.user:
            return RecordForm


class RecordDeleteView(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = reverse_lazy('services:record_list')
    login_url = "users:login"
    redirect_field_name = "redirect_to"


class DiagnosticListView(LoginRequiredMixin, ListView):
    model = Diagnostic
    template_name = 'services/diagnostic_list.html'
    permission_required = 'services.view_diagnostics'
