from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from .models import BackgroundImage

# Register your models here.
class BackgroundImageAdminForm(forms.ModelForm):    
    class Meta:
        model=BackgroundImage
        fields = '__all__'

    def clean_image(self):
        instance=self.instance
        if instance.pk:
            existing_instance=BackgroundImage.objects.get(pk=instance.pk)
            if existing_instance.image != self.cleaned_data['image']:
                raise ValidationError("No se puede modificar una imagen existente. Por favor, elimine la imagen primero y luego suba una nueva.")
        
        if BackgroundImage.objects.filter(image=self.cleaned_data['image'].name).exists() and not instance.pk:
                 raise ValidationError("Una imagen con este nombre ya existe. Por favor, elige un nombre diferente o elimina la imagen existente.")
        return self.cleaned_data['image']

class BackgroundImageAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('name', 'image', 'created')

    form=BackgroundImageAdminForm
            
admin.site.register(BackgroundImage, BackgroundImageAdmin)
