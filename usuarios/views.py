from django.shortcuts import render, redirect
from datetime import datetime
from usuarios.forms import *
#from django.http import HttpResponse



# Create your views here.

def renderizar_index(request):
    return render(request, "usuarios/index.html")

#DRY - chequear si hay tiempo como simplificar esta sección


def estudiante_registro(request):
    # GET - Pedir info a la base de datos
    # POST - Solicitud para crear info / manipular datos
    
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = EstudianteForm()    
    
    
    return render(request, "usuarios/estudianteregistro.html", {'form': form})

def docente_registro(request):
    if request.method == "POST":
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = DocenteForm()    
    
    
    return render(request, "usuarios/docenteregistro.html", {'form': form})

def asignatura_registro(request):
    if request.method == "POST":
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = AsignaturaForm()    
        
    return render(request, "usuarios/asignaturaregistro.html", {'form': form})
    
 


def testing(request):
    fecha_actual = datetime(2025, 10, 17, 4, 30)
    numeros_unoaldiez = range(1, 11)
    contexto = {"fecha":fecha_actual, "numeros": numeros_unoaldiez}
    return render(request, "usuarios/test.html", contexto)