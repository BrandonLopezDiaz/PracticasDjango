from django.contrib import admin
from .models import Temas, SubTemas

# Register your models here.
@admin.register(Temas)
class TemasAdmin(admin.ModelAdmin):
    list_display = ['id','titulo',]

@admin.register(SubTemas)
class SubTemasAdmin(admin.ModelAdmin):
    list_display = ['id','titulo',]
