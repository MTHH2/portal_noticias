
from django.shortcuts import render
from .models import Noticia


def inicio(request):
    #Consultamos la base de datos:
    noticias = Noticia.objects.all().order_by('-fecha_ocurrencia')
    #Enviamos los datos a HTML:
    return render(
        request,
        'noticias/inicio.html',
        {'noticias': noticias}
    )

noticias = Noticia.objects.all().order_by('-fecha_ocurrencia')



#- objects: administrador de consultas del modelo.
#- all(): obtiene todas las noticias.
#- order_by(): organiza los resultados.
#- -fecha_ocurrencia: orden descendente.