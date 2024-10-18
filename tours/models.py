from django.db import models
from acceso.models import acceso

class Tour (models.Model):
    titulo_tour = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255)
    estatus = models.BooleanField(default=True)
    acceso = models.ForeignKey(acceso, on_delete=models.CASCADE, related_name='accesos_relacionados')
    def __str__(self):
        return self.titulo
