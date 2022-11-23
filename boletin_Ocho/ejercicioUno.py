'''
1. Crea un programa que genere 100 números de forma aleatoria y que posteriormente
ofrezca al usuario la posibilidad de:
a. Conocer el mayor
b. Conocer el menor
c. Obtener la suma de todos los números
d. Obtener la media
e. Sustituir el valor de un elemento por otro número introducido por teclado
f. Mostrar todos los números
⇒ Realiza cada una de las opciones con funciones.
⇒ Utiliza la función siguiente para generar números aleatorios (entre 0 y 1000).

Rafael Garcia Benitez
'''

from random import randint

lista = []

for i in range (100):
    lista.append(randint(0, 1000))
print("La lista de los 100 numeros aleatorios => ", lista)

def obtenerElementoMayor (lista):
    mayor=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor
print("El numero mayor de la lista es: ", obtenerElementoMayor(lista))
def obtenerElementoMenor (lista):
    menor=1000
    for i in range(len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor
print("El numero menor de la lista es: ", obtenerElementoMenor(lista))
def obtenerElementoSuma (lista):
    suma=0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma
print("La suma de los numeros de la lista es: ", obtenerElementoSuma(lista))
def obtenerElementoMedia (lista):
    media=obtenerElementoSuma(lista)/(len(lista))
    return media
print("La media de los numeros de la lista es: ", obtenerElementoMedia(lista))
buscar = int(input("Introduce el numero que quieras buscar en la lista: "))
cambiar = int(input("Introduce el numero que por el que quieras sustituirlo: "))
def cambiarNumeroLista(lista, ls, vc):
    for i in range(len(lista)):
        if lista[i]==ls:
            lista[i]=vc
    return lista
print("La lista con el numero cambiado si se encontro o no => ", cambiarNumeroLista(lista, buscar, cambiar))

