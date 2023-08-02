from django.forms import ModelForm, DateInput
from calendarapp.models import Event, EventMember
from django import forms
from calendarapp.models.archivos import *

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ["title", "description", "start_time", "end_time"]
        # datetime-local is a HTML5 input type
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter event title"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter event description",
                }
            ),
            "start_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_time": DateInput(
                attrs={"type": "datetime-local", "class": "form-control"},
                format="%Y-%m-%dT%H:%M",
            ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["start_time"].input_formats = ("%Y-%m-%dT%H:%M",)
        self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


class AddMemberForm(forms.ModelForm):
    class Meta:
        model = EventMember
        fields = ["user"]


class ArchivoForm(forms.ModelForm):
    def __init__(self, user=None, *args, **kwargs):
        super(ArchivoForm, self).__init__(*args, **kwargs)
        self.fields['materia'].queryset = Materia.objects.filter(asignacion_materia__user=user)
    
    # Agregar campo de asignación al formulario
    asignacion = forms.ModelChoiceField(queryset=Asignacion.objects.all(), label='Asignación')

    class Meta:
        model = Archivos
        fields = ['materia', 'asignacion', 'archivo']


class AsignacionForm(forms.ModelForm):
    fecha_inicial = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'],
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"},
            format="%Y-%m-%dT%H:%M:%S",
        )
    )
    fecha_final = forms.DateTimeField(
        input_formats=['%Y-%m-%d %H:%M:%S'],
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"},
            format="%Y-%m-%dT%H:%M:%S",
        )
    )

    class Meta:
        model = Asignacion
        fields = ['nombre', 'carrera', 'ciclo', 'materia', 'user', 'fecha_inicial', 'fecha_final', 'descripcion']

    def __init__(self, *args, **kwargs):
        super(AsignacionForm, self).__init__(*args, **kwargs)
        self.fields["fecha_inicial"].input_formats = ("%Y-%m-%d %H:%M:%S",)
        self.fields["fecha_final"].input_formats = ("%Y-%m-%d %H:%M:%S",)
