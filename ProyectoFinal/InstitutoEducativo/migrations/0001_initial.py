# Generated by Django 5.0 on 2024-01-21 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('comision', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Cursos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('legajo', models.IntegerField(verbose_name=5)),
            ],
            options={
                'verbose_name_plural': 'Profesores',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Curso_Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstitutoEducativo.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('apellido', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nac', models.DateField()),
                ('legajo', models.IntegerField(verbose_name=5)),
                ('cursos', models.ManyToManyField(through='InstitutoEducativo.Curso_Estudiante', to='InstitutoEducativo.curso')),
            ],
            options={
                'verbose_name_plural': 'Estudiantes',
                'ordering': ['legajo'],
            },
        ),
        migrations.AddField(
            model_name='curso_estudiante',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstitutoEducativo.estudiante'),
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('nota', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InstitutoEducativo.curso')),
            ],
            options={
                'verbose_name_plural': 'Examenes',
                'ordering': ['fecha'],
            },
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='InstitutoEducativo.profesor'),
        ),
    ]
