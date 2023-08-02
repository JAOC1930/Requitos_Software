from django.shortcuts import render, redirect
from calendarapp.forms import ArchivoForm, AsignacionForm
from calendarapp.models.archivos import Archivos, Asignacion, Carrera, Ciclo, Materia, CarreraCiclo
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from calendarapp.models import Event
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponseForbidden
from django.urls import reverse

def es_superusuario(user):
    return user.is_superuser

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = ArchivoForm(request.user, request.POST, request.FILES)
        if form.is_valid():
            archivo = form.cleaned_data['archivo']
            if archivo:
                nuevo_archivo = form.save(commit=False)
                nuevo_archivo.user = request.user
                nuevo_archivo.asignacion = form.cleaned_data['asignacion']  # Accede al valor del campo 'asignacion' del formulario
                nuevo_archivo.save()
            return redirect(request.path)
    else:
        form = ArchivoForm(user=request.user)
    return render(request, 'archivo.html', {'form': form})



@login_required    
def archivos_subidos(request):
    archivos = Archivos.objects.filter(user=request.user)
    return render(request, 'archivos_subidos.html', {'archivos': archivos})    

@login_required
@user_passes_test(es_superusuario, login_url=None)
def agregar_asignacion(request):
    if request.method == 'POST':
        form = AsignacionForm(request.POST)
        if form.is_valid():
            asignacion = form.save()

            # Obtener el usuario seleccionado en el formulario
            user = form.cleaned_data['user']
            event = Event(
                user=form.cleaned_data['user'],  # Asignar el usuario actual (requiere que el usuario esté autenticado)
                title=form.cleaned_data['nombre'],
                description=form.cleaned_data['descripcion'],
                start_time=form.cleaned_data['fecha_inicial'],
                end_time=form.cleaned_data['fecha_final']
            )

            # Guardar la instancia del modelo en la base de datos
            event.save()
            # Enviar el correo el   ectrónico
            send_mail(
                subject='Asignación exitosa',
                message=f'Hola {user.email}, se ha asignado la tarea "{asignacion.nombre}".\nFecha de inicio: {asignacion.fecha_inicial}.\nFecha de entrega: {asignacion.fecha_final}.\nDescripción: {asignacion.descripcion}',
                from_email='tu_correo@gmail.com',  # Coloca aquí tu correo desde el que enviarás los correos
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect(request.path)  # Redirige a la vista que quieras después de guardar el formulario
    else:
        form = AsignacionForm()
        
    return render(request, 'agregar_asignacion.html', {'form': form})

@login_required
@user_passes_test(es_superusuario, login_url=None)
def visualizar(request):
    carrera = Carrera.objects.all()
    return render(request, 'visualizar.html', {'carreras': carrera})

@login_required
@user_passes_test(es_superusuario, login_url=None)
def obtener_Ciclo(request, id_carrera):
    try:
        carrera = Carrera.objects.get(pk=id_carrera)
        ciclos = CarreraCiclo.objects.filter(carrera=carrera)
    except Carrera.DoesNotExist:
        # Si la carrera no existe, puedes manejarlo como desees (por ejemplo, mostrar un mensaje de error).
        ciclos = []

    return render(request, 'v_ciclos.html', {'ciclos': ciclos, 'carreras': carrera})

@login_required
def obtener_Materia(request, id):
    try:
        ciclo = Ciclo.objects.get(pk=id)
        materias = Materia.objects.filter(ciclo=ciclo)
    except Ciclo.DoesNotExist:
        # Si el ciclo no existe, puedes manejarlo como desees (por ejemplo, mostrar un mensaje de error).
        materias = []

    return render(request, 'v_materias.html', {'ciclo': ciclo, 'materias': materias})

@login_required
@user_passes_test(es_superusuario, login_url=None)
def obtenerArchivoM(request, id):
    try:
        materia = Materia.objects.get(pk=id)
        archivos = Archivos.objects.filter(materia=materia)
    except Materia.DoesNotExist:
        # Si el ciclo no existe, puedes manejarlo como desees (por ejemplo, mostrar un mensaje de error).
        archivos = []

    return render(request, 'v_archivosM.html', {'materias': materia, 'archivos': archivos})

def secreNoti(request):
    asignacion = Asignacion.objects.all()
    diccionario = {'asignaciones': asignacion}
    return render(request, 'secreNoti.html', diccionario)


def notificar(request, id):
    asignacion = Asignacion.objects.get(pk=id)
    noti = asignacion.user
    send_mail(
                subject='Asignación exitosa',
                message=f'Por favor hacer la entrega del proyecto que se encuentra disponible hasta {asignacion.fecha_final}',
                from_email='tu_correo@gmail.com',  # Coloca aquí tu correo desde el que enviarás los correos
                recipient_list=[noti],
                fail_silently=False,
            )
    
    return redirect(reverse('calendarapp:visualizar'))

