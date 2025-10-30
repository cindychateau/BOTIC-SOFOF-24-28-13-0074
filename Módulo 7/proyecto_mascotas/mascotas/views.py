from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Mascota
from .forms import MascotaForm
from django.urls import reverse_lazy

class MascotaListView(ListView):
    model = Mascota
    #por defecto, va a buscar en templates/app/nombremodelo_list.html
    #templates/mascotas/mascota_list.html
    template_name = "lista_mascotas.html"
    #envia a la plantilla modelo_list -> mascota_list
    context_object_name = "mascotas"

class MascotaCreateView(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = "formulario_mascota.html" #por defecto: templates/mascotas/mascota_form.html
    success_url = reverse_lazy("lista_mascotas") #Devolver la URL correspondiente a ese nombre

class MascotaUpdateView(UpdateView):
    model = Mascota
    #form_class = MascotaForm
    fields = ['nombre', 'especie', 'edad', 'descripcion']
    template_name = "formulario_mascota.html" #por defecto: templates/mascotas/mascota_form.html
    success_url = reverse_lazy("lista_mascotas") #Devolver la URL correspondiente a ese nombre

class MascotaDeleteView(DeleteView):
    model = Mascota
    #por defecto: templates/mascotas/mascota_confirm_delete.html
    template_name = "confirmar_borrado_mascota.html"
    success_url = reverse_lazy("lista_mascotas")

class MascotaDetailView(DetailView):
    model = Mascota
    template_name = "detalle_mascota.html" #por defecto: templates/mascotas/mascota_detail.html
    context_object_name = "mascota" #object