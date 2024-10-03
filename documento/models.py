from django.db import models


class Documento(models.Model):
    videos = models.FileField(upload_to='uploads/')
    pdf = models.FileField(upload_to='uploads/')
    descripcion = models.CharField(max_length=255)