from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Pelicula
from django.urls import reverse_lazy
from .forms import ComentarioForm

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

class PeliculaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pelicula
    template_name = 'borrar.html'
    success_url = reverse_lazy('pelicula-index')

    def test_func(self):
        pelicula = self.get_object()
        return self.request.user == pelicula.publicado_por
    
    def handle_no_permission(self): #403: Forbidden
        #redirect pagina sin permisos
        return redirect('pagina_sinpermisos')

class PeliculaDetailView(LoginRequiredMixin, DetailView):
    model = Pelicula
    template_name = 'detalle.html'
    context_object_name = 'pelicula'

    def get_context_data(self, **kwargs): #keyword arguments
        context = super().get_context_data(**kwargs) #OBTENGO el objeto original
        context['comentario_form'] = ComentarioForm()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object() #Obtengo la película
        form = ComentarioForm(request.POST)
        if form.is_valid():
            #Todo: Guardamos
            pass
        else:
            context = self.get_context_data()
            context['comentario_form'] = form
            return self.render_to_response(context)