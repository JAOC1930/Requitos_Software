from django.db import models
from accounts.models import User
from datetime import datetime

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
            return "%s" % (self.nombre)    

class Ciclo(models.Model):
    numCiclo = models.IntegerField()
    def __str__(self):
            return "%s" % (self.numCiclo)  

class CarreraCiclo(models.Model):
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="carrera_c")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="ciclo_m") 
    class Meta:
        unique_together = ['carrera', 'ciclo']
    
    def __str__(self):
            return "%s %s" % (self.carrera,
                    self.ciclo)



class Materia(models.Model):
    nombre = models.CharField(max_length=50)
    numCreditos = models.IntegerField()
    numHoras = models.IntegerField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="materia_carrera")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="materia_ciclo")

    def __str__(self) :
        return "%s" % (self.nombre)

class Asignacion(models.Model):

    nombre = models.CharField(max_length=30)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, related_name="asignacion_carrera")
    ciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE, related_name="asignacion_ciclo")
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name="asignacion_materia")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_asignacion")
    fecha_inicial = models.DateTimeField()
    fecha_final = models.DateTimeField()
    descripcion = models.CharField(max_length= 200)

    def __str__(self):
            return "%s %s %s %s %s" % (self.nombre,
                    self.carrera, self.ciclo, self.materia, self.user)
    

class Archivos(models.Model):
    
    archivo = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_archivo")
    fecha_subida = models.DateTimeField(auto_now_add=True)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='archivo_materia', null=True)
    asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE, related_name='archivo_asignacion')
    def __str__(self):
            return "%s %s %s" % (self.archivo,
                    self.user,
                    self.fecha_subida)
    
