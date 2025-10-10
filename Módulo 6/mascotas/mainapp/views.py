from django.shortcuts import render, redirect
from .models import Mascota
#Importación de formulario
from .forms import MascotaForm

#Importar Modelo auth: User, authenticate, login, logout, decoradores (@login_required, @permission_required)
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required

#Obtener a los 2 usuarios
elena = User.objects.get(username='elena')
juana = User.objects.get(username='juana')
#Lista de mascotas
MASCOTAS = [
    Mascota(nombre = "Miu", edad = 8, especie = "Gato", descripcion = "Gatita peluda color blanca", dueno = elena),
    Mascota(nombre = "Michi", edad = 4, especie = "Gato", descripcion = "Gatita calico muy traviesa", dueno = juana),
]

@login_required
def home(request):
    #Filtrar las mascotas del usuario en sesión
    '''
    mis_mascotas = Mascota.objects.get(dueno=request.user) -> conexión bd
    mis_mascotas = []
    for mascota in MASCOTAS:
        if mascota.dueno == request.user:
            mis_mascotas.append(mascota)
    '''
    mis_mascotas = [mascota for mascota in MASCOTAS if mascota.dueno == request.user]
    #Enviar contexto (mascotas)
    return render(request, 'home.html', {'mascotas': mis_mascotas})

def login_view(request):
    #Revisar qué tipo de método tenemos en la petición
    if request.method == 'POST': #Significa que estamos recibiendo la información del formulario
        username = request.POST['username']
        password = request.POST['password']
        #autenticar al usuario
        usuario = authenticate(request, username=username, password=password) #usuario = None X
        if usuario is not None:
            #inicio sesión
            login(request, usuario) #Guardo en sesión la información del usuario
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})

    return render(request, 'login.html')

def logout_view(request):
    logout(request) #Función que está hecho de Modelo auth que elimina la sesión actual
    return redirect('login')

@login_required
@permission_required('mainapp.add_mascota', raise_exception=True)
def crear(request):
    formulario = MascotaForm() #Genera un formulario nuevo, sin datos
    #Revisar el tipo/método de petición
    if request.method == 'POST':
        #Recibimos la info del formulario
        formulario = MascotaForm(request.POST) #Formulario CON los datos que recibimos
        #Revisar que los datos que recibimos sean válidos
        if formulario.is_valid():
            #Cleaned data: regresa la información que se recibió quitando espacios extra y con el tipo de dato correcto
            nombre = formulario.cleaned_data['nombre'] #Peluchi
            edad = formulario.cleaned_data['edad'] #1
            descripcion = formulario.cleaned_data['descripcion']
            especie = formulario.cleaned_data['especie'] #perro

            #Creo un objeto Mascota
            nueva_mascota = Mascota(
                nombre = nombre, #Peluchi
                edad = edad, #1
                especie = especie, #perro
                descripcion = descripcion, #Perrito jugueton con pelo largo
                dueno = request.user #el usuario que inicio sesión se establece como dueño
            )

            MASCOTAS.append(nueva_mascota)
            return redirect('home')

    return render(request, 'nuevo.html', {'formulario': formulario})

