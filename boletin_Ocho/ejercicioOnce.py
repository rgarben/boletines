'''
11. Escribe una función intersect que reciba dos listas y devuelva otra lista con los
elementos que son comunes a ambas, sin repetir ninguno.

Rafael García Benítez
'''

lista3 = ['a', 'a', 'c', 'd', 'e', 'e', 'g']
lista4 = ['a', 'a', 'c', 'u', 'c', 'e', 'g', 'g']

def buscarComunes(lista1,lista2):
    listaComunes = []
    for i in range(len(lista1)):
        if lista1[i] in lista2 and lista1[i] not in listaComunes :
            listaComunes.append(lista1[i])
    return listaComunes

print(buscarComunes(lista3, lista4))