'''
8. Escribe un programa que pregunte por el tipo de figura que quiere pintar y el tamaño
del lado de la figura y genere las figuras correspondientes en el siguiente formato
(los valores 3, 4 y 5 son de ejemplo, podrían pedirse desde 1 hasta 10).
a. Cuadrados:
b. Triángulos:
c. Rombos:

Rafael Garcia Benitez
'''

numero = int(input("Introduce el tamaño de las 3 figuras: "))

print("a. Cuadrados:\n")
for i in range(numero):
    print('* '*numero)
print("b. Triángulos:\n")
for i in range(1, numero+1):
    print(' '*(numero-i)+('*'*((i*2)-1)))
print("a. Rombos:\n")
for i in range(1, numero+1):
    print(' '*(numero-i)+('*'*((i*2)-1)))
for i in range(numero-1, 0, -1):
    print(' '*(numero-i)+('*'*((i*2)-1)))