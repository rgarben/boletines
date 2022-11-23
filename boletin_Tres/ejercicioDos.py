'''
2. Realizar un programa que solicite dos números por teclado e imprima en
pantalla si son iguales, el primero mayor que el segundo o el primero más
pequeño que el segundo.

Rafael García Benítez
'''

num1 = int(input("Introduce el primero numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1==num2:
    print("El numero %s y el numero %s son iguales."%(num1,num2))
elif num1>num2:
    print("El numero %s es mayor que el numero %s."%(num1,num2))
else:
    print("El numero %s es mas pequeño que el numero %s."%(num1,num2))