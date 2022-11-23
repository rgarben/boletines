'''
9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
◦ El exponente sea 0, el resultado es 1.
◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.

Rafael García Benítez
'''

base = int(input("Introduce numero base: "))
exponente= int(input("Introduce numero del exponente: "))

if exponente >=0:
    print("La potencia es:", base**exponente)


elif exponente<0:
    print("El resultado es: 1/", (base**-exponente))