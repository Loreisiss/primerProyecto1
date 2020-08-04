from django.shortcuts import render
from .models import Estudiante, Profesor # si queremos importar todo  usamos *
from django.http import HttpResponse, HttpResponseRedirect



def pagina_principal(request):
    return render(request, "login_registro.html")



def registro_estudiante(request):
    estudiante = Estudiante()
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    estudiante.Nombre_y_apellido = nombre+" "+apellido
    estudiante.sexo = request.POST.get('genero')
    estudiante.correo = request.POST.get('correo')
    estudiante.cedula = request.POST.get('cedula')
    estudiante.Carrera = request.POST.get('carrera')
    estudiante.contraseña = request.POST.get('password')
    estudiante.Promedio = 0.00
    estudiante.save()
    return HttpResponseRedirect('/pagina_principal/')




def registro_profesor(request):
    profesor = Profesor()
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    profesor.Nombre_y_apellido = nombre+" "+apellido
    profesor.sexo = request.POST.get('genero')
    profesor.correo = request.POST.get('correo')
    profesor.cedula = request.POST.get('cedula')
    profesor.Asignatura = request.POST.get('asignatura')
    profesor.contraseña = request.POST.get('password')
    profesor.save()
    return HttpResponseRedirect('/pagina_principal/')



aux = profesor = estudiante = None
#proceso de autenticacion, username y contraseña
def login(request):
    global aux; global profesor; global estudiante

    if request.GET["Cedula"]:
        cedula_solicitada =  request.GET["Cedula"]
        try:
            profesor = Profesor.objects.get(cedula = cedula_solicitada)
            aux = True
            if request.GET["pwd"]:
                password_escrita = request.GET["pwd"]
                if profesor.contraseña == password_escrita: 
                    return HttpResponseRedirect("/perfil_ingresado/")
        except:
            try:
                estudiante = Estudiante.objects.get(cedula = cedula_solicitada)
                aux = False
                if request.GET["pwd"]:
                    password_escrita = request.GET["pwd"]
                    if estudiante.contraseña == password_escrita:
                        return HttpResponseRedirect("/perfil_ingresado/")
            except: pass
        return HttpResponse("Cedula o contraseña invalida")
        

  

#vista que se ejecuta cuando el usuario accede al sistema

def perfil_ingresado(request):
    if aux:
        return render(request, "perfil_profesor.html", {"persona": profesor})
    else:

        examen1_hecho =  estudiante.tiempo_examen1 == None
        examen2_hecho =  estudiante.tiempo_examen2 == None
        examen3_hecho =  estudiante.tiempo_examen3 == None

        return render(request, "perfil_estudiante.html", 
        {
        "persona": estudiante, 
        "examen1_realizado": examen1_hecho,
        "examen2_realizado": examen2_hecho, 
        "examen3_realizado": examen3_hecho
        })




def examen1(request):
    return render(request, "test.html")



#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def examen1_post(request):

    global estudiante

    if request.method == 'POST':
        if 'puntos' in request.POST:
            print("exito")

            estudiante.nota_examen1 = request.POST['puntos']
            estudiante.save()
          
        if 'tiempo' in request.POST:
            print("exito")

            estudiante.tiempo_examen1 = request.POST['tiempo']
            estudiante.save()
                 
        return HttpResponse('success') 
         
    return HttpResponse('FAIL!!!!!')
