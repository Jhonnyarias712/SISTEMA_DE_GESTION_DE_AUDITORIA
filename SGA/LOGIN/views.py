from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import USERS,Plantilla
import json
from django.core.serializers.json import DjangoJSONEncoder  # Importa el encoder de Django para manejar datetime




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

        usuario = request.POST.get('usuario')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name')
        tipo_usuario = request.POST.get('tipo_usuario')
        estado = request.POST.get('estado')
        
        if '_delete' in request.POST:
            print('Entra al seccion eliminar')
            usuario_id = request.POST.get('usuario_cb')
            print(f'ENCONTRADO: {usuario_id}')
            user_to_delete = get_object_or_404(USERS, id_usuario=usuario_id)
            user_to_delete.delete()
            return redirect('guardar_usuario') 
                
        elif '_save' in request.POST:
            print('Entra al if del boton GUARDAR')
            usuario_id = request.POST.get('pk_usuario')
            print(f'usuario_cb: {usuario_id}')
            if usuario_id is not None and str(usuario_id).strip():
                print('Encontrol algo')
                print('Actualizando...')
                user_to_save = get_object_or_404(USERS, id_usuario=usuario_id)
                user_to_save.usuario = usuario
                user_to_save.password = password
                user_to_save.full_name = full_name
                user_to_save.tipo_usuario = tipo_usuario
                user_to_save.estado = estado
                user_to_save.save()
                #return redirect('guardar_usuario')
            else:
                usuario = request.POST.get('usuario')
                password = request.POST.get('password')
                full_name = request.POST.get('full_name')
                tipo_usuario = request.POST.get('tipo_usuario')
                estado = request.POST.get('estado')
                print('No encontrado procede a crear el usuario')
                user_to_save = None
                new_user = USERS(usuario=usuario, password=password, full_name=full_name,
                                tipo_usuario=tipo_usuario, estado=estado
                )
                new_user.save()
                print (new_user.full_name)           
               # return redirect('guardar_usuario')


    
    # Obtener todos los usuarios para mostrar en la página
    users = USERS.objects.all()
    users_json = serialize_users_to_json(users)
    context = {
        'USERS': users,
        'USERS_JSON': users_json,
    }

    return render(request, 'guardar_usuario.html', context)

def serialize_users_to_json(users_queryset):
    users_list = list(users_queryset.values(
        'id_usuario',
        'usuario',
        'password',
        'full_name',
        'tipo_usuario',
        'fecha_creacion',
        'fecha_actualizacion',
        'estado'
    ))  # Convertir queryset a lista de diccionarios
    
    # Formatear los campos datetime a cadenas
    for user in users_list:
        user['fecha_creacion'] = user['fecha_creacion'].strftime('%Y-%m-%d %H:%M:%S')
        user['fecha_actualizacion'] = user['fecha_actualizacion'].strftime('%Y-%m-%d %H:%M:%S')
    
    return json.dumps(users_list, cls=DjangoJSONEncoder)

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
    usuario_id = request.POST.get('usuario_cb')
    if request.method == 'POST':
        #id_plantilla
        nombre_plantilla = request.POST.get('nombre_plantilla')
        tema = request.POST.get('tema')
        
        description = request.POST.get('description')
        created_date = request.POST.get('created_date')

        print(f"nombre_plantilla: {nombre_plantilla}")
        print(f"tema: {tema}")
        
        print(f"description: {description}")
        print(f"created_date: {created_date}")
        
        
        if '_delete_plan' in request.POST:
            print('Entra al seccion eliminar')
            Plantilla_cb = request.POST.get('Plantilla_cb')
            print(f'ENCONTRADO: {usuario_id}')
            user_to_delete = get_object_or_404(Plantilla, id_plantilla=Plantilla_cb)
            user_to_delete.delete()
            return redirect('CREAR_PLANTILLA') #crea_plantilla_view
            
        elif '_save_plan' in request.POST:
            print('Entra al if del boton GUARDAR')
            user_to_owner = get_object_or_404(USERS, id_usuario=usuario_id)
            owner = user_to_owner.id_usuario
            print(f"owner: {owner}")           
            nueva_plantilla = Plantilla(
            nombre_plantilla=nombre_plantilla,
            tema=tema,
            owner=user_to_owner,
            description=description,
            created_date=created_date
            )
            # Guardar la nueva instancia en la base de datos
            nueva_plantilla.save()
            print('Guardado con exito')
            print (nueva_plantilla.nombre_plantilla)           
               # return redirect('guardar_usuario')
        

    
    # Obtener todos los usuarios para mostrar en la página
    plantilla = Plantilla.objects.all()
    #plantilla_json = serialize_users_to_json(plantilla)
    users = USERS.objects.all()
    #users_json = serialize_users_to_json(users)
    
    context = {
        'Plantilla': plantilla,
        #'Plantilla_JSON': plantilla_json,
        'USERS': users,
    }

    return render(request, 'crear_plantilla.html', context)

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