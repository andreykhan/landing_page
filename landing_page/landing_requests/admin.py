from django.contrib import admin

from .models import Requests


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'msisdn', 'email', 'date_created', 'date_updated', 'comments', 'agreement']
