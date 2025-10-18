from django.db import models

# Create your models here.

class Estudiante(models.Model):

    
      
        
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    telefono = models.IntegerField(unique=True)
    email = models.EmailField()
    barrio_residencia = models.CharField(max_length=100)

    #autoasignadas
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Nombre completo: {self.apellido}, {self.nombre} / DNI: {self.dni} / Email: {self.email}"
    
class Docente(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(unique=True)
    telefono = models.IntegerField(unique=True)
    email = models.EmailField()
    puntaje_docente = models.FloatField(default=3.0)
    
    #autoasignadas
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Nombre completo: {self.apellido}, {self.nombre} / DNI: {self.dni} / Puntaje: {self.puntaje_docente}"






class Asignatura(models.Model):
    
    nivel = [
        ("n1", "inicial"),
        ("n2" , "intermedio"),
        ("n3" ,"avanzado"),
    ]
    
    nombre_asignatura = models.CharField(max_length=100)
    nivel = models.CharField(max_length = 2, choices=nivel, default=nivel[0])
    horas_catedra = models.IntegerField()
    
    #autoasignadas
    codigo = models.IntegerField(unique=True, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def generar_codigo(self):
        #Aumentar el código actual
        codigo_anterior = Asignatura.objects.all().order_by('codigo').last()
        
        if codigo_anterior:
            return codigo_anterior.codigo + 1
        else:
            return 100 #valor inicial
        
    def save(self, *args, **kwargs):
    # Si el codigo no está asignado se generará antes de guardarse
        if self.codigo is None:
            self.codigo = self.generar_codigo()
        super(Asignatura, self).save(*args, **kwargs)
        
    def __str__(self):
        return f"Asignatura: {self.nombre_asignatura} / Nivel: {self.nivel} / Código: {self.codigo}"

    
