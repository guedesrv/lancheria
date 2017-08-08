# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ['titulo', 'created_at']
    search_fields = ['titulo']
    
    prepopulated_fields = {'slug': ('titulo',)}

admin.site.register(Post, PostAdmin)