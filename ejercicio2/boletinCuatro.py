
'''
1. Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
'''

'''
cateto1 = int(input("Introduce primer cateto: "))
cateto2 = int(input("Introduce segundo cateto: "))

print("La hipotenusa es:", (cateto1**2+cateto2**2)**0.5)
'''
'''
2. Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
'''
'''
grados = int(input("Introduce un grado farenheit: "))

print("En grados Celsius es:", (grados-32)*5/9)
'''
'''
3. Calcular la media de tres números pedidos por teclado
'''
'''
num = int(input("Introduce el primer numero: "))
num1 = int(input("Introduce el segundo numero: "))
num2 = int(input("Introduce el tercer numero: "))

print("La media es:", (num+num1+num2)/3)
'''
'''
4. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
cuanto deberá pagar finalmente por su compra.
'''
'''
total = int(input("Introduce el total de la compra: "))

print("El total de la compra menos el 15% es:", total-(total*0.15))
'''
'''
5. Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su
diferencia, de modo que el resultado sea siempre positivo).
'''
'''
num = int(input("Introduce el primer numero: "))
num1 = int(input("Introduce el segundo numero: "))
print (abs(num-num1))
'''
'''
6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos.
'''
'''
numx1 = int(input("Introduce el valor x del primer punto: "))
numy1 = int(input("Introduce el valor y del primer punto: "))
numx2 = int(input("Introduce el valor x del primer punto: "))
numy2 = int(input("Introduce el valor y del primer punto: "))

print("La distancia entre los dos puntos es:", ((numx2-numx1)^2 + (numy2-numy1)^2))
'''
'''
7. Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.
Python no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿cómo se
puede calcular?
'''
'''
num = int(input("Introduce un numero: "))

print("La raiz cuadrada es:", (num**0.5),"y la raíz cúbica es:", (num**0.3))
'''
'''
8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).
'''
'''
dosEuros = int(input("Introduce monedas de 2 euros: "))
unEuro = int(input("Introduce monedas de 1 euro: "))
cincuenta = int(input("Introduce monedas de 50 centimos: "))
veinte = int(input("Introduce monedas de 20 centimos: "))
diez = int(input("Introduce monedas de 10 centimos: "))
calcularEuros = ((cincuenta*50)+(veinte*20)+(diez*10))//100
calcularCentimos = ((dosEuros*200)+(unEuro*100))+calcularEuros

print("Tienes:", calcularEuros,"en euros y en centimos", calcularCentimos)
'''
'''
9. Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el
exponente. Pueden ocurrir tres cosas:
◦ El exponente sea positivo, sólo tienes que imprimir la potencia.
◦ El exponente sea 0, el resultado es 1.
◦ El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
'''
'''
base = int(input("Introduce numero base: "))
exponente= int(input("Introduce numero del exponente: "))

if exponente >=0:
    print("La potencia es:", base**exponente)


elif exponente<0:
    print("El resultado es: 1/", (base**-exponente))
'''
'''
10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.
'''
'''
lado1 = int(input("Introduce lado A: "))
lado2 = int(input("Introduce lado B: "))
lado3 = int(input("Introduce lado C: "))

if lado1**2+lado2**2==lado3**2 or lado1**2+lado3**2==lado2**2 or lado2**2+lado3**2==lado1**2:
    print("Es un triangulo rectángulo.")
elif lado1+lado2==lado3 or lado1+lado3==lado2 or lado2+lado3==lado1:
    print("Es un triangulo isósceles.")
elif lado1==lado2==lado3:
    print("Es un triangulo equilátero")
else:
    print("Es un triangulo escaleno")
'''
'''
11. Escribir un programa que lea un año indicar si es bisiesto. Nota: un año es bisiesto si es un
número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible
por 400.
'''
'''
año = int(input("Introduce año para ver si es bisiesto: "))

if año%4==0 or (año%400==0 and año%100!=0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")
'''
'''
12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
'''
'''
tipo = str(input("Introduce el tipo A o B: "))
tamaño = int(input("Introduce un tamaño 1 o 2: "))

if tipo=='A' and tamaño == 1:
    print("Se le cargaran 20 centimos mas al precio inicial")
elif tipo=='A' and tamaño == 2:
    print("Se le cargaran 30 centimos mas al precio inicial")
elif tipo=='B' and tamaño == 1:
    print("Se le rebaran 30 centimos mas al precio inicial")
elif tipo=='B' and tamaño == 2:
    print("Se le rebaran 50 centimos mas al precio inicial")
else:
    print("Error, introduce tipo entre A o B y tamaño 1 o 2.")
'''
'''
13. El director de una escuela está organizando un viaje de estudios, y requiere determinar
cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de viajes por el
servicio. La forma de cobrar es la siguiente: si son 100 alumnos o más, el costo por cada
alumno es de 65 euros; de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49, de 95 euros,
y si son menos de 30, el costo de la renta del autobús es de 4000 euros, sin importar el
número de alumnos. Realice un algoritmo que permita determinar el pago a la compañía de
autobuses y lo que debe pagar cada alumno por el viaje.
'''
'''
alumnos = int(input("Introduce el numero de alumnos: "))

if alumnos >= 100:
    print("El precio por alumno es 65 Euros.")
elif alumnos >=50 or alumnos <=99:
    print("El precio por alumno es 70 Euros.")
elif alumnos >=30 or alumnos <=49:
    print("El precio por alumno es 95 Euros.")
elif alumnos <=30:
    print("El precio por alumno es:", 4000/alumnos)
'''
'''
14. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.
'''
'''
minutos = int(input("Introduce numero de minutos de llamada: "))
turno = str(input("Introduce el turno , Domingo, Tarde o Mañana: "))

if 0<minutos <= 5 and turno== 'Domingo':
    print("La llamada costara:", (minutos*1)+((minutos*1)*0.03))
elif 0<minutos <= 5 and turno== 'Tarde':
    print("La llamada costara:", (minutos*1)+((minutos*1)*0.10))
elif 0<minutos <= 5 and turno== 'Mañana':
    print("La llamada costara:", (minutos*1)+((minutos*1)*0.15))
elif 5<minutos <= 8 and turno== 'Domingo':
    print("La llamada costara:", 5+((minutos-5)*0.80)+(((minutos-5)*0.80)*0.03))
elif 5<minutos <= 8 and turno== 'Tarde':
    print("La llamada costara:", 5+((minutos-5)*0.80)+(((minutos-5)*0.80)*0.10))
elif 5<minutos <= 8 and turno== 'Mañana':
    print("La llamada costara:", 5+((minutos-5)*0.80)+(((minutos-5)*0.80)*0.15))
elif 8<minutos <= 10 and turno== 'Domingo':
    print("La llamada costara:", 7.4+((minutos-8)*0.70)+(((minutos-8)*0.70)*0.03))
elif 8<minutos <= 10 and turno== 'Tarde':
    print("La llamada costara:", 7.4+((minutos-8)*0.70)+(((minutos-8)*0.70)*0.10))
elif 8<minutos <= 10 and turno== 'Mañana':
    print("La llamada costara:", 7.4+((minutos-8)*0.70)+(((minutos-8)*0.70)*0.15))
elif minutos > 10 and turno== 'Domingo':
    print("La llamada costara:", 8.8+((minutos-10)*0.50)+(((minutos-10)*0.50)*0.03))
elif minutos > 10 and turno== 'Tarde':
    print("La llamada costara:", 8.8+((minutos-10)*0.50)+(((minutos-10)*0.50)*0.10))
elif minutos > 10 and turno== 'Mañana':
    print("La llamada costara:", 8.8+((minutos-10)*0.50)+(((minutos-10)*0.50)*0.15))
else:
    print("Error, introduce minutos positivos y turnos Domingo, Mañana o Tarde.")
'''
'''
15. Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
correspondiente. Si introducimos otro número nos da un error.
'''
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
'''
'''
16. Escribe un programa que pida un número entero entre uno y doce e imprima el número de
días que tiene el mes correspondiente.
'''
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
'''





