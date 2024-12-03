from django.db import models
from django.contrib.auth.models import User  # Utilizamos el modelo User de Django para gestionar usuarios.

# Tipo de Prenda (solo 5 tipos predefinidos)
class TipoPrenda(models.Model):
    CAMISETA = 'Camiseta'
    CHAQUETA = 'Chaqueta'
    PANTALON = 'Pantalón'
    SUDADERA = 'Sudadera'
    VESTIDO = 'Vestido'

    TIPO_PRENDA_CHOICES = [
        (CAMISETA, 'Camiseta'),
        (CHAQUETA, 'Chaqueta'),
        (PANTALON, 'Pantalón'),
        (SUDADERA, 'Sudadera'),
        (VESTIDO, 'Vestido'),
    ]

    nombre = models.CharField(max_length=50, choices=TIPO_PRENDA_CHOICES, unique=True)

    def __str__(self):
        return self.nombre


# Diseño (cada usuario puede crear un diseño para un tipo de prenda)
class Disenador(models.Model):
    nombre = models.CharField(max_length=255)  # Nombre del diseño
    imagen = models.ImageField(upload_to='disenos/')  # Imagen del diseño (URL)
    tipo_prenda = models.ForeignKey(TipoPrenda, on_delete=models.CASCADE)  # Relación con TipoPrenda
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relación con el modelo User (quién es el diseñador)

    def __str__(self):
        return f"{self.nombre} - {self.tipo_prenda.nombre} ({self.usuario.username})"


class Cuenta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido = models.CharField(max_length=255, default="Desconocido")  # Valor predeterminado agregado
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.first_name} {self.apellido}"
