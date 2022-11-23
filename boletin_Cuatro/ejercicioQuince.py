'''
15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error.

Rafael García Benítez
'''

dia = int(input("Introduce el numero del dia de la semana: "))

if dia == 1:
    print("Es lunes.")
elif dia == 2:
    print("Es martes.")
elif dia == 3:
    print("Es miercoles.")
elif dia == 4:
    print("Es jueves.")
elif dia == 5:
    print("Es viernes.")
elif dia == 6:
    print("Es sabado.")
elif dia == 7:
    print("Es domingo.")
else:
    print("Error: introduce un numero de la semana del 1 al 7.")