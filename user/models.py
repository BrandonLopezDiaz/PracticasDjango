from django.db import models
from acceso.models import acceso
# Create your models here.
class User (models.Model):
    accesos = models.ManyToManyField(acceso, related_name= "acceso_list", blank=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)