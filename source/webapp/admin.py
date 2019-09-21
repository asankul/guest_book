from django.contrib import admin
from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'text', 'date_of_creation', 'date_of_edition', 'status']
    list_filter = ['name', 'email', 'date_of_creation', 'date_of_edition', 'status']
    search_fields = ['name', 'email']
    fields = ['name', 'email', 'text', 'status']


admin.site.register(GuestBook, GuestBookAdmin)

