from django.db import models
import os
from .custom_storage import OverwriteStorage

def profile_picture_path(instance, filename):
    # Generar un nombre aleatorio usando la libreria uuid
    #random_filename = str(uuid.uuid4())
    #Recupero la extensión del archivo de imagen
    extension = os.path.splitext(filename)[1]
    # Devuelvo la ruta completa final del archivo
    return 'backgrounds/{}{}'.format(instance.name,extension)

class BackgroundImage(models.Model):
    name= models.CharField(unique=True,max_length=150, verbose_name='Nombre')
    image=models.ImageField(storage=OverwriteStorage(),upload_to=profile_picture_path,verbose_name='Imagen')
    title = models.CharField(max_length=100, blank=True, null=True, verbose_name='titular')
    subtitle = models.CharField(max_length=100, blank=True, null=True, verbose_name='subtitular')
    sentence = models.TextField(max_length=400, blank=True, null=True, verbose_name='Frase')
    created = models.DateTimeField(verbose_name="Fecha de Creación", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')
        
    class Meta:
        verbose_name = 'titular e imagen de fondo'
        verbose_name_plural = 'titulares e imágenes de fondo'

    def __str__(self):
        return self.name
