from django import forms

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    email = forms.EmailField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=25)
    apellido = forms.CharField(max_length=25)
    email = forms.EmailField()

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=25)
    comision = forms.IntegerField()

class ExamenFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha = forms.DateField()
    nota = forms.IntegerField()
