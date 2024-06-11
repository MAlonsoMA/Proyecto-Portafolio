from django.contrib import admin
from .models import Course, Skill

class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('id','title','created', 'updated')

admin.site.register([Course, Skill], AboutAdmin)
