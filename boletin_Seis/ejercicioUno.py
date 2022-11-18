
'''
1. Design a program to show all numbers between 1 and 100. If the number is a
multiple of 7 you should show the message "The number xx is a multiple of 7". If the
number is a multiple of 13 you should show the message "The number xx is a
multiple of 13". If the number is a multiple of 7 and 13 you should show both
messages.

Rafael García Benítez
'''

for i in range(1, 101):
    
    if i%7==0 and i%13==0:
        print("El numero", i,"multiplo de 7 y de 13.")
    elif i%13==0:
        print("El numero", i,"multiplo de 13.")
    elif i%7==0:
        print("El numero", i,"multiplo de 7.")
    else:
        print("El numero", i,"no es multiplo ni de 7 ni de 13.")