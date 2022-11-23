'''
10. Modifica el programa anterior para que en lugar de un asterisco podamos utilizar
cualquier otro caracter.

Rafael Garcia Benitez
'''

numero = int(input("Introduce el tamaño de las 3 figuras: "))
caracter=input("Introduce un caracter para dibujar las figuras: ")

print("\na.- Acudrado:\n")
for i in range(1, numero+1):    
    if (i==1) or (i==numero):
        print(f'{caracter} '*numero)
    else:
        print(f'{caracter}'+(' '*((numero*2)-3)+f'{caracter}'))
print("\na.- Rombo:\n")
for i in range(1, numero+1):    
    if i==1:
        print(' '*(numero-i)+f'{caracter}'*i)
    elif i==numero:
        print(f'{caracter} '+' '*((numero*2)-4)+f'{caracter} ')
    else:
        print(' '*(numero-i)+(f'{caracter}')+(' '*((i*2)-3))+f'{caracter}')
for i in range(numero-1, 0, -1):    
    if i==1:
        print(' '*(numero-i)+f'{caracter}'*i)
    elif i==numero:
        print(f'{caracter} '+' '*((numero*2)-4)+f'{caracter} ')
    else:
        print(' '*(numero-i)+(f'{caracter}')+(' '*((i*2)-3))+f'{caracter}')
print("\na.- Tringulo:\n")
for i in range(1, numero+1):    
    if i==1:
        print(' '*(numero-i)+f'{caracter}'*i)
    elif i==numero:
        print(f'{caracter}'*((numero+i)-1))
    else:
        print(' '*(numero-i)+(f'{caracter}')+(' '*((i*2)-3))+f'{caracter}')