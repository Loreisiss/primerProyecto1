from django.contrib import admin
from .models import Profesor, Estudiante



@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display= ['Nombre_y_apellido']

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['Nombre_y_apellido','Semestres_cursados']