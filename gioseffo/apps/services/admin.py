from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    raw_id_fields = ['created_by', 'updated_by', 'deleted_by']
