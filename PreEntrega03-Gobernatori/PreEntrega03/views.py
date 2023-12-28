from django.http import HttpResponse
from django.template import Template, Context, loader

def inicio(request):
    mi_html = loader.get_template('inicio.html')

    contexto = {}

    documento = mi_html.render(contexto)

    return HttpResponse(documento)

def profesores(request):
    return

def estudiantes(request):
    return

def cursos(request):
    return

def examenes(request):
    return