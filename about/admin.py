from django.contrib import admin
from .models import Course, Skill

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','degree_title','created', 'updated')

admin.site.register(Course, CategoryAdmin)

class SkillAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title','image','created', 'updated')

admin.site.register(Skill, SkillAdmin)