from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

from accounts.forms import UserChangeForm
from accounts.models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('full_name', 'phone_number', 'email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'phone_number', 'password')}),
        ('Personal info', {'fields': ('is_active',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('full_name', 'phone_number', 'email', 'password', 'confirmed_password')
        })
    )
    search_fields = ('email', 'full_name', 'phone_number')
    ordering = ('full_name', 'email')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
