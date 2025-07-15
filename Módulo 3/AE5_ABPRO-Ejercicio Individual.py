matriz = [ 
    [10, 15, 20], 
    [3, 7, 14] 
]
matriz[1][0] = 6
print(matriz)


cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]

cantantes[0]["nombre"] = "Enrique Martin Morales"
print(cantantes)


ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

ciudades["México"][2] = "Monterrey"
print(ciudades)


coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

coordenadas[0]["latitud"] = 9.9355431
print(coordenadas)

'''
Cambia el valor 3 en matriz por 6.

Cambia el nombre del primer cantante por "Enrique Martin Morales".

En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".

En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
'''

'''
cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
'''

for cantante in cantantes: #cantante = {"nombre": "Ricky Martin", "pais": "Puerto Rico"}
    print(f"nombre - {cantante["nombre"]}, pais - {cantante["pais"]}")

for c in cantantes:
    print(c["nombre"])

for y in cantantes:
    print(y["pais"])


costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for clave in costa_rica:
    print(len(costa_rica[clave]), clave.upper())
    for elemento in costa_rica[clave]:
        print(elemento)

for clave, valor in costa_rica.items():
    print(len(valor), clave.upper())
    for elemento in valor:
        print(elemento) 
    print()