'''
8. Realizar un programa que lea por teclado dos marcaciones de un reloj
digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
23:59:59 e informe cual de ellas es mayor.
Ejemplo:
Hora 1: 12:35:37
Hora 2: 12:38:36
“Hora 2 es mayor”

Rafael García Benítez
'''

hora = int(input("Introduce la primera hora: "))
minutos = int(input("Introduce los primeros minutos: "))
segundos = int(input("Introduce los segundos primeros: "))
hora1 = int(input("Introduce la segunda hora: "))
minutos1 = int(input("Introduce los segundos minutos: "))
segundos1 = int(input("Introduce los segundos segundos: "))

print("Hora 1: %s:%s:%s"%(hora,minutos,segundos))
print("Hora 2: %s:%s:%s"%(hora1,minutos1,segundos1))

if hora > hora1:
    print("La hora 1 es mayor")
elif hora1 > hora:
    print("La hora 2 es mayor")
elif hora == hora1:
    if minutos > minutos1:
        print("La hora 1 es mayor")
    elif minutos1 > minutos:
        print("La hora 2 es mayor")
    elif minutos == minutos1:
        if segundos > segundos1:
            print("La hora 1 es mayor")
        elif segundos1 > segundos:
            print("La hora 2 es mayor")