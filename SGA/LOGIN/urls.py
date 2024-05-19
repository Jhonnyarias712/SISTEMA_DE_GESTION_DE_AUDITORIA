from django.urls import path
from .views import auditoria_view
from .views import crea_user_view
from .views import crea_plantilla_view

urlpatterns = [
    path('', auditoria_view, name='LOGIN'),
    path('crear_usuario/', crea_user_view, name='CREAR_USUARIO'),
    path('crear_plantilla/', crea_plantilla_view, name='CREAR_PLANTILLA'),
]