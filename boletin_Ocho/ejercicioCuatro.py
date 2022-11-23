'''
4. Crea un programa que lea por teclado números de forma sucesiva y los guarde en
una lista; el proceso de lectura y guardado finalizará cuando metamos un número
negativo. En ese momento se mostrará el elemento mayor y los números pares.

Rafael Garcia Benitez
'''

numero = int(input("Introduce numeros para almacenar, terminara cuando metas uno negativo: "))

lista = []
listaPares = []

def obtenerElementoMayor (lista):
    mayor=0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor

while numero > 0:
    lista.append(numero)
    if numero%2==0 and numero >=0:
        listaPares.append(numero)
    numero = int(input("Introduce numeros para almacenar, terminara cuando metas uno negativo: "))
print("El numero mayor es: ", obtenerElementoMayor(lista), "y los numeros pares son: ", listaPares)