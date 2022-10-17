
'''
3. Design a program that asks how many numbers the user wants to introduce. Then,
the user would have to introduce the numbers one by one and the program should
say if each one of the numbers is odd or even. If the user inputs 0 or a negative
number, it is not valid, and the system should ask for another number. The messages
are the following:
“How many numbers do you want input?” to ask for the number of numbers.
“Enter one number greater than 0:” to ask for a number.
“The number is not valid, it should be greater than 0” to inform that the number is not
valid.
“The number XX is odd”
“The number XX is even”
'''

n = int(input("¿Cuantos numeros quieres introducir?"))
i=0

while n>i:
    n1 = int(input("Introduce un numero: "))
    while n1<0:
        n1=int(input("Error: Introduce un numero positivo: "))
    if n1>0 and n1%2==0:
        print("El numero es par")
        i=i+1
    elif n1>0 and n1%2==1:
        print("El numero es impar")
        i=i+1
    