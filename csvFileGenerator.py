import csv
from random import randint

def password_generator():
    x = "abcdfghijklmnopqrstvwxyzABCDFGHIJKLMNOPQRSTVWXYZ123456789%!#{[}].;"
    string = ""
    for i in range(8):
        string += x[randint(0,len(x)-1)]
    return string


genero = None
def gender(indice):

    global genero

    if indice in [0,1,2,4,5,8,9,14,15,16]:
        genero = 1
    else:
        genero = 0
    return indice

sexo = ['M','F']


nombres=["Isabel","Camila","Natacha","Jose","Angela","Andreina",'Richard',"Miguel","Mary","Vanessa","Carlos","Diego","David","Daniel","Carolina",'Adriana','Alissa']
apellidos = ["Hernandez","Perez","Tovar","Ortega","Gutierrez","Gonzalez","Diaz","Rangel","Sosa",'Smith','Johnson','Brown','Lowell','Gibss','Aldrich']


with open('listado_Profesores.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Nombre y Apellido','Asignatura','Experiencia (años)', 'Resumen', 'Correo', 'Cedula','Sexo','Contraseña'])

    
    asignatura = ['Matematica 1', 'Matematica 2', 'Matematica 3', "Fisica 2", "Quimica 1", 
    "Quimica 2", "Quimica 3", "Fisica 3","Fisica 1", "Introduccion a la filosofia occidental","Programacion 1","Psicologia General 1",
    "Geografia", "Fisiologia Vegetal","Estudio de suelos volcanicos","Gramatica Castellana 1"]
    tiempo = [5,7,8,12,5,10,11,12,17,13,8,9]
    resumen = ["Ha sido profesor en MIT, Oxford y UCV",
    "Tuvo un doctorado en Harvard a la edad de 30 años, ha hecho trabajos investigacion en su area de conocimiento por 7 años",
    "Ha dado clase en 8 universidades distintas en todo el Reino Unido",
    "Magister Scientiarum en varias del conocimiento, entre ellas, Biologia marina y Geografia"]
    


    for i in range(30):
        name = nombres[gender(randint(0,len(nombres)-1))]+" "+apellidos[randint(0,len(apellidos)-1)]
        thewriter.writerow([
        name,
        asignatura[randint(0,len(asignatura)-1)],
        tiempo[randint(0,len(tiempo)-1)],
        resumen[randint(0,len(resumen)-1)],
        name.lower().replace(' ', '')+"@ejemplo.com",
        randint(18000000,26000000),
        sexo[ genero  ],
        password_generator()
         ])

with open('listado_Estudiantes.csv', 'w', newline='') as f:
    thewriter = csv.writer(f)
    thewriter.writerow(['Nombre y Apellido','Carrera','Promedio', 'Semestres cursados', 'Correo','Cedula','Sexo',"Contraseña"  ])

    carrera = ['Letras','Ingenieria Geologica','Ingenieria Electrica', 'Licenciatura en Artes', 'Licenciatura en Matematicas','Licenciatura en Biologia',
    'Ingenieria Mecanica']
    promedio = [15.23,17.81,8.93,12.97,14.89,10.51,11.29,16.61,17.54,13.81,18.22,9.34]
    
    


    for i in range(60):
     
        name = nombres[gender(randint(0,len(nombres)-1))]+" "+apellidos[randint(0,len(apellidos)-1)]
        thewriter.writerow([
        name,
        carrera[randint(0,len(carrera)-1)],
        promedio[randint(0,len(promedio)-1)],
        randint(1,7),
        name.lower().replace(' ', '')+"@ejemplo.com",
        randint(18000000,26000000),
        sexo[ genero ],
        password_generator()
         ])