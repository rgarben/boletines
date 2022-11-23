'''
11. Cuadrado de números:
Crea un programa que lea del teclado un número y genere un cuadrado con el patrón siguiente
donde cada elemento está separado por un espacio.
Resultados de ejemplo:

Rafael Garcia Benitez
'''

numero = 4

for i in range(numero+1):

    print(f"{numero} "*((numero*2)-1))
    numero+=-1

#lo intente pero no se me ocurre como