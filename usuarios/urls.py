from django.urls import path
from usuarios.views import *

urlpatterns = [
    path('', renderizar_index, name="index"),
    path("test/", testing, name="test"),
    path("RegistroEstudiantes/", estudiante_registro, name="estudianteregistro"),
    path("RegistroDocente/", docente_registro, name="docenteregistro")
]