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
    
class Docente(models.Model):
    #IGE funcion
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    telefono = models.IntegerField(unique=True)
    email = models.EmailField()
    puntaje_docente = models.FloatField(default=3.0)
    ige = models.IntegerField(unique=True, blank=True, null=True) 
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def generar_ige(self):
        #Aumentar el código actual
        ige_anterior = Docente.objects.all().order_by('ige').last()
        
        if ige_anterior:
            return ige_anterior.ige + 1
        else:
            return 30000 #valor inicial
        
    def save(self, *args, **kwargs):
    # Si el ige no está asignado se generará antes de guardarse
        if self.ige is None:
            self.ige = self.generar_ige()
        super(Docente, self).save(*args, **kwargs)
