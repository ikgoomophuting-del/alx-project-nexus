from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("email","username","role","is_staff")
    search_fields = ("email","username")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email","password")}),
        ("Personal", {"fields": ("username",)}),
        ("Permissions", {"fields": ("is_active","is_staff","is_superuser","role")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",),"fields": ("email","username","password1","password2","role")}),
    )

