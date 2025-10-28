numeros = [10, 20, 30]
numeros.append(40) #numeros = [10, 20, 30, 40]
print(len(numeros)) #len -> tamaño

def es_par(n):
    return n % 2 == 0

print(es_par(2))
print(es_par(3))