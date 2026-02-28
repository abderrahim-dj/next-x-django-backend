from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  search_fields = ['username', 'phone_number', 'email']
  list_display = ['id', 'username', 'email', 'phone_number', 'is_staff', 'is_active']

  fieldsets = UserAdmin.fieldsets + (
    ('Additional Info', {'fields': ('phone_number',)}),
  )

  add_fieldsets = UserAdmin.add_fieldsets + (
    ('Additional Info', {'fields': ('phone_number',)}),
)

  add_fieldsets = UserAdmin.add_fieldsets + (
    ('Additional Info', {'fields': ('phone_number',)}),
  )

