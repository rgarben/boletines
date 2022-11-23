'''
5. Realizar un programa que solicite 4 números e imprima la media de los
números. También debe imprimir aquellos números que son superiores a la
media.

Rafael García Benítez
'''

num1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))
num4 = int(input("Introduce un numero: "))
media = (num1+num2+num3+num4)/4
print("La media es: ",media)
if num1>media:
    print("El numero %s es mayor que la media %s"%(num1,media))
if num2>media:
    print("El numero %s es mayor que la media %s"%(num2,media))
if num3>media:
    print("El numero %s es mayor que la media %s"%(num3,media))
if num4>media:
    print("El numero %s es mayor que la media %s"%(num4,media))