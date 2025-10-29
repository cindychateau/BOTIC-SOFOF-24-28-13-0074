from django import forms
from .models import Mascota

class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = '__all__' #['nombre', 'especie']
        #exclude = ['descripcion']