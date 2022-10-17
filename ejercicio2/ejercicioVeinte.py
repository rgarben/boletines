'''
20. Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 €, el
segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un programa para determinar
cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.
'''

pagar = 10
suma=10

for i in range(1, 20):
    pagar*=2
    suma+=pagar
print(f"{suma}")