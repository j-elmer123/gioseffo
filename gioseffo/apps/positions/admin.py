from django.contrib import admin
from gioseffo.apps.positions.models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    raw_id_fields = ['created_by', 'updated_by', 'deleted_by']
