from django import forms

from services.models import Service, Record
from users.forms import StyleFormMixin


class ServiceForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class RecordForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Record
        exclude = ('user', 'is_active')