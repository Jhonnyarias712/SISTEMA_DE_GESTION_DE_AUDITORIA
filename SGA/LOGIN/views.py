from django.shortcuts import render
from django.http import HttpResponse

def auditoria_view(request):
    return render(request, 'LOGIN_SGA.html')

def crea_user_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'lol.html', context)

