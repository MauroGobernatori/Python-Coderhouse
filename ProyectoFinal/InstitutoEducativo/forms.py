from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from InstitutoEducativo.models import Profesor, Curso, Estudiante

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2", "last_name", "first_name"]

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=25)
    comision = forms.IntegerField()
    profesor = forms.ModelChoiceField(queryset=Profesor.objects.all(), required=False)

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    email = forms.EmailField()
    legajo = forms.IntegerField()

class ExamenFormulario(forms.Form):
    nombre = forms.CharField()
    fecha = forms.DateField()
    nota = forms.IntegerField()
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())
    estudiante = forms.ModelChoiceField(queryset=Estudiante.objects.all())

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    email = forms.EmailField()
    fecha_nac = forms.DateField()
    legajo = forms.IntegerField()
    curso = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple,queryset=Curso.objects.all())

