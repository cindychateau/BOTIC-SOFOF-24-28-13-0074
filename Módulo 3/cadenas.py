#CADENAS - String - Textos
abecedario = "ABCDEFG"
nombre = 'Juana'
apodo = "juanita"
edad = 10

print("Este es el abecedario", abecedario) #Separa los argumentos en un print y me da los espacios automaticamentes
print("La edad de alguien es:", edad)
print("Este es el abecedario", abecedario, sep="!!!")

print("Este es el abecedario "+ abecedario) # + -> me va a pegar(concatenar) los textos tal cual están
#print("La edad de alguien es:"+edad) -> TypeError
print("La edad de alguien es:"+str(edad))
print(f"Este es el abecedario {abecedario}") #Interpolación
print(f"Les presento a {nombre}, le pueden llamar '{apodo}'")
print("Les presento a "+nombre+", le pueden llamar '"+apodo+"'")

print("Les presento a {}, le pueden llamar '{}'".format(nombre, apodo))

#Métodos para manipular cadenas
frase = f"hola mundo! soy {nombre} de Arco y hoy es 4 de Julio"
print(frase.title()) #Primera letra de cada palabra en mayúscula
print(frase.capitalize()) #Primera letra en mayúscula, el resto en minúsculas
print(frase.upper()) #TODA LA FRASE EN MAYÚSCULAS
print(frase.lower()) #toda la frase en minúsculas
print(frase.count("oy")) #Regresa cuántos "oy" hay en la cadena
print(frase.replace("oy", "ay")) #Busca y reemplaza el primer valor por el segundo
print(frase.find("juana")) #Devuelve el índice donde comienza el valor dado. Case-sensitive. -1 si no encuentra el valor

texto = "Elena!Juana!Pablo!Pedro"
print(texto.split("!")) #Crea una lista con la división de mi cadena en base al caracter dado
print(frase.isalpha()) #Regresa True si es un texto con solo letras, False si tiene algún otro caracter
print("123".zfill(5)) #Rellena con ceros por la izq hasta tener n caracteres

saludo = "    hola python.      "
print(saludo.strip()) #Eliminar los espacios vacío del principio y del final

print("Hola".rjust(10))
print("Hola".center(10))

'''
Pide al usuario su nombre, un número favorito, y un lugar favorito.

Usa la función random.choice() para seleccionar aleatoriamente entre dos posibles mensajes:

“Hoy es un buen día para ti en {lugar}. Confía en tu número {numero}.”

“Tal vez hoy no sea el mejor día para visitar {lugar}. Evita pensar en el número {numero}.”

Muestra el mensaje, personalizando el lugar y número con los datos ingresados. Convierte el nombre a mayúsculas en el saludo.
'''

'''
Pide al usuario que escriba una frase.
Pide al usuario que escriba una letra

Reemplaza en la frase la letra dada por una X.

Muestra:
La frase original.
La frase censurada.
La cantidad de caracteres que tenía la frase original.

Escribe una frase: ¡Me encanta el rock and roll!
Escribe una letra: o
Frase original: ¡Me encanta el rock and roll!
Frase censurada: ¡Me encanta el rXck and rXll!
Cantidad de caracteres: 29

'''