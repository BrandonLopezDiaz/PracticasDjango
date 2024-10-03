from django.contrib import admin
from documento.models import Documento

# Register your models here.
@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['id', 'descripcion']