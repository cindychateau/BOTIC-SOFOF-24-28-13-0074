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

    return render(request, 'formulario.html', {"form": form})

def actualizar(request, id):
    bicicleta = get_object_or_404(Bicicleta, id=id) #Obtiene el objeto, en caso de no existir regresa un error 404
    form = BicicletaForm(instance=bicicleta)
    if request.method == 'POST':
        form = BicicletaForm(request.POST, instance=bicicleta)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'formulario.html', {"form": form})

def eliminar(request, id):
    bicicleta = get_object_or_404(Bicicleta, id=id)
    bicicleta.delete()
    return redirect('home')

def detalle(request, id):
    bicicleta = get_object_or_404(Bicicleta, id=id)
    return render(request, 'detalle.html', {"bicicleta": bic})