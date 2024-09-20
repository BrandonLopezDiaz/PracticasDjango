from django.db import models

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    orden = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    #Forma de subir archivos
    # archivo = models.FileField(upload_to="uploads/")
