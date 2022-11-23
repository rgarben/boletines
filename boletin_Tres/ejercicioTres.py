'''
3. Realizar un programa que lea un número por teclado. El programa debe
imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
el programa finaliza sin mostrar ningún mensaje.

Rafael García Benítez
'''

numero = int(input("Introduce un numero: "))

if numero%2==0 and numero%3==0:
    print("Es multiplo de 2 y es multiplo de 3")
elif numero%3==0:
    print("Es multiplo de 3")
elif numero%2==0:
    print("Es multiplo de 2")
else:
    print("")