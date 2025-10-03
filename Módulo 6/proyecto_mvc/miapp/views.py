from django.shortcuts import render, redirect #Muestra una plantilla de HTML
from django.http import HttpResponse #Importo para mostrar una respuesta de http
from .models import Producto #Importando la clase Producto del archivo models
from .formularios import FormularioDeContacto, FormularioDeSubscripcion #Importando la clase FormularioDeContacto del archivo formularios

#Modelo auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
#Funciones que definen qué mostrar al usuario

def funcion_prueba(request):
    return HttpResponse("¡Hola desde miapp!")

def hola(request, nombre):
    print(nombre)
    return HttpResponse(f"<h1>¡Hola {nombre}!</h1>")

#nombre = Elena, cantidad = 5
def hola_repetido(request, nombre, cantidad):
    respuesta = ''
    for i in range(cantidad):
        respuesta += f"<h2>¡Holis {nombre}!</h2>"
    
    return HttpResponse(respuesta)

@login_required
def home(request):
    #Diccionario con la información de 1 usuario. nombre, apellido, edad
    usuario = {
        "nombre": "Elena",
        "apellido": "De Troya",
        "edad": 25
    }

    nombre = "Elena De Troya"

    return render(request, 'home.html', {"nombreCompleto": nombre, "usuario": usuario}) #Enviamos a nuestro HTML. SIEMPRE debe tener formato de diccionario

def calculadora(request, num1, num2, operacion):
    operacion = operacion.lower()
    resultado = 0
    if operacion == "suma":
        resultado = num1 + num2
    elif operacion == "resta":
        resultado = num1 - num2
    else:
        resultado = "Operación inválida"
    
    return HttpResponse(resultado)

def contacto(request):
    #Detectar el tipo de petición
    if request.method == 'POST':
        #Recibir la información del formulario
        formulario = FormularioDeContacto(request.POST)
        #Revisar que los datos sean válidos
        if formulario.is_valid():
            #Procesar los datos
            #Cleaned Data: regresar la info sin espacio y con tipo de dato correcto
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            asunto = formulario.cleaned_data['asunto']
            mensaje = formulario.cleaned_data['mensaje']
            subscripcion = formulario.cleaned_data['subscripcion']

            #Acción que quieres hacer con esos datos
            print("=======INFORMACION DEL FORMULARIO=======")
            print(nombre, email, asunto, mensaje, subscripcion)

            #redirección: 1.- Tenga una ruta definida
            #2.- función en vistas
            return redirect('contacto_exito') #Cambia la URL, voy a una nueva ruta

        else: #De lo contrario mostrar error
            return render(request, 'contacto.html', {'formulario': formulario})

    else: #Petición de tipo get
        formulario = FormularioDeContacto()
        return render(request, 'contacto.html', {'formulario': formulario})

def contacto_exito(request):
    return render(request, 'contacto_exito.html')

def estudiantes(request):
    estudiantes = [
        {"nombre": "Elena de Troya", "curso": "Java"},
        {"nombre": "Juana de Arco", "curso": "Python"},
        {"nombre": "Pablo Picasso", "curso": "MERN"},
        {"nombre": "Pedro Páramo", "curso": "Fundamentos de la Web"}
    ]
    return render(request, 'estudiantes.html', {"estudiantes":estudiantes})

def productos(request):
    productos = [
        Producto(nombre="Chocolate", descripcion="El chocolate más delicioso del mundo", precio=1.99, fecha_creacion="2025-09-27", disponible=True),
        Producto(nombre="Completo", descripcion="Contiene: vienesa, palta, tomate, mayonesa casera", precio=1.50, fecha_creacion="2025-09-27", disponible=False),
        Producto(nombre="Galletas", descripcion="Galletas de Chocolate tipo oreo", precio=0.70, fecha_creacion="2025-09-27", disponible=True),
        Producto(nombre="Helado", descripcion="Sabores disponibles: Vainilla, Chocolate, Frutilla, Napolitano", precio=2.50, fecha_creacion="2025-09-27", disponible=False)
    ]
    contexto = {"productos": productos}
    return render(request, 'productos.html', contexto)

def producto(request, indice): #indice = 0
    productos = [
        Producto(nombre="Chocolate", descripcion="El chocolate más delicioso del mundo", precio=1.99, fecha_creacion="2025-09-27", disponible=True),
        Producto(nombre="Completo", descripcion="Contiene: vienesa, palta, tomate, mayonesa casera", precio=1.50, fecha_creacion="2025-09-27", disponible=False),
        Producto(nombre="Galletas", descripcion="Galletas de Chocolate tipo oreo", precio=0.70, fecha_creacion="2025-09-27", disponible=True),
        Producto(nombre="Helado", descripcion="Sabores disponibles: Vainilla, Chocolate, Frutilla, Napolitano", precio=2.50, fecha_creacion="2025-09-27", disponible=False)
    ]
    
    try:
        producto = productos[indice] #Obtengo el producto en base al indice
    except IndexError:
        producto = None
        print("Producto no existe")
    contexto = {"producto": producto}
    return render(request, 'producto.html', contexto)
    
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