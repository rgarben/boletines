'''
3. Crea un programa que dada una fecha en formato (dd-mm-yyyy), nos devuelva
cuántos días han transcurrido desde el 1 de enero de ese mismo año (considera que
puede tratarse de un año bisiesto).

Rafael Garcia Benitez
'''

dia = int(input("Introduce un dia del mes 1 al 31: "))
mes = int(input("Introduce un mes del 1 al 12: "))
año = int(input("Introduce un año: "))

if not año%4 and (año%100 or not año%400):
    if mes==1:
        print(f"Pasaron {dia} dias.")
    elif mes==2:
        suma=31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==3:
        suma=31+29+dia
        print(f"Pasaron {suma} dias.")
    elif mes==4:
        suma=31+29+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==5:
        suma=31+29+31+30+dia
        print(f"Pasaron {suma} dias.")
    elif mes==6:
        suma=31+29+31+30+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==7:
        suma=31+29+31+30+31+30+dia
        print(f"Pasaron {suma} dias.")
    elif mes==8:
        suma=31+29+31+30+31+30+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==9:
        suma=31+29+31+30+31+30+31+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==10:
        suma=31+29+31+30+31+30+31+31+30+dia
        print(f"Pasaron {suma} dias.")
    elif mes==11:
        suma=31+29+31+30+31+30+31+31+30+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==12:
        suma=31+29+31+30+31+30+31+31+30+31+30+dia
        print(f"Pasaron {suma} dias.")
elif año%4 and (año%100 or not año%400):
    if mes==1:
        print(f"Pasaron {dia} dias.")
    elif mes==2:
        suma=31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==3:
        suma=31+28+dia
        print(f"Pasaron {suma} dias.")
    elif mes==4:
        suma=31+28+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==5:
        suma=31+28+31+30+dia
        print(f"Pasaron {suma} dias.")
    elif mes==6:
        suma=31+28+31+30+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==7:
        suma=31+28+31+30+31+30+dia
        print(f"Pasaron {suma} dias.")
    elif mes==8:
        suma=31+28+31+30+31+30+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==9:
        suma=31+28+31+30+31+30+31+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==10:
        suma=31+28+31+30+31+30+31+31+30+dia
        print(f"Pasaron {suma} dias.")
    elif mes==11:
        suma=31+28+31+30+31+30+31+31+30+31+dia
        print(f"Pasaron {suma} dias.")
    elif mes==12:
        suma=31+28+31+30+31+30+31+31+30+31+30+dia
        print(f"Pasaron {suma} dias.")
else:
    print("Dia no valido.")
