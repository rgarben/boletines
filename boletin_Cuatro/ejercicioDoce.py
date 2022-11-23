'''
12. La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la cual
se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta del
producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo A,
se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es de
tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.

Rafael García Benítez
'''

tipo = str(input("Introduce el tipo A o B: "))
tamaño = int(input("Introduce un tamaño 1 o 2: "))

if tipo=='A' and tamaño == 1:
    print("Se le cargaran 20 centimos mas al precio inicial")
elif tipo=='A' and tamaño == 2:
    print("Se le cargaran 30 centimos mas al precio inicial")
elif tipo=='B' and tamaño == 1:
    print("Se le rebaran 30 centimos mas al precio inicial")
elif tipo=='B' and tamaño == 2:
    print("Se le rebaran 50 centimos mas al precio inicial")
else:
    print("Error, introduce tipo entre A o B y tamaño 1 o 2.")