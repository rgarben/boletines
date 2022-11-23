'''
5. Realiza una función reverse que reciba una lista y devuelva una nueva lista cuyo
contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’,
‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

Rafael García Benítez
'''

lista = ['Di', 'buen', 'día', 'a', 'papa']
#lista.reverse()
#print(lista)

def listaPatras (lista):
    listaRever = []
    for i in range(len(lista),0,-1):
        listaRever.append(lista[i-1])
    return listaRever
print(listaPatras(lista))