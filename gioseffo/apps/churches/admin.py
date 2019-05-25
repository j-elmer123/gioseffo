from django.contrib import admin
from gioseffo.apps.churches.models import Church, ChurchMembership


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    pass

@admin.register(ChurchMembership)
class ChurchMembership(admin.ModelAdmin):
    pass
