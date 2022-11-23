'''
7. Realizar un programa que lea el estado civil de una persona (S-Soltero, C-
Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
siguientes reglas:
 A los solteros o divorciados menores de 35 años, un 12%
 Todas las personas mayores de 50 años, un 8.5%
 A los viudos o casados menores de 35 años, un 11.3%
 Al resto de casos se le aplica un 10.5%

Rafael García Benítez
'''

estadoCivil = input("Introduce tu estado civil: ")
edad = int(input("Introduce tu edad: "))

if edad < 35:
    if estadoCivil == 'S' or estadoCivil == 'D':
        print("Tu retención es un 12%")
    elif estadoCivil=='V' or estadoCivil=='C':
        print("Tu retención es un 11.3%")
elif edad > 50:
    print("Tu retencion es del 8.5%")
else:
    print("Tu retención es del 10,5%")