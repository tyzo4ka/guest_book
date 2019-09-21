from django.contrib import admin
from webapp.models import Entry


class EntryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'email', 'text', 'status', 'created_at', 'updated_at']
    list_filter = ['author', 'email', 'status']
    list_display_links = ['pk', 'author']
    search_fields = ['text']
    fields = ['author', 'email', 'text', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Entry, EntryAdmin)
