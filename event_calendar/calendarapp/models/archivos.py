from django.db import models
from accounts.models import User

class Archivos(models.Model):
    
    archivo = models.FileField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_archivo")
    fecha_subida = models.DateTimeField(auto_now_add=True)

