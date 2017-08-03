"""
Contains all registered admin views
"""
from django.contrib import admin
from app.models import (User, Document, PrintJob,Pricing,Payment,Grant)
from django.contrib.auth.forms import UserCreationForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm


admin.site.register(Document)
admin.site.register(PrintJob)
admin.site.register(Pricing)
admin.site.register(Payment)
admin.site.register(Grant)



