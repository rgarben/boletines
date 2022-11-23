'''
4. Diseña un programa que reciba el tamaño de una secuencia numérica y muestre en
una única línea cada una de las siguientes secuencias. Si se recibe el número 6 se
imprimiría:
a. 1, -5, 25, -125, 625, -3125 (-5 elevado i)
b. 1, -1, 0, 1, -1, 0 (i modulo 3)
c. 1, 3, 9, 27, 81, 243 (3 elevado a i)

Rafael Garcia Benitez
'''

tamaño = int(input("Introduce el tamaño de la secuencia: "))
lineaA=" "
lineaB=" "
lineaC=" "
while tamaño<0:
    tamaño = int(input("Introduce un nuemro positivo para el tamaño de la secuencia: "))
for i in range(tamaño):
    a=-5**i
    b=(i%-3)+1
    c=3**i
    lineaA+=", "+str(a)
    lineaB+=", "+str(b)
    lineaC+=", "+str(c)
print("a. "+ lineaA)
print("b. "+ lineaB)
print("c. "+ lineaC)