'''
10.Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error.

Rafael García Benítez
'''

caracter = str(input("Introduce un caracter +, -, *, /: "))
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
if caracter == '+':
    print("La suma es:", num1+num2)
elif caracter == '-':
    print("La resta es:", num1-num2)
elif caracter == '*':
    print("La la multiplicación es:", num1*num2)
elif caracter == '/':
    print("La division es:", num1/num2)
else:
    print("Error, introduce operaciones +, -, *, /.")