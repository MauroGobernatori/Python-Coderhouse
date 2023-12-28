from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)

class Curso(models.Model):
    nombre = models.CharField(max_length=25)

class Examen(models.Model):
    nombre = models.CharField(max_length=30)