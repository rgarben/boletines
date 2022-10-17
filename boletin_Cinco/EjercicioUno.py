'''
1. Escribe el código de un programa que reciba un número de nota de 0 a 100 y nos
informe de las calificaciones en el siguiente formato:
90-100, Sobresaliente
70-89, Notable
60-69, Bien
50-59, Suficiente
0-49, Suspens
'''

nota = int(input("Introduce la nota: "))

if 100 >= nota >= 90:
    print("Tu no ta es Sobresaliente.")
elif 89 >= nota >= 70:
    print("Tu no ta es Notable.")
elif 69 >= nota >= 60:
    print("Tu no ta es Bien.")
elif 59 >= nota >= 50:
    print("Tu no ta es Suficiente.")
elif 49 >= nota >= 0:
    print("Tu no ta es Suspenso.")
else:
    print("Error introduce una nota comprendida ente 0 y 100.")