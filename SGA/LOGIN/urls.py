from django.urls import path
from .views import auditoria_view
from .views import crea_user_view
from .views import crea_plantilla_view
from .views import agendar_auditoria_view
from .views import auditoria_view
from .views import evalua_actividad_view
from .views import historial_auditorias_view

urlpatterns = [
    path('', auditoria_view, name='LOGIN'),
    path('crear_usuario/', crea_user_view, name='CREAR_USUARIO'),
    path('crear_plantilla/', crea_plantilla_view, name='CREAR_PLANTILLA'),
    path('agendar_auditoria/', agendar_auditoria_view, name='AGENDAR_AUDITORIA'),
    path('auditoria/', auditoria_view, name='AUDITORIA'),
    path('evalua_actividad/', evalua_actividad_view, name='EVALUA_ACTIVIDAD'),
    path('historial/', historial_auditorias_view, name='HISTORIAL'),
    
]