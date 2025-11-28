from django.contrib import admin
from .models import User
from .models import Profile

admin.site.register(User)
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user","phone")




