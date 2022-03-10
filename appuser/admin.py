
from django.contrib import admin
from appuser.models import AppUser

class AppUserAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(AppUser, AppUserAdmin)
