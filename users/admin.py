from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'username', 'password']
    search_fields = ['id', 'name', 'username']
