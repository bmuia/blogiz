# users/admin.py
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active')  # Add fields to display in the list view
    search_fields = ('email', 'first_name', 'last_name')  # Add search functionality by email and name

admin.site.register(CustomUser, CustomUserAdmin)
