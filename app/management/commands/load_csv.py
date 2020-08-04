from django.core.management import BaseCommand
from csv import DictReader
from app.models import Profesor, Estudiante

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        for fila in DictReader(open('listado_Profesores.csv')):
            prof = Profesor()
            prof.Nombre_y_apellido = fila['Nombre y Apellido']
            prof.Asignatura = fila['Asignatura']
            prof.tiempo_exp = fila['Experiencia (años)']
            prof.trayectoria_resumen= fila['Resumen']
            prof.correo = fila["Correo"]
            prof.cedula = fila["Cedula"]
            prof.sexo = fila["Sexo"]
            prof.contraseña = fila["Contraseña"]
            prof.save()

        for fila in DictReader(open('listado_Estudiantes.csv')):
            es = Estudiante()
            es.Nombre_y_apellido = fila['Nombre y Apellido']
            es.Carrera = fila['Carrera']
            es.Promedio= fila['Promedio']
            es.Semestres_cursados= fila['Semestres cursados']
            es.correo = fila["Correo"]
            es.cedula = fila["Cedula"]
            es.sexo = fila["Sexo"]
            es.contraseña = fila["Contraseña"]
            es.save()
