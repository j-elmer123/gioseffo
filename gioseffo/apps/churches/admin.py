from django.contrib import admin

from .models import Church, ChurchMembership


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    raw_id_fields = ['created_by', 'updated_by', 'deleted_by']


@admin.register(ChurchMembership)
class ChurchMembershipAdmin(admin.ModelAdmin):
    raw_id_fields = ['created_by', 'updated_by', 'deleted_by']
    list_display = ['church', 'member', 'position']
