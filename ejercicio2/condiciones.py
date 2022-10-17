'''
Created on Sep 26, 2022

@author: estudiante
'''

'''
temperatura = 25

if temperatura>25 :
    print("Encendiendo el aire acondicionado")
print("A refrescarse") #si no lo ponemos a la misma altura no esta dentro del if

'''
'''
temperatura = 51

if temperatura>25 :
    print("Encendiendo el aire acondicionado")
    print("A refrescarse")
    
if temperatura>15 and temperatura <=25 :
    print("Encendiendo el ventilador")
    
if temperatura <= 15 :
    print("Enciendo la calefacción")
    
'''

'''
temperatura = int(input("Dime una temperatura"))

if temperatura>25 :
    print("Encendiendo el aire acondicionado")
    print("A refrescarse")
    
elif temperatura>15 and temperatura <=25 :
    print("Encendiendo el ventilador")
    
elif temperatura <= 15 :
    print("Enciendo la calefacción")
'''

'''
edad = int(input("Dime tu edadd: ")) 

if edad >=18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")
'''

temperatura = int(input("Dime una temperatura: ")) 
llueve = True
if temperatura > -100 and temperatura <=10:
    print("Enciendo la calefacción")
    
    if llueve:
        print("Coge paraguas")
    else:
        print("...")
elif temperatura > 10 and temperatura <=15:
    print("No hacemos nada, la temperatura es adecuada")
elif temperatura > 15 and temperatura <=25:
    print("Encendemos ventilador")
else:
    print("Enciendo el aire acondicionado")
print("Hasta mañana")
    

    
    