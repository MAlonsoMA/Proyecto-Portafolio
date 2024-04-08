from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portfolio'
    # Configuración extendida para cambiar el nombre de la aplicación en el sector admin
    verbose_name = 'Portafolio'         
