from django.contrib import admin
from pilotlog.models import PilotLog
# Register your models here.


@admin.register(PilotLog)
class PilotLogAdmin(admin.ModelAdmin):
    list_display = ['pilot', 'file', 'created_at']
    search_fields = ['pilot', 'file']
