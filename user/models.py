from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=255)
    age = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)