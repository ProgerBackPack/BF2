from django.contrib import admin

from services.models import Service, Record, Diagnostic


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('id',)
    search_fields = ('name', 'description',)


@admin.register(Record)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'doctor', 'created_at')
    list_filter = ('id', 'created_at')
    search_fields = ('user', 'created_at',)


@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'record', 'result', 'diagnose')
    list_filter = ('id', 'user')
    search_fields = ('user', 'id',)