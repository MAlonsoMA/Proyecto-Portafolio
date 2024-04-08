from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('key', 'name', 'url')
    search_fields = ('name',)

admin.site.register(Link, LinkAdmin)


