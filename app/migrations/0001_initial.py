# Generated by Django 3.0.2 on 2020-04-16 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_y_apellido', models.CharField(max_length=100)),
                ('cedula', models.IntegerField(default='0')),
                ('correo', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('Carrera', models.CharField(max_length=60)),
                ('Promedio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('Semestres_cursados', models.IntegerField(default='0')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_y_apellido', models.CharField(max_length=100)),
                ('cedula', models.IntegerField(default='0')),
                ('correo', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=1)),
                ('Asignatura', models.CharField(max_length=60)),
                ('tiempo_exp', models.IntegerField(default='0')),
                ('trayectoria_resumen', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
