from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def renderizar_index(request):
    return render(request, "usuarios/index.html")

def estudiantes(request):
    return render(request, "usuarios/estudiantes.html")


def testing(request):
    fecha_actual = datetime.datetime(2025, 10, 17, 4, 30)
    numeros_unoaldiez = range(1, 11)
    contexto = {"fecha":fecha_actual, "numeros": numeros_unoaldiez}
    return render(request, "usuarios/test.html", contexto)