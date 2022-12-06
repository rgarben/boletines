'''
8. Diseñar una función que determine la cantidad de vocales diferentes, que tiene una palabra
o frase introducida por teclado. Por ejemplo, la cadena “Abaco”, devolvería 2.

Rafael García Benítez
'''

def contarVocalesDiferentes (cadena):
    listaVocales = []
    cadenaVocales = 'aeiou'
    for i in range(len(cadena)):
        if cadena[i] in cadenaVocales and cadena[i] not in listaVocales:
            listaVocales.append(cadena[i])
        numVocales=len(listaVocales)
    return numVocales

print(contarVocalesDiferentes('Abaco'))