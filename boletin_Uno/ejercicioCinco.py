'''
5. Escribir la tabla de verdad para las siguientes expresiones lógicas:
a) (A OR B) AND NOT(A)
b) NOT (A OR B) AND B
c) A OR NOT (B)
d) NOT ((A AND B) AND (B OR A))

Rafael García Benítez
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