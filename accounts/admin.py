from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'university_id', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'university_id')
    ordering = ('id',)

admin.site.register(User, UserAdmin)
