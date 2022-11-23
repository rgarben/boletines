'''
6. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano.
Calcula y muestra la distancia entre ellos.

Rafael García Benítez
'''

numx1 = int(input("Introduce el valor x del primer punto: "))
numy1 = int(input("Introduce el valor y del primer punto: "))
numx2 = int(input("Introduce el valor x del primer punto: "))
numy2 = int(input("Introduce el valor y del primer punto: "))

print("La distancia entre los dos puntos es:", ((numx2-numx1)^2 + (numy2-numy1)^2))