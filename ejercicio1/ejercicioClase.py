'''
 En el gimnasio Jacafitness tienen el siguiente horario: 
 
 Los Lunes, Miércoles y Viernes imparten Spinning de 12 a 14, Yoga de 16 a 20 y Body combat de 20 a 22; 
 Los Martes y Jueves La sesión de Spinning y Yoga se intercambian.

Elabora un programa que dé la bienvenida al gimnasio Jacafitness y tras p
reguntar por la hora y el día de la semana te indique la actividad que puedes realizar.
'''
print("Bienvenido a Jacafitness.")
dia = str(input("Introduce dia de la semana Lunes, Martes, Miercoles, Jueves y Viernes: "))
hora = int(input("Introduce hora: "))

if dia == 'Lunes' or dia == 'Miercoles' or dia == 'Viernes' and 12<=hora<=14:
    print("Puedes realizar Spinning de 12 a 14")
elif dia == 'Lunes' or dia == 'Miercoles' or dia == 'Viernes' and 16<=hora<=20:
    print("Puedes realizar Yoga de 16 a 20")
elif dia == 'Lunes' or dia == 'Miercoles' or dia == 'Viernes' and 20<=hora<=22:
    print("Puedes realizar Body combat de 20 a 22")
elif dia == 'Martes' or dia == 'Jueves' and 12<=hora<=14:
    print("Puedes realizar Yoga de 12 a 14")
elif dia == 'Martes' or dia == 'Jueves' and 16<=hora<=20:
    print("Puedes realizar Spinning de 16 a 20")
elif dia == 'Martes' or dia == 'Jueves' and 20<=hora<=22:
    print("Puedes realizar Body combat de 20 a 22")
else:
    print("El gimnasio Jacafitness esta cerrado.")