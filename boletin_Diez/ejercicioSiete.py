'''
7. Diseñar una función que reciba como parámetro tres cadenas, la primera será una frase y
deberá buscar si existe la palabra que recibe como segundo parámetro y reemplazarla por la tercera.

Rafael Garćia Benítez
'''

def sustituirPalabra(cadena, buscar, sustituir):
    contador = 0
    resul = ''
    guardar = ''
    for i in range(len(cadena)):
        if cadena[i]==buscar[contador]:
            if contador==len(buscar)-1:
                guardar = ''
                resul+=sustituir
                contador=0
            else:
                guardar+=cadena[i]
                contador+=1
        else:
            resul+=guardar+cadena[i]
            contador = 0
            guardar = ''
    return resul

print(sustituirPalabra('Buscar si existe la palabra que recibe.','palabra','mesa'))