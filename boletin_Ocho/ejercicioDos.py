'''
2. Realiza un programa que lea 10 números, los imprima separados por coma y a
continuación los desplace una posición (y los muestre por pantalla desplazados), de
tal forma que el último pase a la primera posición, el primero a la segunda, el
segundo a la tercera, y así sucesivamente.
Opcional: Añade un parámetro (D/I) a la función para que el controle el sentido del
desplazamiento (a derechas/izquierdas) y otro que indique el número de posiciones
a desplazar (0: quedaría igual, 1: desplaza una posición, etc.).

Rafael García Benítez
'''

lista2 = [1, 3, 5, 7, 9, 12, 15, 18, 21, 24]

def desplazarLista (lista):
    guardo = 0
    escrito = lista[0]
    for i in range(len(lista)):
        guardo = lista[(i+1)%len(lista)]
        lista[(i+1)%len(lista)] = escrito
        escrito = guardo
    return lista
print(desplazarLista(lista2))