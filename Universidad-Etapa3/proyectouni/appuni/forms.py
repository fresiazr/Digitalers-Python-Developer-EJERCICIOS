from django import forms
from .models import Alumno

class FormularioAlumno(forms.ModelForm):
     class Meta:
        model = Alumno
        fields = ('id', 'nombre', 'edad', 'materia')
        labels = {
            'nombre': 'Nombre',
            'edad': 'Edad',
            'materia': 'Materia'
        }

        nombre = forms.CharField(max_length=128)
        edad = forms.IntegerField()
        materia = forms.ChoiceField()