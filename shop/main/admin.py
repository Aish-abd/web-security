from django.contrib import admin

# Register your models here.
from .models import Login,User_Custom

admin.site.register(Login)
admin.site.register(User_Custom)
# main/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from main.models import User_Custom

# class CustomUserAdmin(UserAdmin):
#     model = User_Custom

# # Register the custom admin for your UserCustom model
# admin.site.register(User_Custom, CustomUserAdmin)
