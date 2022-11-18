'''
4.- Existen cuatro grupos sanguíneos en seres humanos, que se multiplican por dos si
consideramos el factor Rh. Unos grupos son compatibles con otros atendiendo al
criterio que podemos ver en las siguientes tablas.
Grupo Dona a Recibe de Rh Dona a Recibe de
A A, AB A, 0 + + +, -
B B, AB B, 0 - +, - -
AB AB A, B, AB, 0
0 A, B, AB, 0 0
Elabora un programa que reciba dos grupos sanguíneos y devuelva si son
compatibles y en qué sentido.
Por ejemplo, si se recibe A y B debería decir que no son compatibles.
Por el contrario, si se recibe 0 y AB debería indicar que son compatibles y AB es
receptor de 0.

Rafael Garcia Benitez
'''

grupo1=input("Inotroduce el primrer grupo sanguineo A, B, AB o 0:")
rh1=input("Introduce el primer Rh + o -:")
grupo2=input("Inotroduce el segundo grupo sanguineo A, B, AB o 0:")   
rh2=input("Introduce el segundo Rh + o -:")

if rh1=="+" and rh2=="+":
    if grupo1=="A" and grupo2=="A":
        print("Son compatibles, A+ es receptor/donador de A+")
    elif grupo1=="A" and grupo2=="AB":
        print("Son compatibles, A+ es donador de AB+")
    elif grupo1=="A" and grupo2=="0":
        print("Son compatibles, A+ es receptor de 0+")
    if grupo1=="B" and grupo2=="B":
        print("Son compatibles, B+ es receptor/donador de B+")
    elif grupo1=="B" and grupo2=="AB":
        print("Son compatibles, B+ es donador de AB+")
    elif grupo1=="B" and grupo2=="0":
        print("Son compatibles, B+ es receptor de 0+")    
    if grupo1=="AB" and grupo2=="AB":
        print("Son compatibles, AB+ es receptor/donador de AB+")
    elif grupo1=="AB" and grupo2=="A":
        print("Son compatibles, AB+ es receptor de A+")
    elif grupo1=="AB" and grupo2=="B":
        print("Son compatibles, AB+ es receptor de B+")
    elif grupo1=="AB" and grupo2=="0":
        print("Son compatibles, AB+ es receptor de 0+")
    if grupo1=="0" and grupo2=="0":
        print("Son compatibles, 0+ es receptor/donador de 0+")
    elif grupo1=="0" and grupo2=="A":
        print("Son compatibles, 0+ es donador de A+")
    elif grupo1=="AB" and grupo2=="B":
        print("Son compatibles, 0+ es donador de B+")
    elif grupo1=="0" and grupo2=="AB":
        print("Son compatibles, 0+ es donador de AB+")
elif rh1=="-" and rh2=="-":
    if grupo1=="A" and grupo2=="A":
        print("Son compatibles, A- es receptor/donador de A-")
    elif grupo1=="A" and grupo2=="AB":
        print("Son compatibles, A- es donador de AB-")
    elif grupo1=="A" and grupo2=="0":
        print("Son compatibles, A- es receptor de 0-")
    if grupo1=="B" and grupo2=="B":
        print("Son compatibles, B- es receptor/donador de B-")
    elif grupo1=="B" and grupo2=="AB":
        print("Son compatibles, B- es donador de AB-")
    elif grupo1=="B" and grupo2=="0":
        print("Son compatibles, B- es receptor de 0-")
    if grupo1=="AB" and grupo2=="AB":
        print("Son compatibles, AB- es receptor/donador de AB-")
    elif grupo1=="AB" and grupo2=="A":
        print("Son compatibles, AB- es receptor de A-")
    elif grupo1=="AB" and grupo2=="B":
        print("Son compatibles, AB- es receptor de B-")
    elif grupo1=="AB" and grupo2=="0":
        print("Son compatibles, AB- es receptor de 0-")
    if grupo1=="0" and grupo2=="0":
        print("Son compatibles, 0- es receptor/donador de 0-")
    elif grupo1=="0" and grupo2=="A":
        print("Son compatibles, 0- es donador de A-")
    elif grupo1=="AB" and grupo2=="B":
        print("Son compatibles, 0- es donador de B-")
    elif grupo1=="0" and grupo2=="AB":
        print("Son compatibles, 0- es donador de AB-")
elif rh1=="+" and rh2=="-":
    if grupo1=="A" and grupo2=="A":
        print("Son compatibles, A+ es receptor de A-")
    elif grupo1=="A" and grupo2=="0":
        print("Son compatibles, A+ es receptor de 0-")
    if grupo1=="B" and grupo2=="B":
        print("Son compatibles, B+ es receptor de B-")
    elif grupo1=="B" and grupo2=="0":
        print("Son compatibles, B+ es receptor de 0-")
    if grupo1=="AB" and grupo2=="AB":
        print("Son compatibles, AB+ es receptor de AB-")
    elif grupo1=="AB" and grupo2=="A":
        print("Son compatibles, AB+ es receptor de A-")
    elif grupo1=="AB" and grupo2=="B":
        print("Son compatibles, AB+ es receptor de B-")
    elif grupo1=="AB" and grupo2=="0":
        print("Son compatibles, AB+ es receptor de 0-")
    if grupo1=="0" and grupo2=="0":
        print("Son compatibles, 0+ es receptor de 0-")
elif rh1=="-" and rh2=="+":
    if grupo1=="A" and grupo2=="A":
        print("Son compatibles, A- es donador de A+")
    elif grupo1=="A" and grupo2=="AB":
        print("Son compatibles, A- es donador de AB+")
    if grupo1=="B" and grupo2=="B":
        print("Son compatibles, B- es donador de B+")
    elif grupo1=="B" and grupo2=="AB":
        print("Son compatibles, B- es donador de AB+")
    if grupo1=="AB" and grupo2=="AB":
        print("Son compatibles, AB- es donador de AB+")
    if grupo1=="0" and grupo2=="0":
        print("Son compatibles, 0- es donador de 0+")
    elif grupo1=="0" and grupo2=="A":
        print("Son compatibles, 0- es donador de A+")
    elif grupo1=="AB" and grupo2=="B":
        print("Son compatibles, 0* es donador de B+")
    elif grupo1=="0" and grupo2=="AB":
        print("Son compatibles, 0- es donador de AB+")
else:
    print("No son compatibles")
