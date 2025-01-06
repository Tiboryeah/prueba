from django.db import models
from django.contrib.auth.models import User  # Utilizamos el modelo User de Django para gestionar usuarios.
from django.core.files.base import ContentFile


# Tipo de Prenda (solo 5 tipos predefinidos)
class TipoPrenda(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Disenador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_prenda = models.ForeignKey(TipoPrenda, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='disenos/')

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo_prenda.nombre}"

class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido = models.CharField(max_length=255, default="Desconcido")
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128, default="contraseña_default")  # Define un valor predeterminado
