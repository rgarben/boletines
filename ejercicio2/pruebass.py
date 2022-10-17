'''
cantidad = int(input("Introduce la cantidad de numeros: "))

while cantidad <= 0:
    cantidad = int(input("Introduce la cantidad de numeros: "))

total = 0

for i in range(cantidad):
    numero = int(input("Introduce un numero mayor que 0: "))
    while numero <= 0:
            numero = int(input("Error: Introduce un numero mayor que 0: "))
    total += numero
print(f"La media es {total/cantidad}")
'''
'''
cantidad = int(input("Introduce la cantidad de numeros: "))

while cantidad <= 0:
    cantidad = int(input("Introduce la cantidad de numeros: "))

total, contador = 0, 0

while cantidad > contador:
    numero = int(input("Introduce un numero mayor que 0: "))
    while numero <= 0:
            numero = int(input("Error: Introduce un numero mayor que 0: "))
    contador +=1
    total += numero
print(f"La media es {total/cantidad}")
'''