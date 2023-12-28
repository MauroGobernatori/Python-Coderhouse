from django.shortcuts import render
# from django.http import HttpResponse
# from django.template import Template, Context, loader

from AppCoder.models import Curso, Profesor, Estudiante, Examen
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, ExamenFormulario

# Create your views here.
def inicio(request):
    if request.method == 'GET':
        comision = request.GET.get('comision')

        if comision is None:
            return render(request, 'inicio.html')
        
        cursos = Curso.objects.filter(comision__icontains=comision)
        # cursos = Curso.objects.filter(comision__gte=comision)

        contexto = {
            'cursos': cursos,
            'comision': comision
        }

        return render(request, 'inicio.html', contexto)
        
    return render(request, 'inicio.html')

def cursos(request):
    if request.method == 'POST':
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data

            nombre = datos.get('curso')
            comision = datos.get('comision')

            curso = Curso(nombre=nombre, comision=comision)

            curso.save()

            return render(request, 'cursos.html', {'formulario': CursoFormulario()})
        
    else:
        formulario = CursoFormulario()

    return render(request, 'cursos.html', { "formulario": formulario })

def profesores(request):
    if request.method == 'POST':
        formulario = ProfesorFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data

            nombre = datos.get('nombre')
            apellido = datos.get('apellido')
            email = datos.get('email')

            profesor = Profesor(nombre=nombre, apellido=apellido, email=email)

            profesor.save()

            return render(request, 'profesores.html', {'formulario': ProfesorFormulario()})
        
    else:
        formulario = ProfesorFormulario()

    return render(request, 'profesores.html', { "formulario": formulario })

def estudiantes(request):
    if request.method == 'POST':
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data

            nombre = datos.get('nombre')
            apellido = datos.get('apellido')
            email = datos.get('email')

            estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email)

            estudiante.save()

            return render(request, 'estudiantes.html', {'formulario': EstudianteFormulario()})
        
    else:
        formulario = EstudianteFormulario()

    return render(request, 'estudiantes.html', { "formulario": formulario })

def examenes(request):
    if request.method == 'POST':
        formulario = ExamenFormulario(request.POST)

        if formulario.is_valid():
            datos = formulario.cleaned_data

            nombre = datos.get('nombre')
            fecha = datos.get('fecha')
            nota = datos.get('nota')

            examen = Examen(nombre=nombre, fecha=fecha, nota=nota)

            examen.save()

            return render(request, 'examenes.html', {'formulario': ExamenFormulario()})
        
    else:
        formulario = ExamenFormulario()

    return render(request, 'examenes.html', { "formulario": formulario })