from django.shortcuts import render

from InstitutoEducativo.models import Curso, Profesor, Estudiante, Examen, Curso_Estudiante
from InstitutoEducativo.forms import UserRegistrationForm, CursoFormulario, ProfesorFormulario, EstudianteFormulario, ExamenFormulario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='login/')
def index(request):

    return render(request, 'index.html')

@login_required(login_url='login/')
def cursos(request):

    if request.method == 'POST':
        form = CursoFormulario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            nombre = datos.get('nombre')
            comision = datos.get('comision')

            curso = Curso(nombre=nombre, comision=comision)
            curso.save()

    cursos = Curso.objects.all().order_by('nombre')

    contexto = {
        'cursos': cursos,
        'form': CursoFormulario()
    }

    return render(request, 'cursos.html', contexto)

@login_required(login_url='login/')
def estudiantes(request):

    if request.method == 'POST':
        form = EstudianteFormulario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            nombre = datos.get('nombre')
            apellido = datos.get('apellido')
            email = datos.get('email')
            fecha_nac = datos.get('fecha_nac')
            legajo = datos.get('legajo')
            cursoSet = datos.get('curso')

            estudiante = Estudiante(nombre=nombre, apellido=apellido, email=email, fecha_nac=fecha_nac, legajo=legajo)
            estudiante.save()

            for curso in cursoSet:
                curso_estudiante = Curso_Estudiante(curso=curso, estudiante=estudiante)
                curso_estudiante.save()

    estudiantes = Estudiante.objects.all().values().order_by('legajo')

    for estudiante in estudiantes:
        cursos_estudiantes = Curso_Estudiante.objects.filter(estudiante=estudiante['id']).values()

        estudiante_curso = []

        if cursos_estudiantes:

            for curso_estudiante in cursos_estudiantes:

                cursos = Curso.objects.filter(id=curso_estudiante['curso_id']).values()
                estudiante_curso.append(cursos)
            
        estudiante['cursos'] = estudiante_curso

    contexto = {
        'estudiantes': estudiantes,
        'form': EstudianteFormulario()
    }

    return render(request, 'estudiantes.html', contexto)

@login_required(login_url='login/')
def profesores(request):

    if request.method == 'POST':
        form = ProfesorFormulario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            nombre = datos.get('nombre')
            apellido = datos.get('apellido')
            email = datos.get('email')
            legajo = datos.get('legajo')

            profesor = Profesor(nombre=nombre, apellido=apellido, email=email, legajo=legajo)
            profesor.save()

    profesores = Profesor.objects.all().order_by('legajo')

    contexto = {
        'profesores': profesores,
        'form': ProfesorFormulario()
    }

    return render(request, 'profesores.html', contexto)

@login_required(login_url='login/')
def examenes(request):

    if request.method == 'POST':
        form = ExamenFormulario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            nombre = datos.get('nombre')
            fecha = datos.get('fecha')
            nota = datos.get('nota')
            curso = datos.get('curso')
            estudiante = datos.get('estudiante')

            examen = Examen(nombre=nombre, fecha=fecha, nota=nota, curso=curso, estudiante=estudiante)
            examen.save()

    examenes = Examen.objects.all().order_by('fecha')

    contexto = {
        'examenes': examenes,
        'form': ExamenFormulario()
    }

    return render(request, 'examenes.html', contexto)

def login_request(request):

    if request.method == 'POST':
        
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)

                return render(request, 'index.html', {'mensaje': f'Bienvenido {username}'})
            else:
                return render(request, 'index.html', {'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'index.html', {'mensaje': 'Datos del formulario incorrectos'})

    form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def register_request(request):

    if request.method == 'POST':

        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')

            form.save()

            return render(request, 'login.html', { 'mensaje': f'Se registró a {username}'})

    form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def editar_curso(request, id_curso):
    
    curso = Curso.objects.get(id=id_curso)

    if request.method == 'POST':

        form = CursoFormulario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            curso.nombre = datos.get('nombre')
            curso.comision = datos.get('comision')
            curso.profesor = datos.get('profesor')

            curso.save()

            cursos = Curso.objects.all().order_by('nombre')

            contexto = {
                'cursos': cursos,
                'form': CursoFormulario()
            }

            return render(request, 'cursos.html', contexto)
        
    form = CursoFormulario(initial={'nombre': curso.nombre, 'comision': curso.comision, 'profesor': curso.profesor})

    return render(request, 'editar_curso.html', {'form': form, 'id_curso': id_curso})

def eliminar_curso(request, id_curso):
    
    curso = Curso.objects.get(id=id_curso)

    curso.delete()

    cursos = Curso.objects.all().order_by('nombre')

    contexto = {
        'cursos': cursos,
        'form': CursoFormulario()
    }

    return render(request, 'cursos.html', contexto)

def editar_profesor(request, id_profesor):
    
    profesor = Profesor.objects.get(id=id_profesor)

    if request.method == 'POST':

        form = ProfesorFormulario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            profesor.nombre = datos.get('nombre')
            profesor.apellido = datos.get('apellido')
            profesor.email = datos.get('email')
            profesor.legajo = datos.get('legajo')

            profesor.save()

            profesores = Profesor.objects.all().order_by('legajo')

            contexto = {
                'profesores': profesores,
                'form': ProfesorFormulario()
            }

            return render(request, 'profesores.html', contexto)
        
    form = ProfesorFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'legajo': profesor.legajo})

    return render(request, 'editar_profesor.html', {'form': form, 'id_profesor': id_profesor})

def eliminar_profesor(request, id_profesor):
    
    profesor = Profesor.objects.get(id=id_profesor)

    profesor.delete()

    profesores = Profesor.objects.all().order_by('legajo')

    contexto = {
        'profesores': profesores,
        'form': ProfesorFormulario()
    }

    return render(request, 'profesores.html', contexto)

def editar_examen(request, id_examen):

    examen = Examen.objects.get(id=id_examen)

    if request.method == 'POST':

        form = ExamenFormulario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            examen.nombre = datos.get('nombre')
            examen.fecha = datos.get('fecha')
            examen.nota = datos.get('nota')
            examen.curso = datos.get('curso')
            examen.estudiante = datos.get('estudiante')

            examen.save()

            examenes = Examen.objects.all().order_by('fecha')

            contexto = {
                'examenes': examenes,
                'form': ExamenFormulario()
            }

            return render(request, 'examenes.html', contexto)

    form = ExamenFormulario(initial={'nombre': examen.nombre, 'fecha': examen.fecha, 'nota': examen.nota, 'curso': examen.curso, 'estudiante': examen.estudiante})

    return render(request, 'editar_examen.html', {'form': form, 'id_examen': id_examen})

def eliminar_examen(request, id_examen):

    examen = Examen.objects.get(id=id_examen)

    examen.delete()

    examenes = Examen.objects.all().order_by('fecha')

    contexto = {
        'examenes': examenes,
        'form': ExamenFormulario()
    }

    return render(request, 'examenes.html', contexto)

def editar_estudiante(request, id_estudiante):
    
    estudiante = Estudiante.objects.get(id=id_estudiante)

    if request.method == 'POST':

        form = EstudianteFormulario(request.POST)

        if form.is_valid():
            datos = form.cleaned_data

            estudiante.nombre = datos.get('nombre')
            estudiante.apellido = datos.get('apellido')
            estudiante.email = datos.get('email')
            estudiante.fecha_nac = datos.get('fecha_nac')
            estudiante.legajo = datos.get('legajo')

            estudiante.save()

            cursoSet = datos.get('curso')
            curso_est_set = Curso_Estudiante.objects.filter(estudiante=id_estudiante).values()

            cursos_id_old = [] # Guarda el id de los cursos que tiene el estudiante
            cursos_id_to_keep = [] # Va a guardar el id de los cursos que va a tener el estudiante

            for curso_est in curso_est_set:
                cursos_id_old.append(curso_est['curso_id'])

            for curso in cursoSet:
                cursos_id_to_keep.append(curso.id)

                if not Curso_Estudiante.objects.filter(estudiante=id_estudiante,curso=curso.id).exists():
                    curso_est_add = Curso_Estudiante(curso=curso, estudiante=estudiante)
                    curso_est_add.save()

            cursos_id_to_delete = list(set(cursos_id_old) - set(cursos_id_to_keep)) # Consigue los cursos que tenía el estudiante pero ya no tiene más, osea que deben ser eliminados
            for curso_id in cursos_id_to_delete:
                curso_estudiante_to_delete = Curso_Estudiante.objects.get(curso=curso_id,estudiante=id_estudiante)
                curso_estudiante_to_delete.delete()

            ########################################################
            estudiantes = Estudiante.objects.all().values().order_by('legajo')
            
            for estudiante in estudiantes:
                cursos_estudiantes = Curso_Estudiante.objects.filter(estudiante=estudiante['id']).values()

                estudiante_curso = []

                if cursos_estudiantes:

                    for curso_estudiante in cursos_estudiantes:

                        cursos = Curso.objects.filter(id=curso_estudiante['curso_id']).values()
                        estudiante_curso.append(cursos)
                    
                estudiante['cursos'] = estudiante_curso

            contexto = {
                'estudiantes': estudiantes,
                'form': EstudianteFormulario()
            }

            return render(request, 'estudiantes.html', contexto)
            ########################################################

    form = EstudianteFormulario(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email, 'fecha_nac': estudiante.fecha_nac, 'legajo': estudiante.legajo})

    return render(request, 'editar_estudiante.html', {'form': form, 'id_estudiante': id_estudiante})

def eliminar_estudiante(request, id_estudiante):
    
    estudiante = Estudiante.objects.get(id=id_estudiante)

    estudiante.delete()

    estudiantes = Estudiante.objects.all().values().order_by('legajo')

    for estudiante in estudiantes:
        cursos_estudiantes = Curso_Estudiante.objects.filter(estudiante=estudiante['id']).values()

        estudiante_curso = []

        if cursos_estudiantes:

            for curso_estudiante in cursos_estudiantes:

                cursos = Curso.objects.filter(id=curso_estudiante['curso_id']).values()
                estudiante_curso.append(cursos)
            
        estudiante['cursos'] = estudiante_curso

    contexto = {
        'estudiantes': estudiantes,
        'form': EstudianteFormulario()
    }

    return render(request, 'estudiantes.html', contexto)

@login_required(login_url='login/')
def about(request):

    return render(request, 'about.html')