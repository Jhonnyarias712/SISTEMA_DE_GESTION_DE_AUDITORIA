from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return render(request, 'LOGIN_SGA.html')

def crea_user_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'crear_usuario.html', context)

def crea_plantilla_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'crear_plantilla.html',context)

def agendar_auditoria_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'agendar_auditoria.html',context)


def auditoria_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'auditoria.html',context)


def evalua_actividad_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'evualuar_actividades.html',context)


def historial_auditorias_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'historial_auditoria.html',context)


def home_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'home_auditor.html',context)