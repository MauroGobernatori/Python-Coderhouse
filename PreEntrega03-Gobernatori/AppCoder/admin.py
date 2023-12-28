from django.contrib import admin

# Register your models here.
from AppCoder.models import (
    Profesor,
    Curso,
    Estudiante,
    Examen,
)

admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Examen)