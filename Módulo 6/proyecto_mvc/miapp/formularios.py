from django import forms

class FormularioDeContacto(forms.Form):
    nombre = forms.CharField(label="Escribe tu nombre", max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Escribe tu correo electrónico", widget=forms.EmailInput(attrs={"class": "form-control"}))
    asunto = forms.CharField(label="Escribe el asunto", required=False, max_length=15, widget=forms.TextInput(attrs={"class": "form-control"}))
    mensaje = forms.CharField(label="Escribe tu mensaje", widget=forms.Textarea(attrs={"class": "form-control"})) #No existe un TextField, sino que explícitamente hay que indicar que ese campo será textarea
    subscripcion = forms.BooleanField(label="Deseo recibir notificaciones", required=False)



class FormularioDeSubscripcion(forms.Form):
    email = forms.EmailField(label="Escribe tu correo electrónico", widget=forms.EmailInput(attrs={"class": "form-control"}))