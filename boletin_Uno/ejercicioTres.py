'''
3. Escribir una expresión lógica que cumpla:
a) Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60
euros pero igual o inferior a 420 euros.
b) Debe ser Verdadera si el numero contenido en la variable entera numero es impar.
c) Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son
válidas.
d) Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir, que
estén comprendidas entre 0:0 y 23:59.
e) Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una
persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado).
NOTA: Además siempre debe ser Falsa en el caso contrario al que se formula.

Rafael García Benítez
'''

precio = 140
print(60<= precio and precio <=420)

print(precio%2==0)

saldo = 500
dineroSacar = 450

print(saldo >=0 and dineroSacar<=saldo and dineroSacar>0)

hora =22
minutos = 54

print((hora >=0 and minutos>=0) and (hora <=23 and minutos<=59))

estadoCivil = 'S'

print(not(estadoCivil== 'S' or estadoCivil== 'C' or estadoCivil== 'V' or estadoCivil== 'D'))
