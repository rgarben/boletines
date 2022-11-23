'''
3. Diseñar un programa que muestre, para cada número introducido por teclado, si es
par, si es positivo y su cuadrado. El proceso se repetirá hasta que el número
introducido por teclado sea 0. Por ejemplo:
4 ⇒ es par, positivo y su cuadrado es 16
-7 ⇒ es impar, negativo y su cuadrado es 49

Rafael Garcia Benitez
'''

numero=int(input("Introduce un numero para saber si es par, positivo y su cuadrado: "))


while numero!=0:
    espacio=""
    if numero%2==0:
        espacio+="Es par, "
    else:
        espacio+="Es impar, "
    if numero>=0:
        espacio+="es Positivo y"
    else:
        espacio+="es Negativo y"
    print(f"{espacio} su cuadrado es {numero**2}:")
    numero=int(input("Introduce un numero para saber si es par, positivo y su cuadrado: "))