from django.contrib import admin
from gioseffo.apps.positions.models import Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
