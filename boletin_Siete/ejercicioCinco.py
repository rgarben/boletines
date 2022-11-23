'''
5. La secuencia siguiente está definida para el conjunto de los números enteros:
n → n/2 (n es par)
n → 3n + 1 (n es impar)
Utilizando la función anterior y empezando en 13 se genera la siguiente secuencia
de números:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Esta secuencia tiene 10 términos y se cree que cualquier secuencia termina en 1.
Elabora un programa que pida un número n e imprima una cadena con la secuencia
de números hasta llegar a 1.

Rafael Garcia Benitez
'''

empieza = int(input("Introduce numero para la secuencia: "))
linea = " "
numero=empieza
while numero!=1:
    if numero%2==0:
        numero=numero//2
        linea+=", "+str(numero)
    else:
        numero=(3*numero)+1
        linea+=", "+str(numero)
print(f"La secuencia es: {empieza}"+ linea)


empieza = int(input("Introduce numero para la secuencia: "))
lista=[]
numero=empieza
while numero!=1:
    if numero%2==0:
        numero=numero//2
        lista.append(numero)
    else:
        numero=(3*numero)+1
        lista.append(numero)
print("pasar saber cuando mide la cadena", len(lista))
print(f"{empieza} => "+ str(lista))
