'''
9. En un establecimiento en rebajas, hay 3 tipos de productos (A, B y C). El
porcentaje de rebaja que se aplicará sobre el precio original del producto se
calcula de la siguiente forma:
 Si el producto es de tipo A, independientemente de su precio se
aplica un 7% de descuento.
 Si el producto es de tipo C o bien el precio es inferior a 500€ se
aplicará un porcentaje del 12% de descuento.
 En el resto de casos se aplica un 9% de descuento.
Realizar un programa que solicite los datos necesarios (tipo de producto y
precio original) y calcule el precio rebajado. Debe comprobarse que los
datos de entrada son correctos, y si no lo son mostrar un mensaje de error.

Rafael García Benítez
'''

producto = str(input("Introduce un producto A, B o C: "))
precio = int(input("Introduce un precio: "))

if producto == 'A':
    print(precio-(precio*0.07))
elif producto == 'C' or precio < 500:
    print(precio-(precio*0.12))
elif producto == 'B':
    print(precio-(precio*0.09))
else:
    print("Error, introduce los productos A, B o c.")