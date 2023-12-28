from django.urls import path

from AppCoder.views import inicio, cursos, profesores, estudiantes, examenes

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('profesores/', profesores, name='profesores'),
    path('estudiantes/', estudiantes, name='estudiantes'),
    path('examenes/', examenes, name='examenes'),
]