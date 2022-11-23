'''
10. Diseña una función conversor que convierta un número de binario a decimal o de
decimal a binario. Esta función recibirá un número en formato de cadena de texto
cuya última posición indica el sistema numérico utilizado (D-decimal, B-binario).
Debe validar la información, así, por ejemplo, el número ‘1020101B’ no sería válido
puesto que los valores en binario son 0 y 1.

Rafael García Benítez
'''

numeroCadena = input("Introduce el numero decimal o binario para convertirlo 293D/10101B: ")

def listaPatras (lista):
    listaRever = []
    for i in range(len(lista),0,-1):
        listaRever.append(lista[i-1])
    return listaRever

while numeroCadena[-1]!='D' and numeroCadena[-1]!='B':
    numeroCadena = input("Error: introduce el numero decimal o binario terminado con D/B para convertirlo 293D/1011B: ")
while int(numeroCadena[0:-1]) < 0:
    numeroCadena = input("Error: introduce el numero decimal o binario positivo para convertirlo 293D/10101B: ")
if numeroCadena[-1]=='B':
    binario=numeroCadena[0:-1]
    binario=listaPatras(binario)
    suma=0
    contador = 0
    for elemento in binario:
        elemento=int(elemento)
        if elemento==1:
            multi=2**contador
            suma=multi+suma
        contador+=1
    print(f"{suma}D")
if numeroCadena[-1]=='D':
    decimal=int(numeroCadena[0:-1])
    guardarC=0
    guardarR=0
    guardarStr=""
    acabar=1
    numeroBinario=""
    while acabar>0:
        guardarC=decimal%2
        guardarR=decimal//2
        decimal=guardarR
        guardarStr+=str(guardarC)
        acabar=guardarR
    guardarStr=listaPatras(guardarStr)
    for i in range(len(guardarStr)):
        numeroBinario+=str(guardarStr[i])
    print(numeroBinario)
'''
numeroBinario = numeroCadena[0:-1]
for i in range (len(numeroBinario)):

    if contador==(len(numeroBinario)):
        print("Es binario")
    elif numeroBinario[i]=='0' or numeroBinario[i]=='1':
        contador+=1
    else:
        print("No es binario")
'''
    
'''
if numeroCadena[-1]=='D':
    
elif numeroCadena[-1]=='B':
    
while numeroCadena < 0:
    numeroCadena = input("Introduce el numero decimal o binario para convertirlo 293D/10101B: ")

    numeroCadena = int(numeroCadena[0:-1])
print(numeroCadena)
'''