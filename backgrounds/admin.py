from django.contrib import admin
from .models import BackgroundImage

# Register your models here.

class BackgroundImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('name', 'image', 'title','subtitle', 'sentence', 'created', 'updated')
    fields = ('name', 'image', 'title', 'subtitle', 'sentence', 'created', 'updated')
    def get_readonly_fields(self,request,obj=None):
        if obj:
            return self.readonly_fields + ('name',)
        return self.readonly_fields
                    
admin.site.register(BackgroundImage, BackgroundImageAdmin)
