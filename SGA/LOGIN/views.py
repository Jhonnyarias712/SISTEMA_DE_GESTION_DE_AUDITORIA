from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import USERS

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = USERS.objects.get(usuario=username, password=password)
            return redirect(home_view)
        except USERS.DoesNotExist:
            messages.error(request, 'Credenciales incorrectas')
            return render(request, 'LOGIN_SGA.html')
    else:
        return render(request, 'LOGIN_SGA.html')

def crea_user_view(request):
    User = USERS.objects.all()
    context = {
        'USERS':User,      
    }
    return render(request, 'crear_usuario.html', context)

def guardar_usuario(request):
    User = USERS.objects.all()
    context = {
        'USERS':User,      
    }
    print('Entra al metodo guardar_usuario')
    print(request.POST)

    if request.method == 'POST':
        
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        tipo_usuario = request.POST.get('tipo_usuario')
        estado = request.POST.get('estado')
        new_user = USERS(usuario=usuario, password=password, full_name=full_name,
                         tipo_usuario=tipo_usuario, estado=estado)
        #new_user = USERS.objects.create(usuario=usuario, password=password, full_name=full_name,
        #                 tipo_usuario=tipo_usuario, estado=estado)
        
        new_user.save()


        #return redirect(reversed('login_view')) 

    return render(request, 'guardar_usuario.html',context)


def guardar_usuario_2(request):
    if request.method == 'POST':
        print(request.POST)  # Verifica qué datos se están enviando desde el formulario
        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        tipo_usuario = request.POST.get('tipo_usuario')
        estado = request.POST.get('estado')

        # Crear un nuevo objeto de usuario y guardarlo en la base de datos
        new_user = USERS(usuario=usuario, password=password, full_name=full_name,
                         tipo_usuario=tipo_usuario, estado=estado)
        new_user.save()

        # Redirigir a la página donde se muestra la lista de usuarios (o cualquier otra página deseada)
        return redirect('CREAR_USUARIO')

    # Si no es método POST, simplemente renderiza la página con el formulario vacío
    return render(request, 'crear_usuario.html')


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