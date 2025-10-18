from django.contrib import admin
from .models import *

modelos = [Estudiante, Docente, Asignatura]

for modelo in modelos:
    admin.site.register(modelo)




# Register your models here.
