'''
12. Escribe una función unionListas que reciba dos listas y devuelva los elementos que
pertenecen a una, o bien, a la otra, pero sin repetir ninguno (unión de conjuntos).

Rafael García Benítez
'''

lista3 = ['a', 'a', 'c', 'd', 'e', 'e', 'g']
lista4 = ['a', 'a', 'c', 'u', 'c', 'e', 'g']

def unionListas(lista1,lista2):
    listaUnion = []
    for i in range(len(lista1)):
        if lista2 and lista1[i] not in listaUnion :
            listaUnion.append(lista1[i])
        if lista1 and lista2[i] not in listaUnion :
            listaUnion.append(lista2[i])
    return listaUnion

print(unionListas(lista3, lista4))