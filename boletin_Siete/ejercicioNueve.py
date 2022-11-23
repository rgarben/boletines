'''
9. Crea un programa nuevo basado en el anterior que genere las mismas figuras, pero
vacías:
Cuadrado Rombo Triángulo

Rafael Garcia Benitez
'''

numero = int(input("Introduce el tamaño de las 3 figuras: "))

print("\na.- Acudrado:\n")
for i in range(1, numero+1):    
    if (i==1) or (i==numero):
        print('* '*numero)
    else:
        print('*'+(' '*((numero*2)-3)+'*'))
print("\na.- Rombo:\n")
for i in range(1, numero+1):    
    if i==1:
        print(' '*(numero-i)+'*'*i)
    elif i==numero:
        print('* '+' '*((numero*2)-4)+'* ')
    else:
        print(' '*(numero-i)+('*')+(' '*((i*2)-3))+'*')
for i in range(numero-1, 0, -1):    
    if i==1:
        print(' '*(numero-i)+'*'*i)
    elif i==numero:
        print('* '+' '*((numero*2)-4)+'* ')
    else:
        print(' '*(numero-i)+('*')+(' '*((i*2)-3))+'*')
print("\na.- Tringulo:\n")
for i in range(1, numero+1):    
    if i==1:
        print(' '*(numero-i)+'*'*i)
    elif i==numero:
        print('*'*((numero+i)-1))
    else:
        print(' '*(numero-i)+('*')+(' '*((i*2)-3))+'*')
