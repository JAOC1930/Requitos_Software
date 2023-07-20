from django.contrib import admin
from calendarapp import models
from .models.archivos import Archivos, Asignacion

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

class ArchivoAdmin(admin.ModelAdmin):
    model: Archivos
    list_display = ['archivo','user', 'fecha_subida']
    list_filter = ['archivo','user', 'fecha_subida']

admin.site.register(Archivos, ArchivoAdmin)

class AsignacionAdmin(admin.ModelAdmin):
    model: Asignacion
    list_display = ['nombre', 'user']
    list_filter = ['nombre', 'user']

admin.site.register(Asignacion, AsignacionAdmin)