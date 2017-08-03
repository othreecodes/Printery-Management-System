"""
Contains all registered admin views
"""
from django.contrib import admin
from app.models import (User, Document, PrintJob, Pricing, Payment, Grant)
from django.contrib.auth.forms import UserCreationForm


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    form = UserCreationForm
    list_display = ['first_name', 'last_name', 'username', 'date_joined']
    


@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ['amount', 'granted']
    list_editable = ['granted']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'file']
    search_fields = ['title']
    actions = ['create_job']

    def create_job(self,queryset):
        pass


@admin.register(PrintJob)
class PrintJobAdmin(admin.ModelAdmin):
    list_display = ['charged_to', 'copies', 'cost', 'status']
    list_editable = ['status']
    list_filter = ['status']    

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payer','job','paid','created']
    search_fields = ['job']
    list_editable = ['paid']
    list_filter = ['paid','created','modified']


admin.site.register(Pricing)
