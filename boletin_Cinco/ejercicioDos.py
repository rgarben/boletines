'''
2. Escribe una aplicación que pida la fecha actual (día y mes) y el hemisferio
(Norte/Sur) e indique en qué estación se encuentra:
a. Hemisferio Norte: Otoño (desde 23 Septiembre), Invierno (desde 21
diciembre), Primavera (desde 21 Marzo), Verano (desde 21 Junio).
b. Hemisferio Sur: Primavera (desde 23 Septiembre), Verano (desde 21
diciembre), Otoño (desde 21 Marzo), Invierno (desde 21 Junio).

Rafael Garcia Benitez
'''

hemisferio = input("Introduce el hemisferio norte/sur: ")
dia = int(input("Introduce el dia del mes: "))
mes = int(input("Introduce el mes: "))

if hemisferio == 'norte':
    if ((10 <= mes <=11) and (1 <= dia <= 30 )) or ((mes==9 and 23 <= dia <= 30) or (mes==12 and 1 <= dia <= 20)):
        print("Es la estación de Otoño")
    elif ((1 <= mes <=2) and (1 <= dia <= 30 )) or ((mes==12 and 21 <= dia <= 30) or (mes==3 and 1 <= dia <= 20)):
        print("Es la estación de Invierno")
    elif ((4 <= mes <=5) and (1 <= dia <= 30 )) or ((mes==3 and 21 <= dia <= 30) or (mes==6 and 1 <= dia <= 20)):
        print("Es la estación de Primavera")
    else:
        print("Es la estación de Verano")
if hemisferio == 'sur':
    if ((10 <= mes <=11) and (1 <= dia <= 30 )) or ((mes==9 and 23 <= dia <= 30) or (mes==12 and 1 <= dia <= 20)):
        print("Es la estación de Primavera")
    elif ((1 <= mes <=2) and (1 <= dia <= 30 )) or ((mes==12 and 21 <= dia <= 30) or (mes==3 and 1 <= dia <= 20)):
        print("Es la estación de Verano")
    elif ((4 <= mes <=5) and (1 <= dia <= 30 )) or ((mes==3 and 21 <= dia <= 30) or (mes==6 and 1 <= dia <= 20)):
        print("Es la estación de Otoño")
    else:
        print("Es la estación de Invierno")