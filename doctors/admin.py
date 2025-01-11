from django.contrib import admin
from doctors.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic', 'work_experience')
    list_filter = ('id',)
    search_fields = ('name', 'patronymic',)