from django.urls import path

from . import views
from .views import archivo

app_name = "calendarapp"


urlpatterns = [
    path("calender/", views.CalendarViewNew.as_view(), name="calendar"),
    path("calenders/", views.CalendarView.as_view(), name="calendars"),
    path("event/new/", views.create_event, name="event_new"),
    path("event/edit/<int:pk>/", views.EventEdit.as_view(), name="event_edit"),
    path("event/<int:event_id>/details/", views.event_details, name="event-detail"),
    path(
        "add_eventmember/<int:event_id>", views.add_eventmember, name="add_eventmember"
    ),
    path(
        "event/<int:pk>/remove",
        views.EventMemberDeleteView.as_view(),
        name="remove_event",
    ),
    path("all-event-list/", views.AllEventsListView.as_view(), name="all_events"),
    path(
        "running-event-list/",
        views.RunningEventsListView.as_view(),
        name="running_events",
    ),
    path('upload/', archivo.upload_file, name='upload_file'),
    path('archivos-subidos/', archivo.archivos_subidos, name='archivos_subidos'),
    path('crear-asignacion/', archivo.agregar_asignacion, name='crear_asignacion'),
    path('visualizar/', archivo.visualizar, name='visualizar'),
    path('visualizar/ciclo/<int:id_carrera>/', archivo.obtener_Ciclo, name='v_ciclo'),
    path('visualizar/materia/<int:id>', archivo.obtener_Materia, name='v_materias'),
    path('visualizar/archivo/materia/<int:id>', archivo.obtenerArchivoM, name='v_archivoM'),
    path('get_ciclos/', archivo.get_ciclos, name='get_ciclos'),
    path('get_materias/', archivo.get_materias, name='get_materias'),
]   

