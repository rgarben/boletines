'''
6. Realizar un programa que solicite un carácter por teclado e informe por
pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.

Rafael García Benítez
'''

caracter = input("Dime una letra: ")

if caracter == 'A' or caracter == 'a':
    print("Es la primera vocal.")
elif  caracter == 'E' or caracter == 'e':
    print("Es la segunta vocal.")
elif caracter == 'I' or caracter == 'i':
    print("Es la tercera vocal.")
elif caracter == 'O' or caracter == 'o':
    print("Es la cuarta vocal.")
elif caracter == 'U' or caracter == 'u':
    print("Es la quinta vocal.")
else:
    print("No es vocal")
