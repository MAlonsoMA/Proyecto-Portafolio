from django.apps import AppConfig

class AboutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'
    # Configuración extendida para cambiar el nombre de la aplicación en el sector admin
    verbose_name = 'Acerca de'
