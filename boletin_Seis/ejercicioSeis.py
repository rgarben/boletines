'''


Rafael García Benítez
'''

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el primer numero: "))
suma = 0
multi = 0

while suma<(abs(numero2)):
    suma+=1
    multi+=numero1
if numero2<0:
    multi=-multi
print(multi)