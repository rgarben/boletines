'''
16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente.

Rafael García Benítez
'''

mes = int(input("Introduce el numero del mes: "))

if mes == 1:
    print("El mes de enero tiene 31 dias.")
elif mes == 2:
    print("El mes de febrero tiene 28 dias.")
elif mes == 3:
    print("El mes de marzo tiene 31 dias.")
elif mes == 4:
    print("El mes de abril tiene 30 dias.")
elif mes == 5:
    print("El mes de mayo tiene 31 dias.")
elif mes == 6:
    print("El mes de junio tiene 30 dias.")
elif mes == 7:
    print("El mes de julio tiene 31 dias.")
elif mes == 8:
    print("El mes de agosto tiene 31 dias.")
elif mes == 9:
    print("El mes de septiembre tiene 30 dias.")
elif mes == 10:
    print("El mes de octubre tiene 31 dias.")
elif mes == 11:
    print("El mes de noviembre tiene 30 dias.")
elif mes == 12:
    print("El mes de diciembre tiene 31 dias.")
else:
    print("Error: introduce un numero del mes del 1 al 12.")