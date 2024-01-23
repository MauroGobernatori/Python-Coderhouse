from django.contrib import admin

# Register your models here.
from InstitutoEducativo.models import (
    Profesor,
    Curso,
    Estudiante,
    Examen,
    Curso_Estudiante
)

admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Examen)
admin.site.register(Curso_Estudiante)