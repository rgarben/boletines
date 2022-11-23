'''
8. Realiza un programa que añada números enteros a una lista hasta que se
introduzca un número negativo. Haciendo uso de esta lista, elabora funciones que
devuelvan:
a. una lista con todos los que sean primos.
b. el sumatorio
c. el promedio de los valores.
d. una lista con el factorial de cada uno de esos números.

Rafael García Benítez
'''

listaNumeros = []
def obtenerElementoSuma (lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma
def obtenerElementoMedia (lista):
    media=obtenerElementoSuma(lista)/(len(lista))
    return media
listaPrimos = []
listaFactorial=[]
enteros = int(input("Introduce numeros enteros, para finalizar introduce uno negativo: "))
while enteros > 0:
    listaNumeros.append(enteros)
    contador = 0
    for i in range(2,enteros):
        if enteros %i==0:
            contador+=1
    if contador==0:
        listaPrimos.append(enteros)
    facto=1
    for i in range(enteros):
        facto*=i+1
    if i==enteros-1:
        listaFactorial.append(facto)
    enteros = int(input("Introduce numeros enteros, para finalizar introduce uno negativo: "))
print("Los numeros primo son", listaPrimos)
print("El sumatorio de la lista es:", obtenerElementoSuma(listaNumeros))
print("El promedio de la lista es:", obtenerElementoMedia(listaNumeros))
print("El factorial de lo numeros es:", listaFactorial)
print("Programa terminado.")