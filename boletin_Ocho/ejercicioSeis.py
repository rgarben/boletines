'''
6. Diseña una función llamada estaOrdenada que reciba una lista de elementos y
devuelva True si está ordenada o False en caso contrario.

Rafael García Benítez
'''

listaOrdenada = [1, 2, 3, 4, 5, 6]

def ordenarLista(lista):
    verdad=True
    for i in range(len(listaOrdenada)-1):
        contador=0
        if contador==(len(listaOrdenada)-1):
            verdad=True
        elif listaOrdenada[i]<listaOrdenada[i+1]:
            contador+=1
        else:
            verdad=False  
    return verdad              
print(ordenarLista(listaOrdenada))

'''
for i in range(len(listaOrdenada)-1):
    if listaOrdenada[i]>listaOrdenada[i+1]: 
        verdad=False 
print(verdad)
'''
'''
def estaOrdenadaLista(lista):
    ordenada = True
    i = 0
while i < len(lista-1 and ordenada):
    for i in range(len(listaOrdenada)-1):
    if listaOrdenada[i]>listaOrdenada[i+1]: 
        verdad=False
    return verdad
'''
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         