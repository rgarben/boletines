'''
Rafael García Benítez  1º DAW B
'''

tamanio = int(input("Introduce tamaño de la empreza: "))
contarPython = 0
contarJava = 0
contarHombreJava = 0
contarHombrePython = 0
contarMujerJava = 0
contarMujerPython = 0
contador = 0
contarEmpleados = 0
contarEdadPython = 0
contarEdadJava = 0

while tamanio <=0:
    tamanio = int(input("Error introduce tamaño de la empreza mayor que 0: "))
while contador<=tamanio:
    edad = int(input("Introduce tu edad: "))
    contarEmpleados+=1
    while edad < 18 or edad >65:
        edad = int(input("Error introduce una edad entre 18/65 años: "))
    sexo = input("Introduce tu sexo H/M: ")
    while sexo!='H' and sexo!='M':
        sexo = input("Error introduce tu sexo H/M: ")
    lenguaje = input("Introduce tu lenguaje python o java: ")
    while lenguaje!='python' and lenguaje!='java':
        lenguaje = input("Error introduce tu sexo H/M: ")
    if sexo=='H':
        if lenguaje=='python':
            contarHombrePython+=1
            contarPython+=1
            contarEdadPython+=edad
        elif lenguaje=='java':
            contarHombreJava+=1
            contarJava+=1
            contarEdadJava+=edad
    elif sexo=='M':
        if lenguaje=='python':
            contarMujerPython+=1
            contarPython+=1
            contarEdadPython+=edad
        elif lenguaje=='java':
            contarMujerJava+=1
            contarJava+=1
            contarEdadJava+=edad
    print(f"El {(contarPython/20)*100} % de empleados utiliza python, de los que {contarHombrePython} son hombres y {contarMujerPython} mujeres y su edad media {contarEdadPython/tamanio}.")
    print(f"El {(contarJava/20)*100} % de empleados utiliza python, de los que {contarHombreJava} son hombres y {contarMujerJava} mujeres y su edad media {contarEdadJava/tamanio}.")
    
    
    