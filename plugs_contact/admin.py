from django.contrib import admin

from plugs_contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
    """
    Contact Model Admin
    """
    fields = ('email', 'subject', 'message')
    readonly_fields = ('id', 'created', 'updated')
    list_display = ('email', 'subject', 'created')
    search_fields = ('email', 'subject')

admin.site.register(Contact, ContactAdmin)
