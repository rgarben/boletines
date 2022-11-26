'''
10. Design a method called isFriendNumber that receives two positive numbers and
returns True if the numbers are friends, False otherwise. Two numbers are
considered to be friends if the sum of its divisors, except the given number, is equal
to the second and vice versa.

Rafael García Benítez
'''

def numerosAmigos (num1,num2):
    sonAmigos=False
    sumaDivi1=0
    sumaDivi2=0
    for i in range(1,num1):
        if num1%i==0:
            sumaDivi1+=i
    for i in range(1,num2):
        if num2%i==0:
            sumaDivi2+=i
    if sumaDivi1==num2 and sumaDivi2==num1:
        sonAmigos=True
    return sonAmigos

print(f"¿Numero {1184} y {1210} son amigos? {numerosAmigos(1184, 1210)}")