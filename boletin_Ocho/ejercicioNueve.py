'''
9. Desarrolla un programa que a partir de una lista de números y un entero k, realice la
llamada a tres funciones: a) para devolver una lista de números con los menores de
k, b) otra con los mayores y c) otra con aquellos que son múltiplos de k.

Rafael García Benítez
'''

listaNumero = [2, 34, 56, 74, 24, 65, 243]
numeroK = int(input("Introduce numero K: "))

def numerosMenoresLista(lista):
    listaNumeroMenor = []
    for i in range(len(listaNumero)):
        if numeroK>listaNumero[i]:
            listaNumeroMenor.append(listaNumero[i])
    return listaNumeroMenor
def numerosMayoresLista(lista):
    listaNumeroMayor = []
    for i in range(len(listaNumero)):
        if numeroK<listaNumero[i]:
            listaNumeroMayor.append(listaNumero[i])
    return listaNumeroMayor
def numerosMultiploLista(lista):
    listaNumeroMultiplo = []
    for i in range(len(listaNumero)):
        if numeroK%listaNumero[i]==0:
            listaNumeroMultiplo.append(listaNumero[i])
    return listaNumeroMultiplo
        
print("Numeros menores que", numeroK, numerosMenoresLista(listaNumero))
print("Numeros mayores que", numeroK, numerosMayoresLista(listaNumero))
print("Multiplos de", numeroK, numerosMultiploLista(listaNumero))