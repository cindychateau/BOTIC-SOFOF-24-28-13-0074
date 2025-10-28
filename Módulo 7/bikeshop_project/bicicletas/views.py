from django.shortcuts import render, redirect, get_object_or_404
from .models import Bicicleta
from .forms import BicicletaForm

def home(request):
    bicicletas = Bicicleta.objects.all() 
    return render(request, 'home.html', {"bicicletas":bicicletas})

def crear(request):
    form = BicicletaForm()
    if request.method == 'POST': #Recibiendo la info del formulario
        form = BicicletaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
    return render(request, 'crear.html', {"form": form})