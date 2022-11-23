'''
10. Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los
lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo en
cuenta los siguiente:
◦ Si se cumple Pitágoras entonces es triángulo rectángulo
◦ Si sólo dos lados del triángulo son iguales entonces es isósceles.
◦ Si los 3 lados son iguales entonces es equilátero.
◦ Si no se cumple ninguna de las condiciones anteriores, es escaleno.

Rafael García Benítez
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