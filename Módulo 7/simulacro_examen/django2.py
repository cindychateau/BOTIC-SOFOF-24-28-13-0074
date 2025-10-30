from django.views.generic import ListView
from .models import Libro

class LibroListView(ListView):
    model = Libro
    template_name = 'libros.html'
    context_object_name = 'libros'