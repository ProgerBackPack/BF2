from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
    list_filter = ('id',)
    search_fields = ('first_name', 'last_name', 'email')