'''
4. Escribir una expresión lógica que cumpla:
a) Debe ser Falsa cuando la variable cantidad que contiene la cantidad a sacar de un cajero
es superior a 300 euros o negativa.
b) Debe ser Falsa si la persona es un adolescente, es decir, la variable edad está entre 16-22
años.
c) Debe ser Falsa si la variable respuesta a una pregunta de tipo (S/N) es válida.
d) Debe ser Falsa si el número contenido en la variable entera numero es múltiplo de 7 o de 3.
NOTA: Además siempre debe ser Verdadera en el caso contrario al que se formula.

Rafael García Benítez
'''


sacar = 74

print("a:", sacar <= 300 and sacar >=0)

edad = 27

print("b:", edad>=16 and edad<=22)

respuesta = 'P'

print("c:", respuesta != 'S' and respuesta != 'N')

numero = 21

print("d:", not(numero%7==0 or numero%3==0))