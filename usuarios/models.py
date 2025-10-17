from django.db import models

# Create your models here.

class Estudiante(models.Model):

    
    nivel = [
        ("n1", "inicial"),
        ("n2" , "intermedio"),
        ("n3" ,"avanzado"),
    ]
        
        
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    telefono = models.IntegerField(unique=True)
    email = models.EmailField()
    barrio_residencia = models.CharField(max_length=100)
    nivel = models.CharField(max_length = 2, choices=nivel, default=nivel[0])
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Nombre completo: {self.apellido}, {self.nombre} / DNI: {self.dni} / Nivel: {self.nivel}"
    
