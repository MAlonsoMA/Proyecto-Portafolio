from django.db import models
from django.core.validators import MaxLengthValidator
from ckeditor.fields import RichTextField
import os
import uuid
from django.conf import settings
from django.core.files.storage import default_storage
from PIL import Image

def profile_picture_path(instance, filename):
    # Generar un nombre aleatorio usando la libreria uuid
    random_filename = str(uuid.uuid4())
    # Recupero la extensión del archivo de imagen
    extension = os.path.splitext(filename)[1]
    # Devuelvo la ruta completa final del archivo
    return 'projects/{}/{}{}'.format(instance.title, random_filename, extension)

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título')
    description = models.TextField(validators=[MaxLengthValidator(400)], verbose_name='Descripción')
    detalle = RichTextField(verbose_name='Detalle')
    image = models.ImageField(default='default.jpg',upload_to=profile_picture_path, verbose_name='Imagen')
    pie = models.CharField(max_length=100, blank=True, null=True, verbose_name='pie')
    autor = models.CharField(max_length=100, blank=True, null=True, verbose_name='autor')
    link = models.URLField(max_length=180, blank=True, null=True, verbose_name='Enlace Github')
    link_i = models.URLField(max_length=180, blank=True, null=True, verbose_name='Enlace Web')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha Modificación')

    def save(self, *args, **kwargs):
        # Verificar que la imagen que estoy subiendo es diferente a la predeterminada
        if self.pk and self.image.name != 'default.jpg':
            old_profile = Project.objects.get(pk=self.pk)
            default_image_path = os.path.join(settings.MEDIA_ROOT, 'default.jpg')

            if old_profile.image.path != self.image.path and old_profile.image.path != default_image_path:
                # Voy a eliminar la imagen anterior si es distinta de la actual y distinta de default.jpg
                default_storage.delete(old_profile.image.path)
        super(Project, self).save(*args, **kwargs)

        # Todo el codigo para recortar y redimensionar la imagen
        if self.image and os.path.exists(self.image.path):
            # Redimensionar la imagen antes de guardarla
            with Image.open(self.image.path) as img:
                ancho, alto = img.size

                if ancho > alto:
                    # La imagen es mas ancha que alta
                    nuevo_alto = 500
                    #nuevo_ancho = int((ancho/alto) * nuevo_alto)
                    nuevo_ancho = 850
                    img = img.resize((nuevo_ancho, nuevo_alto))
                    img.save(self.image.path)
                elif alto > ancho:
                    # La imagen es mas alta que ancha
                    nuevo_ancho = 500
                    #nuevo_alto = int((alto/ancho) * nuevo_ancho )
                    nuevo_alto = 850
                    img = img.resize((nuevo_ancho, nuevo_alto))
                    img.save(self.image.path)
                else:
                    # La imagen es cuadrada
                    img=img.resize((500,500))
                    img.save(self.image.path)

            # El recorte de la imagen final
            with Image.open(self.image.path) as img:
                """ ancho, alto = img.size

                    if ancho > alto:
                    left = (ancho - alto) / 2
                    top = 0
                    right = (ancho + alto) / 2
                    bottom = alto
                else:
                    left = 0
                    top = (alto - ancho) / 2
                    right = ancho
                    bottom = (alto + ancho) / 2

                img = img.crop((left, top, right, bottom)) """
                #comprimimos la imagen, 1-95, 1 minima calidad, 95 maxima
                calidad=60
                img.save(self.image.path,optimize=True,quality=calidad)

    # Pasos para convertir al español la aplicación en el admin y ordenación de los registros 
    # de acuerdo al campo 'created' de forma descendente
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    # Con esta función logro mostrar en la lista de proyectos del admin, todos los proyectos con su titulo
    def __str__(self):
        return self.title

