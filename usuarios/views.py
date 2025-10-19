from django.shortcuts import render
from datetime import datetime
from django.contrib import messages
from usuarios.forms import *
#from django.http import HttpResponse



# Create your views here.

def renderizar_index(request):
    return render(request, "usuarios/index.html")

#crear en el futuro funcion registrar(Clase, request?, mensaje_exito). 
#django.shortcuts -> redirect sirve para redirigir

#**********************************************************************

# direcciones de listado query

def estudiante_listado(request):
    query = request.GET.get('q', '').strip()
    mensaje = None
    if query:     #si se busca algo
        query_estudiante = Estudiante.objects.filter(apellido__icontains = query).order_by("nombre")
        #si no se encuentra la busqueda
        if not query_estudiante.exists():
            query_estudiante = Estudiante.objects.all().order_by("apellido")
            mensaje = "No se encontraron estudiantes con ese apellido, mostrando todos los resultados"
    else: 
        # Si no hay búsqueda, no mostrar nada (tabla no aparece)
        query_estudiante = None
    
    contexto = {"query": query, "query_estudiante": query_estudiante, "mensaje": mensaje}
    return render(request, "usuarios/estudiantelistado.html", contexto)



# registro formularios

def estudiante_registro(request):
    # GET - Pedir info a la base de datos
    # POST - Solicitud para crear info / manipular datos
    
    if request.method == "POST":
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Estudiante registrado/a con éxito.")
            form = EstudianteForm()  # limpiar el formulario       
    else:
        form = EstudianteForm()    
    
    
    return render(request, "usuarios/estudianteregistro.html", {'form': form})

def docente_registro(request):
    if request.method == "POST":
        form = DocenteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Docente registrado/a con éxito.")
            form = DocenteForm()  # limpiar el formulario  
    else:
        form = DocenteForm()    
    
    
    return render(request, "usuarios/docenteregistro.html", {'form': form})

def asignatura_registro(request):
    if request.method == "POST":
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Asignatura registrada con éxito.")
            form = AsignaturaForm()  # limpiar el formulario
    else:
        form = AsignaturaForm()    
        
    return render(request, "usuarios/asignaturaregistro.html", {'form': form})
    
 
# testing

def testing(request):
    fecha_actual = datetime(2025, 10, 17, 4, 30)
    numeros_unoaldiez = range(1, 11)
    contexto = {"fecha":fecha_actual, "numeros": numeros_unoaldiez}
    return render(request, "usuarios/test.html", contexto)