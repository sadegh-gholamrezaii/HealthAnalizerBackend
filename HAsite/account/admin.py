from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

from account.models import CustomUser, Bmi, Bmr, Whr, Bfp


@register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'type']
    fieldsets = (
        (None, {'fields': ('username', 'password', 'type')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'type', 'password1', 'password2'),
        }),
    )


@register(Bmi)
class BmiAdmin(admin.ModelAdmin):
    list_display = ['user', 'weight', 'height', 'created_time']


@register(Bmr)
class BmrAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'weight', 'height', 'gender', 'created_time']


@register(Whr)
class BmrAdmin(admin.ModelAdmin):
    list_display = ['user', 'waist', 'hip', 'gender', 'created_time']


@register(Bfp)
class BmrAdmin(admin.ModelAdmin):
    list_display = ['user', 'neck', 'waist', 'height', 'hip', 'gender', 'created_time']
