from django import forms

from doctors.models import Doctor
from users.forms import StyleFormMixin


class DoctorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'