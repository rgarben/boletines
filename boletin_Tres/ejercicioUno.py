'''
1. Realizar un programa que lea un número entero por teclado e informe de si
el número es par o impar (el cero se considera par).

Rafael García Benítez
'''

numero = int(input("Introduce un numero: "))

if numero%2==0:
    print("El numero %s es par"%(numero))
else:
    print("El numero %s no es par"%(numero))