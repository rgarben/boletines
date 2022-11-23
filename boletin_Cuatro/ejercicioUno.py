'''
1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

Rafael García Benítez
'''


cateto1 = int(input("Introduce primer cateto: "))
cateto2 = int(input("Introduce segundo cateto: "))

print("La hipotenusa es:", (cateto1**2+cateto2**2)**0.5)