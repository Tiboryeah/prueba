from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Cuenta

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Crear una instancia del modelo Cuenta asociada al usuario
        Cuenta.objects.create(user=instance, correo=instance.email)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    # Guardar cambios en el modelo Cuenta si se actualiza el usuario
    instance.cuenta.save()
