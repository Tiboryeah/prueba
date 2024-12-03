# Proyecto_Ropa/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('usuarios.urls')),  # Asegúrate de incluir las rutas de usuarios
]
