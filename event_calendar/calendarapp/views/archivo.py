from django.shortcuts import render, redirect
from calendarapp.forms import ArchivoForm
from calendarapp.models.archivos import Archivos
from django.contrib.auth.decorators import login_required

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

# def subir_archvio(request):
#     """
#     """
#     if request.method=='POST':
#         formulario = ArchivoForm(request.POST)
#         print(formulario.errors)
#         if formulario.is_valid():
#             formulario.save() # se guarda en la base de datos
#             return redirect(subir_archvio)
#     else:
#         formulario = ArchivoForm()
#     diccionario = {'formulario': formulario}

#     return render(request, 'archivo.html', diccionario)