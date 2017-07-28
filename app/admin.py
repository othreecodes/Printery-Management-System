"""
Contains all registered admin views
"""
from django.contrib import admin
from app.models import (User, Client, Document, PrintJob)


admin.site.register(User)
admin.site.register(Client)
admin.site.register(Document)
admin.site.register(PrintJob)
