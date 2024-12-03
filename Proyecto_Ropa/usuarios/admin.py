from django.contrib import admin
from .models import TipoPrenda, Disenador, Cuenta

# Personalización del modelo TipoPrenda en el admin
class TipoPrendaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Muestra el nombre del tipo de prenda
    search_fields = ('nombre',)  # Permite buscar por el nombre del tipo de prenda

# Personalización del modelo Disenador en el admin
class DisenadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo_prenda', 'usuario')  # Muestra el nombre del diseño, tipo de prenda y el usuario
    list_filter = ('tipo_prenda', 'usuario')  # Filtros por tipo de prenda y usuario
    search_fields = ('nombre', 'usuario__username')  # Permite buscar por nombre del diseño o nombre de usuario
    raw_id_fields = ('tipo_prenda', 'usuario')  # Muestra los campos de tipo_prenda y usuario como campos de búsqueda rápida

# Personalización del modelo Cuenta en el admin
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('user', 'apellido', 'correo')  # Muestra el nombre de usuario, apellido y correo
    search_fields = ('user__username', 'correo')  # Permite buscar por el nombre de usuario o correo

# Registrar los modelos con sus clases de administración
admin.site.register(TipoPrenda, TipoPrendaAdmin)
admin.site.register(Disenador, DisenadorAdmin)
admin.site.register(Cuenta, CuentaAdmin)
