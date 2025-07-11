#Básico: imprime todos los números enteros del 0 al 100.
for i in range(101):
    print(i)

#Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for x in range(2, 501, 2):
    print(x)

for x in range(2, 501):
    if x % 2 == 0:
        print(x)

for multdos in range (1 , 251):
    print(multdos * 2)

#Contando Vanilla Ice: imprime los números enteros del 1 al 100. Si es divisible por 5 imprime “ice ice” en vez del número. Si es divisible por 10, solo imprime “baby”
for iceice in range(1, 101):
    if iceice % 10 == 0:
        print("baby")
    elif iceice % 5 == 0:
        print("ice ice")
    else:
        print(iceice)