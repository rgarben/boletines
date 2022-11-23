'''
Bucles avanzado I
1. Crea un programa que tras preguntar por dos números realice la división del mayor
de ellos por el menor y muestre el resultado de la división, es decir, el cociente y el
resto. Solo puedes utilizar la suma o la resta, pero no otras operaciones.

Rafael Garcia Benitez
'''

numero1 = int(input("Introduce el primero numero: "))
numero2 = int(input("Introduce el segundo numero: "))
contador = 0
resto = 0

while numero1 <= 0:
    numero1 = int(input("Error: introduce el primer numero mayor que 0: "))
while numero2 <= 0:
    numero2 = int(input("Error: introduce el segundo numero mayor que 0: "))
while numero1>=numero2:
    numero1=numero1-numero2
    contador+=1
    resto=numero1
print(f"El cociente es {contador} y el resto es {resto}.")
while numero1<=numero2:
    numero2=numero2-numero1
    contador+=1
    resto=numero2
print(f"El cociente es {contador} y el resto es {resto}.")