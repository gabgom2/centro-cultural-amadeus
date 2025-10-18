from django import forms
from usuarios.models import Estudiante, Docente, Asignatura

def agregar_form_control():
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs.update({
                    'class': 'form-control'
                })

#DRY
class EstudianteForm(forms.ModelForm):
    class Meta:
        
        model = Estudiante
        fields = ["apellido", "nombre", "dni", "telefono", "barrio_residencia", "email"]
        
        agregar_form_control()

class DocenteForm(forms.ModelForm):
    
    class Meta:
        
        model = Docente
        fields = ["apellido", "nombre", "dni", "telefono", "email", "puntaje_docente"]
        
        agregar_form_control()
        
class AsignaturaForm(forms.ModelForm):
    
    class Meta:
        
        model = Asignatura
        fields = ["nombre_asignatura", "nivel", "horas_catedra"]
        
        agregar_form_control()
