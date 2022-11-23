'''
5. Design a method called powerIt that receives two integers and raises the first
number to the second. You may use the product or recursion and check the values. If
no exponent is provided the first number is raised to 0.

Rafael García Benítez
'''

def calcularNumeroElevado (numReal,numEntero=2):
    multi=1
    for i in range (numEntero):
        multi=multi*numReal
    return multi

print(calcularNumeroElevado(2,3))
print(calcularNumeroElevado(10))