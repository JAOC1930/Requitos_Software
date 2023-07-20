from django.db import models
from accounts.models import User

class Archivos(models.Model):
    
    archivo = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_archivo")
    fecha_subida = models.DateTimeField(auto_now_add=True)



class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    

class Ciclo(models.Model):
    numCiclo = models.IntegerField()


class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    numCreditos = models.IntegerField()
    numHoras = models.IntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="materia_carrera")

class CarreraCiclo(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="carrera_c")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="ciclo_m") 


class Asignacion(models.Model):

    nombre = models.CharField(max_length=30)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="asignacion_carrera")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="asignacion_ciclo")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="asignacion_materia")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_asignacion")

    def __str__(self):
        return self.nombre
    