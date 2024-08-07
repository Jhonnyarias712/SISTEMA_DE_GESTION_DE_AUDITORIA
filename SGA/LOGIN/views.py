from datetime import timezone
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import USERS,Plantilla,Formulario,AgendaAuditorias,Auditoria,EvaluacionActividad,Formulario
import json
from django.core.serializers.json import DjangoJSONEncoder  # Importa el encoder de Django para manejar datetime
from .forms import AgendaAuditoriasForm, AuditoriaForm, AuditarForm, FormularioForm


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


def formulario_actividades(request):
    
    #print(f"nombre_plantilla: {formulario}")
    print("Entra actividades")

    if request.method == 'POST':
        print("Entra POST DELETE")
        
        if '_delete_act' in request.POST:
            Formulario_cb = request.POST.get('formulario_cb')
            print(f'ENCONTRADO: {Formulario_cb}')

            formulario = get_object_or_404(Formulario, id_actividad=Formulario_cb) 
            formulario.delete()
            return redirect('formulario_actividades')

        elif '_save_act' in request.POST:
        
            Plantilla_cb = request.POST.get('Plantilla_cb')
            actividad = request.POST.get('actividad')
            print(f'Plantilla_cb: {Plantilla_cb}')
            print(f'actividad ENCONTRADO: {actividad}')

            
            Plantilla_encontrada = get_object_or_404(Plantilla, id_plantilla=Plantilla_cb) 
            print(f'Plantilla_encontrada: {Plantilla_encontrada}')
            
            nueva_actividad_form = Formulario(
                plantilla=Plantilla_encontrada,
                actividad=actividad,
            )
            nueva_actividad_form.save()
            

    plantilla = Plantilla.objects.all()
    formulario = Formulario.objects.all()

    context = {
        'Plantilla': plantilla,   
        'Formulario'  :formulario,
    }
    return render(request, 'formulario_actividades.html',context)


def agendar_auditoria_jar(request):
    
    #print(f"nombre_plantilla: {formulario}")
    print("Entra a agendar_auditoria_jar")

    if request.method == 'POST':
        print("Entra POST ")
        
        if '_delete_age' in request.POST:
            print(f'Entra a delete ')   
            Auditorias_cb = request.POST.get('auditorias_cb')
            print(f'ENCONTRADO: {Auditorias_cb}')
            auditoria = get_object_or_404(AgendaAuditorias, id_agenda=Auditorias_cb) 
            auditoria.delete()  
            print('ELIMINADO')            
            return redirect('AGENDA_AUDITORIA_JAR')

        elif '_save_age' in request.POST:
            print("Entra SAVE ")
            Plantilla_cb = request.POST.get('Plantilla_cb')
            User_cb = request.POST.get('owner')
            print(f'Plantilla_cb: {Plantilla_cb}')
            print(f'User ENCONTRADO: {User_cb}')

            Plantilla_encontrada = get_object_or_404(Plantilla, id_plantilla=Plantilla_cb)
            USERS_encontrada = get_object_or_404(USERS, id_usuario=User_cb)
            print(f'Plantilla_encontrada ENCONTRADO: {Plantilla_encontrada}')
            print(f'USERS_encontrada ENCONTRADO: {USERS_encontrada}')
            fecha_inicio = request.POST.get('fecha_inicio')
            fecha_fin = request.POST.get('fecha_fin')

            nueva_AgendaAuditorias = AgendaAuditorias(
            nombre_entidad =  request.POST.get('nombre_entidad'),
            tipo_entidad = request.POST.get('tipo_entidad'),
            sector_industria = request.POST.get('sector_industria'),
            direccion = request.POST.get('direccion'),
            contacto_entidad_email = request.POST.get('contacto_entidad_email'),
            fecha_inicio = fecha_inicio,
            fecha_fin = fecha_fin,
            duracion_dia = request.POST.get('duracion_dia'),
            area_departamento = request.POST.get('area_departamento'),
            auditor = USERS_encontrada,
            fk_plantilla = Plantilla_encontrada,
            objetivo = request.POST.get('objetivo')
            )
            print(f'nueva_AgendaAuditorias: {nueva_AgendaAuditorias}')
            nueva_AgendaAuditorias.save()

            Auditoria_nueva=Auditoria(
                agenda_auditorias = nueva_AgendaAuditorias,
                fecha_inicio_auditoria = nueva_AgendaAuditorias.fecha_inicio,
                fecha_fin_auditoria = nueva_AgendaAuditorias.fecha_fin,
                fecha_inicio_plazo = None,
                estado_auditoria = "Evaluando",
                observacion = None,
                fecha_fin_plazo = None,
                fecha_cierre_auditoria = None,
                )
            Auditoria_nueva.save()

            print(f'gUARDADO CORRECTAMENTE')
            redirect('AGENDA_AUDITORIA_JAR')
            

    plantilla = Plantilla.objects.all()
    agendaAuditorias = AgendaAuditorias.objects.all()
    users = USERS.objects.all()

    context = {
        'Plantilla': plantilla,
        'USERS':users,   
        'AgendaAuditorias':agendaAuditorias,
    }
    return render(request, 'agenda_auditoria_jar.html',context)



def agendar_auditoria_view(request, pk=None):
    if pk:
        instance = get_object_or_404(AgendaAuditorias, pk=pk)
    else:
        instance = None

    if request.method == 'POST':
        form = AgendaAuditoriasForm(request.POST, instance=instance)
        
        if form.is_valid():
            if '_delete' in request.POST:
                instance.delete()
                return redirect('AGENDAR_AUDITORIA')  # Redirige a la misma página después de eliminar
            
            instance = form.save()

            if '_continue' in request.POST:
                return redirect('AGENDAR_AUDITORIA_EDITAR', pk=instance.pk)
            else:
                return redirect('AGENDAR_AUDITORIA')  # Redirige a la misma página después de guardar
    else:
        form = AgendaAuditoriasForm(instance=instance)

    # Obtener todas las auditorías
    auditorias = AgendaAuditorias.objects.all()

    # Añadir las auditorías al contexto
    context = {
        'form': form,
        'auditorias': auditorias,
    }
    return render(request, 'agendar_auditoria.html', context)


def auditoria_view(request):
    
    if '_delete_age' in request.POST:
            print(f'Entra a delete ')   
            Auditorias_cb = request.POST.get('auditorias_cb')
            print(f'ENCONTRADO: {Auditorias_cb}')
            auditoria = get_object_or_404(Auditoria, id_agenda=Auditorias_cb) 
            auditoria.delete()  
            print('ELIMINADO')            
            return redirect('AUDITORIA')
    elif '_auditar' in request.POST:
        print(f'Entra a auditar ')
        return redirect('EVALUA_ACTIVIDAD')


    auditoria = Auditoria.objects.all()
    agendaAuditorias = AgendaAuditorias.objects.all()
    context = {
    'AUDITORIA': auditoria,
    'AGENDAAUDITORIAS':agendaAuditorias,
    }

    return render(request, 'auditoria.html', context)


def evalua_actividad_view(request):


    if '_delete' in request.POST:
        print(f'Entra a delete ')   
        Auditorias_cb = request.POST.get('auditorias_cb')
        print(f'ENCONTRADO: {Auditorias_cb}')
        evaluacionActividad = get_object_or_404(EvaluacionActividad, id=Auditorias_cb) 
        evaluacionActividad.delete()  
        print('ELIMINADO')            
        return redirect('EVALUA_ACTIVIDAD_EDITAR')
    elif '_save' in request.POST:
        print(f'Entra a _save ')
        Auditorias_cb = request.POST.get('auditorias_cbb')
        formulario_cb = request.POST.get('formulario_cb')
        Auditoria_encontrado = get_object_or_404(Auditoria, id_auditar=Auditorias_cb) 
        Formulario_encontrado = get_object_or_404(Formulario, id_actividad=formulario_cb) 
        print(f'Auditoria_encontrado: {Auditoria_encontrado} ')
        print(f'formulario_cb:  {formulario_cb} ')


        respuesta = request.POST.get('respuesta')
        observaciones = request.POST.get('observaciones')
        plazo_ini_observacion = request.POST.get('plazo_ini_observacion')
        plazo_fin_observacion = request.POST.get('plazo_fin_observacion')

        evaluacion_EvaluacionActividad = EvaluacionActividad(
        auditoria_id = Auditoria_encontrado,
        id_actividad = Formulario_encontrado,
        respuesta = respuesta,
        observaciones = observaciones,
        plazo_ini_observacion = plazo_ini_observacion,
        plazo_fin_observacion = plazo_fin_observacion
        )
        print(f'creado:  {evaluacion_EvaluacionActividad} ')
        evaluacion_EvaluacionActividad.save()
        print(f'Guardado exitosamente ')
        return redirect('EVALUA_ACTIVIDAD_EDITAR')



        
    auditoria = Auditoria.objects.all()
    agendaAuditorias = AgendaAuditorias.objects.all()
    formulario = Formulario.objects.all()
    evaluacionActividad = EvaluacionActividad.objects.all()

    context = {
    'AUDITORIA': auditoria,
    'AGENDAAUDITORIAS':agendaAuditorias,
    'FORMULARIO':formulario,
    'EVALUACIONACTIVIDAD':evaluacionActividad,
    }

    return render(request, 'evualuar_actividades.html', context)

def formulario_view(request, pk=None):
    if pk:
        instance = get_object_or_404(Formulario, pk=pk)
    else:
        instance = None

    if request.method == 'POST':
        form = FormularioForm(request.POST, instance=instance)
        
        if form.is_valid():
            if '_delete' in request.POST:
                instance.delete()
                return redirect('EVALUA_ACTIVIDAD')
            
            instance = form.save()

            if '_continue' in request.POST:
                return redirect('EVALUA_ACTIVIDAD_EDITAR', pk=instance.pk)
            else:
                return redirect('EVALUA_ACTIVIDAD')
    else:
        form = FormularioForm(instance=instance)   

    # No es necesario crear un segundo formulario aquí
    context = {
        'form': form,
        'MENSAJE': 'EVALUAR FORMULARIO',
    }
    return render(request, 'evualuar_actividades.html', context)


def historial_auditorias_view(request):
    # Ajusta los nombres de los campos según tus modelos
    DATOS_AUDITORIA = AgendaAuditorias.objects.all()
    INICIO_AUDITORIA = Auditoria.objects.all()
    ESTADO = EvaluacionActividad.objects.all()
    context = {
        'DATOS_AUDITORIA': DATOS_AUDITORIA,
        'INICIO_AUDITORIA': INICIO_AUDITORIA,
        'ESTADO': ESTADO,
    }
    return render(request, 'historial_auditoria.html', context)


def home_view(request):
    context = {
        'MENSAJE': 'CREAR AUDITOR',      
    }
    return render(request, 'home_auditor.html',context)