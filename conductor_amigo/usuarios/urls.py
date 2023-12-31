# Este código hace uso de funcionalidades proporcionadas por Django,
# un framework de desarrollo web de código abierto. Utiliza modelos
# personalizados para gestionar sus urls y direcciones

from django.urls import path
from . import views
from .views import UserProfileUpdateView, ProfilePasswordChangeView

# Configuración de URLs
urlpatterns = [
    path("busqueda_usuarios/", views.buscar_usuario, name="busqueda"),
    path("usuario_discapacidad/", views.usuario_discapacidad, name="discapacidad"),
    path("login/", views.login_view, name="login_view"),
    path('registro/inicial',views.registro_inicial,name='registro_inicial'),
    path('registro/conductor',views.registro_conductor,name='registro_conductor'),
    path('registro/estudiante',views.registro_estudiante,name='registro_estudiante'),
    path('privacidad/', views.privacidad, name='privacidad'),
    path('verficar_licencia/',views.verificar_licencia,name='verificar_licencia'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path("Usuario Discapacidad", views.usuario_discapacidad, name='usuario_discapacidad'),
    path('profile/<str:username>/edit/', UserProfileUpdateView.as_view() , name='editar_usuario'),
    path('profile/<str:username>/contrasena/', ProfilePasswordChangeView.as_view(), name='cambio_contrasena'),
    path('calificar/<str:username>/', views.calificar_usuario, name='calificar'),
]