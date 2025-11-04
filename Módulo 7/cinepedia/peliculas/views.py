from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, CreateView
from .models import Pelicula
from django.urls import reverse_lazy

def index(request):
    return render(request, 'index.html')

class PeliculaListView(LoginRequiredMixin, ListView):
    model = Pelicula
    template_name = 'lista.html'
    context_object_name = 'peliculas'

class PeliculaCreateView(LoginRequiredMixin, CreateView):
    model = Pelicula
    template_name = 'formulario.html'
    fields = ['nombre', 'director', 'fecha_estreno', 'sinopsis']
    success_url = reverse_lazy('pelicula-index')

    #Validación
    def form_valid(self, form):
        form.instance.publicado_por = self.request.user
        return super().form_valid(form)