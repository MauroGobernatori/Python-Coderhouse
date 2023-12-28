from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField(default=None)

    class Meta:
        verbose_name_plural = 'Profesores'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField(default=None)

    def __str__(self):
        return f'{self.nombre}, {self.apellido}'

class Curso(models.Model):
    nombre = models.CharField(max_length=25)
    comision = models.IntegerField(default=None)

    def __str__(self):
        return f'{self.nombre} -- {self.comision}'

class Examen(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField(default=None)
    nota = models.IntegerField(default=None)

    class Meta:
        verbose_name_plural = 'Examenes'
        ordering = ['fecha']

    def __str__(self):
        return f'{self.fecha} -- {self.nombre}'