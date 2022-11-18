'''

    1, 1, 2, 3, 5, 8, 13, 21, 34, 55

'''
rango = int(input("Catidad de numero: "))
numero = 1
numero2 = 0
contador = 1
while contador<=rango:
    contador+=1
    numero=numero2+numero
    numero2=numero+numero2
    print(numero)
    print(numero2)