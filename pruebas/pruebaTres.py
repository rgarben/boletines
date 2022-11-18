'''
rafael garcia benitez
'''

peso = float(input("Introduce tu peso: "))

while peso!=0:
    edad = int(input("Introduce tu edad: "))
    tipoVida = input("Introduce tu tipo de vida 'S'edentaria/'A'ctiva/'M'uy activa: ")
    while peso<0 or peso >=180:
        peso = int(input("Error: Introduce un peso entre 10 y 180: "))
    while tipoVida=='S' and tipoVida=='A' and tipoVida=='M':
        tipoVida = input("Error: Introduce un tipo de vida 'S'edentaria/'A'ctiva/'M'uy activa: ")
    while edad<=0:
        edad = int(input("Error: Introduce una edad positiva: "))
    if (peso>100) or (edad>70 and tipoVida=='S') or (peso>74.4 and edad>50):
        print("Te recomendamos ir al medico.")  
    else:
        print("No es urgente que acuda al médico si no tiene problemas de salud.")
    peso = float(input("Introduce 0 para terminar el programa o vuelva a introducir un peso: "))
print("Programa terminado.")