from django.contrib import admin
from .models import TipoPrenda, Disenador, Cuenta

# Personalización del modelo TipoPrenda en el admin
class TipoPrendaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Muestra el nombre del tipo de prenda
    search_fields = ('nombre',)  # Permite buscar por el nombre del tipo de prenda

# Personalización del modelo Disenador en el admin
class DisenadorAdmin(admin.ModelAdmin):
    raw_id_fields = ['usuario']  # Asegúrate de que 'usuario' es ForeignKey
    list_display = ['usuario', 'tipo_prenda', 'imagen']

# Registra el modelo UNA SOLA VEZ
admin.site.register(Disenador, DisenadorAdmin)

# Personalización del modelo Cuenta en el admin
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('user', 'apellido', 'correo')  # Muestra el nombre de usuario, apellido y correo
    search_fields = ('user__username', 'correo')  # Permite buscar por el nombre de usuario o correo

# Registrar los modelos con sus clases de administración
admin.site.register(TipoPrenda, TipoPrendaAdmin)
admin.site.register(Cuenta, CuentaAdmin)
