# Este código hace uso de funcionalidades proporcionadas por Django,
# un framework de desarrollo web de código abierto. Utiliza modelos
# personalizados para gestionar sus urls y direcciones

from django.urls import path
from . import views

# Configuración de URLs
urlpatterns = [
    path('lista_viajes/', views.lista_viajes, name='lista_viajes'),
    path("crear_viaje/",views.crear_viaje, name='crear_viaje'),
    path('detalle_viaje/<str:viaje_id>/', views.detalle_viaje, name='detalle_viaje'),
    path("viaje/",views.viaje,name="viaje"),
    path('viaje/<str:accion>/<str:viaje_id>/', views.accion_viaje,name='accion_viaje')
]