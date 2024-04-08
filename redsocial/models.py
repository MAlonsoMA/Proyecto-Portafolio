from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.CharField(verbose_name="Clave", max_length=100)
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=250, blank=True, null=True)
    created = models.DateTimeField(verbose_name="Fecha de Creación", auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de Modificación", auto_now=True)

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['name']
    
    def __str__(self):
        return self.name
