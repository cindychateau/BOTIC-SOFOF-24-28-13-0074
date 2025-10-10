from django import forms
'''
<form>
    <p>
        <label>Escribe el nombre:</label>
        <input type="text" >
    </p>
</form>
'''
class MascotaForm(forms.Form):
    nombre = forms.CharField(max_length=60, label="Nombre")
    edad = forms.IntegerField(label="Edad")
    especie = forms.CharField(max_length=60, label="Especie")
    descripcion = forms.CharField(widget=forms.Textarea, label="Descripción")