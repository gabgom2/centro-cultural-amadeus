from django.urls import path
from usuarios.views import renderizar_index, testing

urlpatterns = [
    path('', renderizar_index, name="index"),
    path("test/", testing, name="test")
    path("estudiantes/", estudiantes, name="estudiantes")
]