from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
import os
from .storage import OverwriteStorage

def profile_picture_path(instance, filename):
    # Generar un nombre aleatorio usando la libreria uuid
    #random_filename = str(uuid.uuid4())
    #Recupero la extensión del archivo de imagen
    #extension = os.path.splitext(filename)[1]
    # Devuelvo la ruta completa final del archivo
    return 'backgrounds/{}'.format(instance.name)

class BackgroundImage(models.Model):
    name= models.CharField(max_length=150, verbose_name='Nombre')
    image=models.ImageField(upload_to=profile_picture_path,storage=OverwriteStorage(),verbose_name='Imagen')
    created = models.DateTimeField(verbose_name="Fecha de Creación", auto_now=False, auto_now_add=True)

    def save(self, *args, **kwargs):        
        if self.pk:
            existing_instance=BackgroundImage.objects.get(pk=self.pk)
            if existing_instance.image != self.image:
                print("No se puede modificar una imagen existente. Por favor, elimine la imagen primero y luego suba una nueva.")
                return
        else:
            if BackgroundImage.objects.filter(image=self.image.name).exists():
                BackgroundImage.objects.filter(image=self.image.name).delete()
            super(BackgroundImage,self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)
        super(BackgroundImage,self).delete(*args, **kwargs)

        
    class Meta:
        verbose_name = 'imagen de fondo'
        verbose_name_plural = 'imágenes de fondo'

    def __str__(self):
        return self.image.name
