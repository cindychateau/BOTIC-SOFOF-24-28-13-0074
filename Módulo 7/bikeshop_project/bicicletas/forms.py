from django import forms
from .models import Bicicleta

class BicicletaForm(forms.ModelForm):
    class Meta:
        model = Bicicleta
        fields = '__all__' #['marca', 'modelo']
        #exclude = ['disponible']
        '''
        labels = {
            'marca': 'Marca de Bicicleta',
        }
        '''