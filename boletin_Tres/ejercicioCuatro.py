'''
4. Realizar un programa que lea la edad de una persona menor a 100 años e
informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
29) o un adulto.

Rafael García Benítez
'''

edad = int(input("Introduce tu edad: "))

if edad < 100:
    if edad <=12 and edad >=0:
        print("Eres un niño")
    elif edad <=17 and edad >=13:
        print("Eres adolescente")
    elif edad <=29 and edad >=17:
        print("Eres un joven adulto")
elif edad <=100 and edad >=30:
    print("Eres un adulto")
else:
    print("Error: introduce un numero comprendido entre 0 y 100")