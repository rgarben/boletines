'''
14. La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el cobro
es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan 1 euro,
los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir del
décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es domingo, y si
es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice un algoritmo para
determinar cuánto debe pagar por cada concepto una persona que realiza una llamada.

Rafael Garćia Benítez
'''

minutos = int(input("Introduce numero de minutos de llamada: "))
turno = str(input("Introduce el turno , Domingo, Tarde o Mañana: "))

if 0<minutos <= 5 and turno== 'Domingo':
    print("La llamada costara:", (minutos*1)+((minutos*1)*0.03))
elif 0<minutos <= 5 and turno== 'Tarde':
    print("La llamada costara:", (minutos*1)+((minutos*1)*0.10))
elif 0<minutos <= 5 and turno== 'Mañana':
    print("La llamada costara:", (minutos*1)+((minutos*1)*0.15))
elif 5<minutos <= 8 and turno== 'Domingo':
    print("La llamada costara:", 5+((minutos-5)*0.80)+(((minutos-5)*0.80)*0.03))
elif 5<minutos <= 8 and turno== 'Tarde':
    print("La llamada costara:", 5+((minutos-5)*0.80)+(((minutos-5)*0.80)*0.10))
elif 5<minutos <= 8 and turno== 'Mañana':
    print("La llamada costara:", 5+((minutos-5)*0.80)+(((minutos-5)*0.80)*0.15))
elif 8<minutos <= 10 and turno== 'Domingo':
    print("La llamada costara:", 7.4+((minutos-8)*0.70)+(((minutos-8)*0.70)*0.03))
elif 8<minutos <= 10 and turno== 'Tarde':
    print("La llamada costara:", 7.4+((minutos-8)*0.70)+(((minutos-8)*0.70)*0.10))
elif 8<minutos <= 10 and turno== 'Mañana':
    print("La llamada costara:", 7.4+((minutos-8)*0.70)+(((minutos-8)*0.70)*0.15))
elif minutos > 10 and turno== 'Domingo':
    print("La llamada costara:", 8.8+((minutos-10)*0.50)+(((minutos-10)*0.50)*0.03))
elif minutos > 10 and turno== 'Tarde':
    print("La llamada costara:", 8.8+((minutos-10)*0.50)+(((minutos-10)*0.50)*0.10))
elif minutos > 10 and turno== 'Mañana':
    print("La llamada costara:", 8.8+((minutos-10)*0.50)+(((minutos-10)*0.50)*0.15))
else:
    print("Error, introduce minutos positivos y turnos Domingo, Mañana o Tarde.")