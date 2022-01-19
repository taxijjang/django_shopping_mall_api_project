from django.contrib import admin

from .models import ElasticSearch


@admin.register(ElasticSearch)
class ElasticSearchAdmin(admin.ModelAdmin):
    fields = ('id', 'settings', 'mappings')
    list_display = ('id',)
    readonly_fields = ('id',)
