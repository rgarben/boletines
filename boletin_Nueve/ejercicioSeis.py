'''
6. Design a method called getNumberOfDigits that receives one number (it can be
real, integer, positive or negative) and should return the number of digits it contains. If
the parameter is not valid the method should return None. Extend this function to
other numeric systems (hexadecimal, decimal, binary, octal).

Rafael García Benítez
'''

def validarNumero (num):
    lista = '01234567890.-ABCDEF'
    contarMenos=0
    contarPuntos=0
    validar=True
    for i in range(len(lista)-1):
        if '-' in num:
            contarMenos+=1
        if '.' in num:
            contarPuntos+=1
    if contarPuntos>1 and num[0]=='.' and num[-1]=='.':
        validar=False
    elif contarMenos>1 and num[0]!='-':
        validar=False
    elif num[1]=='.' and num[0]=='-':
        validar=False
    for i in range(len(num)):
        if num[i] not in lista:
            validar=False
    return validar

def contarDigitoshexadecimal (num):
    lista = '0123456789ABCDEF.-'
    lista2 = '0123456789ABCDEF'
    hexa=True
    contador=0
    if validarNumero(num):
        for i in range(len(num)):
            if num[i] in lista2:
                contador+=1
                hexa=contador
        for i in range(len(num)):
            if num[i] not in lista:
                hexa=False
    else:
        hexa=False
    return hexa

def contarDigitosDecimal (num):
    lista = '0123456789.-'
    lista2 = '0123456789'
    decimal=True
    contador=0
    if validarNumero(num):
        for i in range(len(num)):
            if num[i] in lista2:
                contador+=1
                decimal=contador
        for i in range(len(num)):
            if num[i] not in lista:
                decimal=False
    else:
        decimal=False
    return decimal

def contarDigitosBinario (num):
    lista = '01.-'
    lista2 = '01'
    Binario=True
    contador=0
    if validarNumero(num):
        for i in range(len(num)):
            if num[i] in lista2:
                contador+=1
                Binario=contador
        for i in range(len(num)):
            if num[i] not in lista:
                Binario=False
    else:
        Binario=False
    return Binario

def contarDigitosOctal (num):
    lista = '01234567.-'
    lista2 = '01234567'
    Octal=True
    contador=0
    if validarNumero(num):
        for i in range(len(num)):
            if num[i] in lista2:
                contador+=1
                Octal=contador
        for i in range(len(num)):
            if num[i] not in lista:
                Octal=False
    else:
        Octal=False
    return Octal

print(contarDigitoshexadecimal('-29382.2323F'))
print(contarDigitosDecimal('-46.36'))
print(contarDigitosBinario('-101.010110'))
print(contarDigitosOctal('-172.635'))