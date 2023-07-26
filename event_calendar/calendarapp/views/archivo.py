from django.shortcuts import render, redirect
from calendarapp.forms import ArchivoForm, AsignacionForm
from calendarapp.models.archivos import Archivos, Asignacion, Carrera, Ciclo, Materia, CarreraCiclo
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from calendarapp.models import Event

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = form.cleaned_data['archivo']
            if archivo:
                nuevo_archivo = form.save(commit=False)  # Guarda el formulario pero no en la base de datos todavía
                nuevo_archivo.user = request.user  # Establece el usuario actual como el valor del campo 'user'
                nuevo_archivo.save()  # Ahora guarda el objeto 'Archivos' en la base de datos
            return redirect(request.path)  # Cambiar redirect(index) por redirect('index')
    else:
        form = ArchivoForm()
    return render(request, 'archivo.html', {'form': form})
    
def archivos_subidos(request):
    archivos = Archivos.objects.filter(user=request.user)
    return render(request, 'archivos_subidos.html', {'archivos': archivos})    

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

def visualizar(request):
    carrera = Carrera.objects.all()
    return render(request, 'visualizar.html', {'carreras': carrera})

def obtener_Ciclo(request, id_carrera):
    try:
        carrera = Carrera.objects.get(pk=id_carrera)
        ciclos = CarreraCiclo.objects.filter(carrera=carrera)
    except Carrera.DoesNotExist:
        # Si la carrera no existe, puedes manejarlo como desees (por ejemplo, mostrar un mensaje de error).
        ciclos = []

    return render(request, 'v_ciclos.html', {'ciclos': ciclos, 'carreras': carrera})

def obtener_Materia(request, id):
    try:
        ciclo = Ciclo.objects.get(pk=id)
        materias = Materia.objects.filter(ciclo=ciclo)
    except Ciclo.DoesNotExist:
        # Si el ciclo no existe, puedes manejarlo como desees (por ejemplo, mostrar un mensaje de error).
        materias = []

    return render(request, 'v_materias.html', {'ciclo': ciclo, 'materias': materias})

def obtenerArchivoM(request, id):
    try:
        materia = Materia.objects.get(pk=id)
        archivos = Archivos.objects.filter(materia=materia)
    except Materia.DoesNotExist:
        # Si el ciclo no existe, puedes manejarlo como desees (por ejemplo, mostrar un mensaje de error).
        archivos = []

    return render(request, 'v_archivosM.html', {'materias': materia, 'archivos': archivos})

def obtener_superusuario(request):
    superusuario = User.objects.filter(is_superuser=True).first()
    return render(request, 'superusuario.html', {'superusuario': superusuario})
