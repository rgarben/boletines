

'''
1. Calcular el resultado de las siguientes expresiones lógicas:
a) 7>=27 AND NOT (7<=2)
b) 24>5 AND 10<=10 OR 10=5
c) (10>=15 OR 23=13) AND NOT(8=8)
d) NOT (6/3>3) OR 7>7
'''
'''
print("a)",7>=27 and not (7<=2))
print("b)",24>5 and 10<=10 or 10==5)
print("c)",(10>=15 or 23==13) and not(8==8))
print("d)",not (6/3>3) or 7>7)
'''
'''
2. Calcular el valor de las siguientes expresiones aritméticas:
a) 27 mod 4 + 15\4
b) 37\4^2–2
c) 9*2/3*10*3
d) (7*3–4*4)^2\4*2
'''
'''
print("a)",27%4+15/4, type(27%4+15/4))
print("b)",37/4**2-2, type(37/4**2-2))
print("c)",9*2/3*10*3, type(9*2/3*10*3))
print("d)",(7*3-4*4)**2/4*2, type((7*3-4*4)**2/4*2))
'''
'''
3. Escribir una expresión lógica que cumpla:
a) Debe ser Verdadera si el contenido de la variable entera precio es igual o superior a 60
euros pero igual o inferior a 420 euros.
b) Debe ser Verdadera si el numero contenido en la variable entera numero es impar.
c) Debe ser Verdadera si las dos variables enteras saldo de una cuenta, y dineroSacar son
válidas.
d) Debe ser Verdadera si las variables enteras hora y minutos son correctas, es decir, que
estén comprendidas entre 0:0 y 23:59.
e) Debe ser Verdadera si la variable estadoCivil que almacena el estado civil de una
persona no es correcta (S-Soltero, C-Casado, V-Viudo, D-Divorciado).
NOTA: Además siempre debe ser Falsa en el caso contrario al que se formula.
'''
'''
precio = 140
print(60<= precio and precio <=420)

print(precio%2==0)

saldo = 500
dineroSacar = 450

print(saldo >=0 and dineroSacar<=saldo and dineroSacar>0)

hora =22
minutos = 54

print((hora >=0 and minutos>=0) and (hora <=23 and minutos<=59))

estadoCivil = 'S'

print(not(estadoCivil== 'S' or estadoCivil== 'C' or estadoCivil== 'V' or estadoCivil== 'D'))
'''
'''
4. Escribir una expresión lógica que cumpla:
a) Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero
es superior a 300 euros o negativa.
b) Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22
años.
c) Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida.
d) Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.
NOTA: Además siempre debe ser Verdadera en el caso contrario al que se formula.
'''
cantidad = 300
sacar = 51

print(sacar <= cantidad and sacar >=0)

numero = 21

print(not(numero%7==0 or numero%3==0))

'''
5. Escribir la tabla de verdad para las siguientes expresiones lógicas:
a) (A OR B) AND NOT(A)
b) NOT (A OR B) AND B
c) A OR NOT (B)
d) NOT ((A AND B) AND (B OR A))
'''
'''
a=True
b=True
a1=True
b1=False
a2=False
b2=True
a3=False
b3=False
print("RELACION DE PROBLEMAS 1:")
print()
print("Ejercicio 5: Escribir la tabla de verdad para las siguientes expresiones lógicas:")
print()
print("Apartado a:  (A OR B) AND NOT(A)")
print()
print("Salida 1:",(a or b) and not(a))
print("Salida 2:",(a1 or b1) and not(a1))
print("Salida 3:",(a2 or b2) and not(a2))
print("Salida 4:",(a3 or b3) and not(a3))
print()
print("---------------------------")
print()
print("Apartado b: NOT (A OR B) AND B")
print()
print("Salida 1:",(not (a or b) and b))
print("Salida 2:",(not (a1 or b1) and b1))
print("Salida 3:",(not (a2 or b2) and b2))
print("Salida 4:",(not (a3 or b3) and b3))
print()
print("----------------------------")
print()
print("Apartado c: A OR NOT (B)")
print()
print("Salida 1:",(a or not (b)))
print("Salida 2:",(a1 or not (b1)))
print("Salida 3:",(a2 or not (b2)))
print("Salida 4:",(a3 or not (b3)))
print()
print("----------------------------")
print()
print("Apartado d: NOT ((A AND B) AND (B OR A))")
print()
print("Salida 1:",(not ((a and b) and (b or a))))
print("Salida 2:",(not ((a1 and b1) and (b1 or a1))))
print("Salida 3:",(not ((a2 and b2) and (b2 or a2))))
print("Salida 4:",(not ((a3 and b3) and (b3 or a3))))
'''

