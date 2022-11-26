'''
9. Design a method called getPrimeDivisors that receives a positive number as a
parameter and returns a list containing its prime divisors. If the parameter is not valid
the method should return None.

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

def divisoresPrimos (num):
    divisoresPrimos=[]
    for i in range(1,num):
        if num%i==0 and esPrimo(i):
            divisoresPrimos.append(i)
    return divisoresPrimos

print(divisoresPrimos(10))