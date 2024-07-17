from django.shortcuts import get_object_or_404, render,redirect
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

def delete_user(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')  # Obtener el nombre completo del usuario a eliminar
        
        try:
            user_to_delete = get_object_or_404(USERS, full_name=full_name)  # Buscar usuario por nombre completo
            
            if '_delete' in request.POST:
                user_to_delete.delete()  # Eliminar el usuario
                
                # Podrías añadir un mensaje de éxito o redirigir a otra vista
                return redirect('guardar_usuario')  # Redirigir a la página donde se guarda el usuario, por ejemplo
            
        except USERS.DoesNotExist:
            # Manejar el caso donde el usuario no existe
            print(f"El usuario con nombre completo '{full_name}' no existe.")
            pass
    
    # Renderizar la página nuevamente o redirigir a donde sea necesario
    return render(request, 'guardar_usuario.html', {})

def guardar_usuario(request):
    if request.method == 'POST':
        if '_get' in request.POST:
            return redirect('guardar_usuario') 

        elif '_delete' in request.POST:
            print('Entra al seccion eliminar')
            usuario_id = request.POST.get('usuario_cb')
            print(f'ENCONTRADO: {usuario_id}')
            user_to_delete = get_object_or_404(USERS, id_usuario=usuario_id)
            user_to_delete.delete()
            return redirect('guardar_usuario') 
                
        elif '_save' in request.POST:
            print('Entra al if del boton')
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


            return redirect('guardar_usuario') 
    
    # Obtener todos los usuarios para mostrar en la página
    users = USERS.objects.all()
    context = {
        'USERS': users,
    }

    return render(request, 'guardar_usuario.html', context)


def guardar_usuario_2(request):
    if request.method == 'POST':
        if '_save' in request.POST:
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