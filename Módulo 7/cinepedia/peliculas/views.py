from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
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

def pagina_sinpermisos(request):
    return render(request, 'pagina_sinpermisos.html')

class PeliculaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pelicula
    template_name = 'formulario.html'
    fields = ['nombre', 'director', 'fecha_estreno', 'sinopsis']
    success_url = reverse_lazy('pelicula-index')
    #Se manda al template object

    def test_func(self):
        pelicula = self.get_object()
        return self.request.user == pelicula.publicado_por
    
    def handle_no_permission(self): #403: Forbidden
        #redirect pagina sin permisos
        return redirect('pagina_sinpermisos')