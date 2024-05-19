from django.shortcuts import render
from django.http import HttpResponse

def auditoria_view(request):
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
