
'''
2. Design a program for reading an integer between 0 and 10 and show the times table.
To ask for the number you should show the next message "Enter one number
between 0 and 10”. If the number is out of the boundaries, the program should show
the message “The number is out of the boundaries”. If the number is valid, it should
show the times table following the next format:
7*0=0
7*1=7
.....
7*10=70
'''

num = int(input("Introduce un numero comprendido entre 1 y 10: "))

if 0>=num>=10:
    print("Tabla del", num)
    for i in range(0,11):
        resul=num*i
        print("%s*%s ="%(num,i), resul)
else:
    print("Error: introduce un numero comprendido entre 1 y 10")