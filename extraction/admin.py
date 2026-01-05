from django.contrib import admin
from .models import ExtractionJob, ExtractionResult


@admin.register(ExtractionJob)
class ExtractionJobAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'record_count', 'created_at', 'finished_at')
    list_filter = ('status',)
    search_fields = ('id',)


@admin.register(ExtractionResult)
class ExtractionResultAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'external_id', 'job')
    search_fields = ('email', 'external_id')
