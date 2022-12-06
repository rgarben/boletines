'''
10. Escribir una función que, devuelva el número de palabras que hay en una cadena que recibe
como parámetro. Ten en cuenta que entre dos palabras puede haber más de un blanco.
También al principio y al final de la frase puede haber blancos redundantes.
Por ejemplo, si la cadena es “He estudiado mucho”, debe devolver 3

Rafael García Benítez
'''

def contarPalabras(cadena):
    contador = 0
    for i in range(len(cadena)):
        if i<len(cadena)-1 and cadena[i]==' ' and cadena[i+1]!=' ':
            contador+=1
    return contador

print(contarPalabras('     He         estudiado       mucho    '))