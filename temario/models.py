from django.db import models

class Temas (models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    video_url = models.CharField(max_length=255)
    imagen_url = models.CharField(max_length=500)
    def __str__(self):
        return self.titulo

class SubTemas (Temas):
    tema = models.ForeignKey(Temas, on_delete=models.CASCADE, related_name='subtemas_relacion')