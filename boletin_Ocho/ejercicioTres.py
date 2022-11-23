'''
3. Realiza un programa que solicite la fecha como tres datos numéricos (día, mes y
año) y muestre a continuación la fecha en formato largo.
Introduce el día de la fecha: 15
Introduce el mes de a fecha: 3
Introduce el año de a fecha: 2009
La fecha en formato largo es 15 de Marzo de 2009
Debe validar los datos y ejecutarse hasta que se introduzca un día negativo.

Rafael García Benítez
'''

dia = int(input("Introduce el dia: "))
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Obtrubre', 'Noviembre', 'Diciembre']
dias_maximo_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31]
def es_bisiesto(year):
    bisiesto = year%4==0 and (year%100!=0 or year%400==0)
    return (bisiesto)

while dia>=0:
    mes = int(input("Introduce el mes: "))
    while 1 > mes > 12:
        mes = int(input("Error: introduce un mes del 1/12: "))
    while 1 > dia > dias_maximo_por_mes[mes-1]:
        dia = int(input("Error: introduce un dia del 1/30: "))
    anio = int(input("Introduce el año: "))
    while 1950 > anio > 2022:
        anio = int(input("Error: introduce el año del 1950/2022: "))
    print("La fecha en formato largo es ", dia,"de ", (meses[mes-1]), "de ", anio)    
    dia = int(input("Introduce el dia: "))
print("Programa terminado.")