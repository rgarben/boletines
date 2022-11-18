'''


Rafael García Benítez
'''
numero = int(input("Introduce un numero: "))
peque = numero
preguntar = input("¿Desea ingresar más números (S/N)?")

while preguntar == 'S':
    numero = int(input("Introduce un numero: "))
    if numero < peque:
        peque = numero
    preguntar = input("¿Desea ingresar más números (S/N)?")
    
    
print(f"El numero mas pequeño introducido {peque} es el peque.")