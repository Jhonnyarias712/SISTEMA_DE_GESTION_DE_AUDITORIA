from django.urls import path
from .views import auditoria_view
from .views import crea_user_view
from .views import crea_plantilla_view
from .views import agendar_auditoria_view
from .views import auditoria_view
from .views import evalua_actividad_view
from .views import historial_auditorias_view
from .views import login_view
from .views import home_view
from .views import guardar_usuario
from .views import guardar_usuario_2
from .views import formulario_actividades
from .views import formulario_view
from .views import agendar_auditoria_jar




urlpatterns = [
    path('', login_view, name='LOGIN'),
    path('crear_usuario/', crea_user_view, name='CREAR_USUARIO'),
    path('crear_plantilla/', crea_plantilla_view, name='CREAR_PLANTILLA'), 
    path('agendar_auditoria/', agendar_auditoria_view, name='AGENDAR_AUDITORIA'),
    path('agendar_auditoria/<int:pk>/', agendar_auditoria_view, name='AGENDAR_AUDITORIA_EDITAR'),
    path('auditoria/', auditoria_view, name='AUDITORIA'),
    #path('auditoria/<int:pk>/', auditoria_view, name='AUDITORIA_EDITAR'),
    path('evalua_actividad/', evalua_actividad_view, name='EVALUA_ACTIVIDAD'),
    path('formulario_view/', formulario_view, name='FORMULARIO_ACTIVIDAD'),
    path('evalua_actividad/<int:pk>/', evalua_actividad_view, name='EVALUA_ACTIVIDAD_EDITAR'),
    path('formulario_view/<int:pk>/', formulario_view, name='FORMULARIO_ACTIVIDAD_EDITAR'),
    path('historial/', historial_auditorias_view, name='HISTORIAL'),
    path('home/', home_view, name='HOME'),
    path('guardar_usuario/', guardar_usuario, name='guardar_usuario'),
    path('formulario_actividades/', formulario_actividades, name='formulario_actividades'),
    path('guardar_usuario/', guardar_usuario_2, name='guardar_usuario_2'),
    path('agenda_auditoria_jar/', agendar_auditoria_jar, name='AGENDA_AUDITORIA_JAR'),
    
    
]