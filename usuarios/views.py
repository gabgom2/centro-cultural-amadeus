from django.shortcuts import render

# Create your views here.

def renderizar_index(request):
    return render(request, "usuarios/index.html")