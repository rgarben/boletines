'''
1. Realizar un programa que lea un número entero por teclado e informe de si
el número es par o impar (el cero se considera par).
'''
'''
numero = int(input("Introduce un numero: "))

if numero%2==0:
    print("El numero %s es par"%(numero))
else:
    print("El numero %s no es par"%(numero))
'''
'''
2. Realizar un programa que solicite dos números por teclado e imprima en
pantalla si son iguales, el primero mayor que el segundo o el primero más
pequeño que el segundo.
'''
'''
num1 = int(input("Introduce el primero numero: "))
num2 = int(input("Introduce el segundo numero: "))

if num1==num2:
    print("El numero %s y el numero %s son iguales."%(num1,num2))
elif num1>num2:
    print("El numero %s es mayor que el numero %s."%(num1,num2))
else:
    print("El numero %s es mas pequeño que el numero %s."%(num1,num2))
'''
'''
3. Realizar un programa que lea un número por teclado. El programa debe
imprimir en pantalla un mensaje con “El número xx es múltiplo de 2” o un
mensaje con “El número xx es múltiplo de 3”. Si es múltiplo de 2 y de 3
deben aparecer los dos mensajes. Si no es múltiplo de ninguno de los dos
el programa finaliza sin mostrar ningún mensaje.
'''
'''
numero = int(input("Introduce un numero: "))

if numero%2==0 and numero%3==0:
    print("Es multiplo de 2 y es multiplo de 3")
elif numero%3==0:
    print("Es multiplo de 3")
elif numero%2==0:
    print("Es multiplo de 2")
else:
    print("")
'''
'''
4. Realizar un programa que lea la edad de una persona menor a 100 años e
informe de si es un niño (0-12 años), un adolescente (13-17), un joven (18-
29) o un adulto.
'''
'''
edad = int(input("Introduce tu edad: "))

if edad < 100:
    if edad <=12 and edad >=0:
        print("Eres un niño")
    elif edad <=17 and edad >=13:
        print("Eres adolescente")
    elif edad <=29 and edad >=17:
        print("Eres un joven adulto")
elif edad <=100 and edad >=30:
    print("Eres un adulto")
else:
    print("Error: introduce un numero comprendido entre 0 y 100")
'''
'''
5. Realizar un programa que solicite 4 números e imprima la media de los
números. También debe imprimir aquellos números que son superiores a la
media.
'''
'''
nnum1 = int(input("Introduce un numero: "))
num2 = int(input("Introduce un numero: "))
num3 = int(input("Introduce un numero: "))
num4 = int(input("Introduce un numero: "))
media = (num1+num2+num3+num4)/4
print("La media es: ",media)
if num1>media:
    print("El numero %s es mayor que la media %s"%(num1,media))
if num2>media:
    print("El numero %s es mayor que la media %s"%(num2,media))
if num3>media:
    print("El numero %s es mayor que la media %s"%(num3,media))
if num4>media:
    print("El numero %s es mayor que la media %s"%(num4,media))
'''
'''
6. Realizar un programa que solicite un carácter por teclado e informe por
pantalla si el carácter es una vocal o no lo es. Si es una vocal mostrará el
mensaje “Es la primera vocal (A)” o “Es la segunda vocal (E)”, etc.
'''
'''
caracter = input("Dime una letra: ")

if caracter == 'A' or caracter == 'a':
    print("Es la primera vocal.")
elif  caracter == 'E' or caracter == 'e':
    print("Es la segunta vocal.")
elif caracter == 'I' or caracter == 'i':
    print("Es la tercera vocal.")
elif caracter == 'O' or caracter == 'o':
    print("Es la cuarta vocal.")
elif caracter == 'U' or caracter == 'u':
    print("Es la quinta vocal.")
else:
    print("No es vocal")
'''
'''
7. Realizar un programa que lea el estado civil de una persona (S-Soltero, C-
Casado, V-Viudo y D-Divorciado) y su edad. Después debe mostrar por
pantalla el porcentaje de retención que debe aplicársele de acuerdo con las
siguientes reglas:
 A los solteros o divorciados menores de 35 años, un 12%
 Todas las personas mayores de 50 años, un 8.5%
 A los viudos o casados menores de 35 años, un 11.3%
 Al resto de casos se le aplica un 10.5%
'''
'''
estadoCivil = input("Introduce tu estado civil: ")
edad = int(input("Introduce tu edad: "))

if edad < 35:
    if estadoCivil == 'S' or estadoCivil == 'D':
        print("Tu retención es un 12%")
    elif estadoCivil=='V' or estadoCivil=='C':
        print("Tu retención es un 11.3%")
elif edad > 50:
    print("Tu retencion es del 8.5%")
else:
    print("Tu retención es del 10,5%")
'''
'''
8. Realizar un programa que lea por teclado dos marcaciones de un reloj
digital (horas, minutos, segundos) comprendidas entre las 0:0:0 y las
23:59:59 e informe cual de ellas es mayor.
Ejemplo:
Hora 1: 12:35:37
Hora 2: 12:38:36
“Hora 2 es mayor”
'''
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
'''
'''
9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
porcentaje de rebaja que se aplicará sobre el precio original del producto se
calcula de la siguiente forma:
 Si el producto es de tipo A, independientemente de su precio se
aplica un 7% de descuento.
 Si el producto es de tipo C o bien el precio es inferior a 500€ se
aplicará un porcentaje del 12% de descuento.
 En el resto de casos se aplica un 9% de descuento.
Realizar un programa que solicite los datos necesarios (tipo de producto y
precio original) y calcule el precio rebajado. Debe comprobarse que los
datos de entrada son correctos, y si no lo son mostrar un mensaje de error.
'''
'''
producto = str(input("Introduce un producto A, B o C: "))
precio = int(input("Introduce un precio: "))

if producto == 'A':
    print(precio-(precio*0.07))
elif producto == 'C' or precio < 500:
    print(precio-(precio*0.12))
elif producto == 'B':
    print(precio-(precio*0.09))
else:
    print("Error, introduce los productos A, B o c.")
'''
'''
10.Realizar un programa que lea un carácter y dos números enteros por
teclado. Si el carácter leído es un operador aritmético, calcular la operación
correspondiente, si es cualquier otro debe mostrar un error.
'''
'''
caracter = str(input("Introduce un caracter +, -, *, /: "))
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
if caracter == '+':
    print("La suma es:", num1+num2)
elif caracter == '-':
    print("La resta es:", num1-num2)
elif caracter == '*':
    print("La la multiplicación es:", num1*num2)
elif caracter == '/':
    print("La division es:", num1/num2)
else:
    print("Error, introduce operaciones +, -, *, /.")
'''