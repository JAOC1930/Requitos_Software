from django.shortcuts import render, redirect
from calendarapp.forms import ArchivoForm, AsignacionForm
from calendarapp.models.archivos import Archivos, Asignacion
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail


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

            # Enviar el correo electrónico
            send_mail(
                subject='Asignación exitosa',
                message=f'Hola {user.email}, se se ha asignado la tarea "{asignacion.nombre}".',
                from_email='tu_correo@gmail.com',  # Coloca aquí tu correo desde el que enviarás los correos
                recipient_list=[user.email],
                fail_silently=False,
            )

            return redirect(request.path)  # Redirige a la vista que quieras después de guardar el formulario
    else:
        form = AsignacionForm()

    return render(request, 'agregar_asignacion.html', {'form': form})



