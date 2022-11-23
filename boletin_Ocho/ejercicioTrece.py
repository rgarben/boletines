'''
13. Escribe una función que, dada una lista de nombres y una letra, devuelva una lista
con todos los nombres que empiezan por dicha letra. Debe validar los datos.

Rafael García Benítez
'''

lista55 = ["pepe", "juan", "roberto", "josefa", "juliana", "j"]

def buscarNombres (lista):
    listaDevuelta = []
    for i in range(len(lista)-1):
        if lista[-1] in lista[i]:
            listaDevuelta.append(lista[i])
    return listaDevuelta

print(buscarNombres(lista55))