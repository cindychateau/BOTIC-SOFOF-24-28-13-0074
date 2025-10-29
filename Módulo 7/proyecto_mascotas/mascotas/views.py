from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Mascota

class MascotaListView(ListView):
    model = Mascota
    #por defecto, va a buscar en templates/app/nombremodelo_list.html
    #templates/mascotas/mascota_list.html
    template_name = "lista_mascotas.html"
    #envia a la plantilla modelo_list -> mascota_list
    context_object_name = "mascotas"