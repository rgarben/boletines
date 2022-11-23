'''
6. Design a method called getNumberOfDigits that receives one number (it can be
real, integer, positive or negative) and should return the number of digits it contains. If
the parameter is not valid the method should return None. Extend this function to
other numeric systems (hexadecimal, decimal, binary, octal).

Rafael García Benítez
'''

def contarDigitos (num):
    lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    listaV = []
    for i in range (len(num)):
        if num[i] in lista:
            listaV.append(num[i])
        contarNumeros=len(listaV)
    return contarNumeros

print(contarDigitos('234A'))