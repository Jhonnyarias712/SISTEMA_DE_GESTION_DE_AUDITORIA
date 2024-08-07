"""
URL configuration for SGA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('LOGIN.urls')),
    path('admin/', admin.site.urls),
    #path('LOGIN/', include('LOGIN.urls')),
    path('LOGIN/', include('LOGIN.urls')),
    #path('XD/', include('LOGIN.urls'),name='XD'),
    path('LOGIN/crear_usuario/', include('LOGIN.urls'),name='CREAR_USUARIO'),
    path('LOGIN/guardar_usuario/', include('LOGIN.urls'),name='guardar_usuario'),
    path('LOGIN/crear_plantilla/', include('LOGIN.urls'),name='CREAR_USUARIO'),
    path('LOGIN/agendar_auditoria/', include('LOGIN.urls'),name='AGENDAR_AUDITORIA'),
    path('LOGIN/auditoria/', include('LOGIN.urls'),name='AUDITORIA'),
    path('LOGIN/evalua_actividad/', include('LOGIN.urls'),name='EVALUA_ACTIVIDAD'),
    path('LOGIN/historial/', include('LOGIN.urls'),name='HISTORIAL'),
    path('LOGIN/home/', include('LOGIN.urls'),name='HOME'),
    path('LOGIN/formulario_actividades/', include('LOGIN.urls'),name='formulario_actividades'),
    path('LOGIN/agenda_auditoria_jar/', include('LOGIN.urls'),name='AGENDA_AUDITORIA_JAR'),
]
