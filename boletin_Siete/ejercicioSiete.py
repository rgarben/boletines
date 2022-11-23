'''
7. Triángulos. Escribe un programa que pida un número y a continuación pinte un
triángulo como los siguientes utilizando el número como símbolo.

Rafael Garcia Benitez
'''

numero = int(input("Introduce un numero para el triangulo de numeros: "))
espacio=""

for i in range(0, numero):
    espacio+=" "+str(numero)
    print(espacio)