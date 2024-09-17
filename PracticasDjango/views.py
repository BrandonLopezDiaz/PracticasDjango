from django.http import  HttpResponse

def saludo(request):
    return HttpResponse("Hola este es mi  primer proyecto django")