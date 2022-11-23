'''
1. Design a method called computeFactorial that receives a positive integer and
returns the factorial for that number. If the number is negative the method should
return None.

Rafael García Benítez
'''

def factorialNumero (numero):
    facto=1
    for i in range(numero):
        facto*=i+1
    if numero < 0:
        return None
    return facto

print(factorialNumero(4))