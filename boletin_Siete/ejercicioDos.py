'''
2. Diseñar un programa que pida dos números enteros y nos muestre los siguientes
números que son múltiplos del segundo introducido a partir del primero. Por ejemplo,
si introducimos:
13 y 7 ⇒ 14, 21, 28, 35, 42, 49, 56, 63, 70, 77
(a partir de 13 los siguientes 10 múltiplos de 7)

Rafael Garcia Benitez
'''

numero = int(input("Inserte un numero para empezar desde hay: "))
multiplo = int(input("Introduce el multiplo: "))
contador=0
rango=numero
linea=" "
while contador<10:
    rango+=1
    if rango%multiplo==0:
        contador+=1
        linea+=str(rango)+", "
        if contador==10:
            linea+=str(rango)
print(f"Empieza desde el {numero} y el multiplo es {multiplo} => {linea}")