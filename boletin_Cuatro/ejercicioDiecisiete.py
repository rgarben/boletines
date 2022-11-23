'''
17. Escribir un programa que imprima todos los números pares entre dos números que se le
pidan al usuario

Rafael García Benítez
'''

numero1 = int(input("Introduce el primero numero: "))
numero2 = int(input("Introduce el primero numero: "))

if numero1 < numero2:

    for i in range(numero1+1, numero2):
        
        if i%2==0:
            print(i)
            
if numero2 < numero1:
    
    for i in range(numero2+1, numero1):
        if i%2==0:
            print(i)