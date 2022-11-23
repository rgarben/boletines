'''
8. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de
pedirnos cuantas monedas tenemos de 2e, 1e, 50 céntimos, 20 céntimos o 10 céntimos).

Rafael García Benítez
'''

dosEuros = int(input("Introduce monedas de 2 euros: "))
unEuro = int(input("Introduce monedas de 1 euro: "))
cincuenta = int(input("Introduce monedas de 50 centimos: "))
veinte = int(input("Introduce monedas de 20 centimos: "))
diez = int(input("Introduce monedas de 10 centimos: "))
calcularEuros = ((cincuenta*50)+(veinte*20)+(diez*10))//100
calcularCentimos = ((dosEuros*200)+(unEuro*100))+calcularEuros

print("Tienes:", calcularEuros,"en euros y en centimos", calcularCentimos)