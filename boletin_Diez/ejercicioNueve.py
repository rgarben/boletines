'''
9. Crear una función que, tomando una cadena de texto como entrada, construya y devuelva
otra cadena formada de la siguiente manera: el método debe colocar todas las consonantes
al principio y todas las vocales al final de la misma, eliminando los blancos.
Por ejemplo, pasándole la cadena "curso de programacion", una posible solución sería
"crsdprgrmcnuoeoaaio

Rafael García Benítez
'''

def deformarCadena(cadena):
    stringVocales = ''
    stringConsonantes = ''
    vocales = 'aeiou'
    for i in range (len(cadena)):
        if cadena[i] in vocales:
            stringVocales+=cadena[i]
        elif cadena[i] not in vocales and cadena[i]!=' ':
            stringConsonantes+=cadena[i]
        resultado=stringConsonantes+stringVocales
    return resultado

print(deformarCadena('curso de programacion'))