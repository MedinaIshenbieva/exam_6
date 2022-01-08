from django.contrib import admin

from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'text']
    list_filter = ['created_at']
    search_fields = ['author', 'text']
    fields = ['author', 'email', 'text', 'status']
    readonly_fields = ['updated_at']


admin.site.register(GuestBook, GuestBookAdmin)

