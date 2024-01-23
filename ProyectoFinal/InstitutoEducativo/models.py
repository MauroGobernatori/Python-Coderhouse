from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()
    legajo = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Profesores'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Curso(models.Model):
    nombre = models.CharField(max_length=25)
    comision = models.IntegerField()
    profesor = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = 'Cursos'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} -- {self.comision}'
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    email = models.EmailField()
    fecha_nac = models.DateField()
    legajo = models.IntegerField()
    cursos = models.ManyToManyField(Curso, through='Curso_Estudiante', default=None)

    class Meta:
        verbose_name_plural = 'Estudiantes'
        ordering = ['legajo']

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
class Curso_Estudiante(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

class Examen(models.Model):
    nombre = models.CharField(max_length=30)
    fecha = models.DateField()
    nota = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, default=None)

    class Meta:
        verbose_name_plural = 'Examenes'
        ordering = ['fecha']

    def __str__(self):
        return f'{self.fecha} -- {self.curso}, {self.estudiante} - {self.nombre}'