'''
7. Design a method called isPrime that receives one integer positive number greater
than 0 as parameter. The method should return True if the number is prime or False if
not prime. If the parameter is not valid the method should return None.

Rafael García Benítez
'''

def esPrimo (num):
    primo=False
    contador = 0
    for i in range(2,num):
        if num %i==0:
            contador+=1
    if num<2:
        primo=None
    elif contador==0:
        primo=True
    return primo

print(esPrimo(7))