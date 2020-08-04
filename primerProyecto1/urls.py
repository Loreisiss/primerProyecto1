from django.contrib import admin
from django.urls import path
from app.views import * # importar vistas

urlpatterns = [
    path('pagina_principal/', pagina_principal),
    path('registro_estudiante/', registro_estudiante),
    path('registro_profesor/', registro_profesor),
    path("perfil_ingresado/", perfil_ingresado),
    path('examen1/', examen1, name="test1"),
    path('enviar_info/', examen1_post),
    path('login/',login),
    path('admin/', admin.site.urls),
]
