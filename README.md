# Python-Coderhouse

# Proyecto Final

El proyecto final consta de un sistema de un Instituto Educativo. Tiene 4 modelos, Cursos, Profesores, Estudiantes y Exámenes.  

Cada Curso tiene un Profesor y puede tener varios Estudiantes, y cada Exámen pertenece a un Curso y Estudiante.  

El sistema puede realizar un CRUD de cada modelo.  

Cuenta de una barra de navegación en donde se puede circular por las diferentes páginas. Cada modelo tiene su propia página, y adicionalmente hay una página de inicio y una de about.  

Hay un template padre (main.html) del cual heredan otro templates.  

La página principal una vez dado de alta el servidor con el comando 'python manage.py runserver' es 'localhost:8000/instituto'.  

El sistema cuenta con un sistema de Login y Registro, por lo que se debe iniciar sesión para entrar al sistema. Se puede iniciar sesión desde la url 'localhost:8000/instituto/login' y registrarse desde 'localhost:8000/instituto/register'