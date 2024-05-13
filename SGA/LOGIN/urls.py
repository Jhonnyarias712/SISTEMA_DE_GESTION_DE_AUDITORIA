from django.urls import path
from .views import auditoria_view
from .views import crea_user_view

urlpatterns = [
    path('', auditoria_view, name='LOGIN'),
    path('crear_usuario/', crea_user_view, name='CREAR_USUARIO'),
    
]