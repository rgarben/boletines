'''
3. Design a method called computeDaysInMonth that returns the number of days for
the month and year that are received as arguments. You may use the method
leapYear above. If the values are not valid the method should return -1.

Rafael García Bennítez
'''

mes = int(input("Introduce el numero del mes: "))
anio = int(input("Introduce el año: "))

def computeDaysInMonth (month, year):
    dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    diass=dias[month-1]
    if (mes==1) and (year%4==0 and (year%100!=0 or year%400==0)):
        diass=28
    elif month < 0 or year < 400:
        return None
    return diass
print(f"El mes tiene {computeDaysInMonth(mes,anio)}")