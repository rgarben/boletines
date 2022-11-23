'''
18. Escribe un programa que pida el limite inferior y superior de un intervalo. Si el límite
inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando termine
el programa dará las siguientes informaciones:
◦ La suma de los números que están dentro del intervalo (intervalo abierto).
◦ Cuantos números están fuera del intervalo.
◦ Informa si hemos introducido algún número igual a los límites del intervalo.

Rafael García Benítez
'''

inferior = int(input("Introduce numero inferior: "))
superior = int(input("Introduce numero superior: "))
suma = 0
suma1 = 0
suma2 = 0

while inferior >= superior:
    
    inferior = int(input("Introduce un numero inferior menor que el superior: "))
    numero = int(input(f"Introduce numeros dentro del intervalo {inferior, superior}, introduce 0 para finalizar el programa: "))
while numero != 0:
        
    if inferior < numero < superior:
        suma+=suma
    elif numero < inferior or numero > superior:
        suma1+=+1
    else:
        suma2+=+1
    numero = int(input(f"Introduce numeros dentro del intervalo {inferior, superior}, introduce 0 para finalizar el programa: "))
    
print()
print(f"La suma de los numeros es: {suma}")
print()
print(f"La cantidad de los numeros fuera del intervalo es: {suma1}")
print()
print(f"La cantidad de los numeros que son iguales a los intervalos es: {suma2}")
print()