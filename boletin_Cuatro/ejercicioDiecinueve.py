'''
19. Escribe un programa que dados dos números, uno real (base) y un entero positivo
(exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el operador
de potencia.

Rafael García Benítez
'''

numeroReal = int(input("Introduce el numero real de la base: "))
numeroEntero = int(input("Introduce el numero entero positivo del exponente: "))
multi=1
for i in range (numeroEntero):
    multi=multi*numeroReal
print(multi)