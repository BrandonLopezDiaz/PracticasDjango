from django.contrib import admin
from acceso.models import acceso

@admin.register(acceso)
class accesoAdmin(admin.ModelAdmin):
    list_display = ['title' ,'acceso']
