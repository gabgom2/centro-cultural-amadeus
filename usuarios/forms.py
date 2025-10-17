from django import forms
from usuarios.models import Estudiante

class EstudianteForm(forms.ModelForm):
    class Meta:
        
        model = Estudiante
        fields = ["apellido", "nombre", "dni", "telefono", "barrio_residencia", "email", "nivel"]
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs.update({
                    'class': 'form-control'
                })
        
 