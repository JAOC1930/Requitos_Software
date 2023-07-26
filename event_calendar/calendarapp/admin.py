from django.contrib import admin
from calendarapp import models
from .models.archivos import Archivos, Asignacion, Carrera, Ciclo, CarreraCiclo, Materia

@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    model = models.Event
    list_display = [
        "id",
        "title",
        "user",
        "is_active",
        "is_deleted",
        "created_at",
        "updated_at",
    ]
    list_filter = ["is_active", "is_deleted"]
    search_fields = ["title"]


@admin.register(models.EventMember)
class EventMemberAdmin(admin.ModelAdmin):
    model = models.EventMember
    list_display = ["id", "event", "user", "created_at", "updated_at"]
    list_filter = ["event"]

class CarreraAdmin(admin.ModelAdmin):
    model = Carrera
    list_display = ['nombre']
    list_filter = ['nombre']

admin.site.register(Carrera, CarreraAdmin)

class CicloAdmin(admin.ModelAdmin):
    model = Ciclo
    list_display = ['numCiclo']
    list_filter = ['numCiclo']

admin.site.register(Ciclo, CicloAdmin)

class CarreraCicloAdmin(admin.ModelAdmin):
    model = CarreraCiclo
    list_display = ['carrera', 'ciclo']
    list_filter = ['carrera', 'ciclo']

admin.site.register(CarreraCiclo, CarreraCicloAdmin)   

class MateriaAdmin(admin.ModelAdmin):
    model = Materia
    list_display = ['nombre', 'numCreditos', 'numHoras', 'carrera', 'ciclo']
    list_display = ['nombre', 'numCreditos', 'numHoras', 'carrera', 'ciclo']
admin.site.register(Materia, MateriaAdmin)

class AsignacionAdmin(admin.ModelAdmin):
    model = Asignacion
    list_display = ['id','nombre', 'carrera', 'ciclo', 'materia', 'user', 'fecha_inicial', 'fecha_final', 'descripcion']
    list_filter = ['nombre', 'carrera', 'ciclo', 'materia', 'user', 'fecha_inicial', 'fecha_final', 'descripcion']

admin.site.register(Asignacion, AsignacionAdmin)

class ArchivoAdmin(admin.ModelAdmin):
    model = Archivos
    list_display = ['archivo','user', 'fecha_subida', 'materia', 'asignacion']
    list_filter = ['archivo','user', 'fecha_subida', 'materia', 'asignacion']

admin.site.register(Archivos, ArchivoAdmin)