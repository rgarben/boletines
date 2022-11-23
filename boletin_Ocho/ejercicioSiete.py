'''
7. Escribir una función denominada encajan que indique si dos fichas de dominó
encajan o no. Las fichas son recibidas en dos cadenas de texto con el siguiente
formato
[3,4] [2,5]

Rafael Garcia Benitez
'''

ficha1 = [3,4]
ficha2 = [2,5]

ficha3 = [6,1]
ficha4 = [1,2]

def fichasEncajan (ficha1, ficha2):
    encaja = "No encajan"
    if (ficha1[0] in ficha2) or (ficha1[1] in ficha2):
        encaja="Encaja"
    return encaja
print(fichasEncajan(ficha3, ficha4))