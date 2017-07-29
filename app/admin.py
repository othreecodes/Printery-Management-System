"""
Contains all registered admin views
"""
from django.contrib import admin
from app.models import (User, Client, Document, PrintJob)
from django.contrib.auth.forms import UserCreationForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm

admin.site.register(Client)
admin.site.register(Document)
admin.site.register(PrintJob)


