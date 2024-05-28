from django.db.models.signals import post_delete
from  django.dispatch import receiver
from .models import BackgroundImage

@receiver(post_delete,sender=BackgroundImage)
def delete_image_on_delete(sender,instance,**kwargs):
    if instance.image:
        instance.image.delete(False)