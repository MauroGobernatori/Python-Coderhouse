from django.urls import path

from InstitutoEducativo.views import (
    index,
    cursos,
    estudiantes,
    profesores,
    examenes,
    about,
    login_request,
    register_request,
    editar_curso,
    eliminar_curso,
    editar_profesor,
    eliminar_profesor,
    editar_examen,
    eliminar_examen,
    editar_estudiante,
    eliminar_estudiante
    )

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('cursos/', cursos, name='cursos'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('profesores/', profesores, name='profesores'),
    path('examenes/', examenes, name='examenes'),
    path('about', about, name='about'),
    path('login/', login_request, name='login'),
    path('register/', register_request, name='register'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar_curso/<id_curso>', editar_curso, name='editar_curso'),
    path('eliminar_curso/<id_curso>', eliminar_curso, name='eliminar_curso'),
    path('editar_profesor/<id_profesor>', editar_profesor, name='editar_profesor'),
    path('eliminar_profesor/<id_profesor>', eliminar_profesor, name='eliminar_profesor'),
    path('editar_examen/<id_examen>', editar_examen, name='editar_examen'),
    path('eliminar_examen/<id_examen>', eliminar_examen, name='eliminar_examen'),
    path('editar_estudiante/<id_estudiante>', editar_estudiante, name='editar_estudiante'),
    path('eliminar_estudiante/<id_estudiante>', eliminar_estudiante, name='eliminar_estudiante')
]