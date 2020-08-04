from django.db import models

GENERO = [('M','Masculino'),('F','Femenino')]


class modelo_evaluacion(models.Model):

    nota_examen1 = models.IntegerField(null=True)
    nota_examen2 = models.IntegerField(null=True)
    nota_examen3 = models.IntegerField(null=True)
    tiempo_examen1 = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    tiempo_examen2 = models.DecimalField(null=True, decimal_places=2, max_digits=4)
    tiempo_examen3 = models.DecimalField(null=True, decimal_places=2, max_digits=4)

    class Meta:
        abstract = True


class persona(models.Model):
    Nombre_y_apellido = models.CharField(max_length=100)
    cedula = models.IntegerField(default='0')
    correo = models.EmailField()
    sexo = models.CharField(choices=GENERO, max_length=1)
    contraseña = models.CharField(max_length=8)

    class Meta:
        abstract = True


class Profesor(persona):

    Asignatura = models.CharField(max_length=60)
    tiempo_exp = models.IntegerField(default='0')
    trayectoria_resumen = models.TextField(blank=True)


class Estudiante(persona, modelo_evaluacion):

    Carrera = models.CharField(max_length=60)
    Promedio = models.DecimalField(decimal_places=2, max_digits=4)
    Semestres_cursados = models.IntegerField(default='0')
   
   