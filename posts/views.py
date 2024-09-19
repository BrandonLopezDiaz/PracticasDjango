from django.shortcuts import render
from django.http import  HttpResponse
from django.views.generic.base import View

class HelloWorld(View):
    def get(self, request):
        mi_Persona = {
            'name':'Brandon Lopez Diaz',
            'edad': 20,
            'codes': ['python', 'C#', 'Tyscript', 'javascript']
        }

        return render(request, 'hola.html',context= mi_Persona)
# Create your views here.
