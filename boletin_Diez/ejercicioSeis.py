'''
6. Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.

Rafael García Benítez
'''

def buscarCadenaEnCadena (buscarCade,cade):
    palabra=True
    contarCaracter=0
    for i in range(len(cade)):
        if cade[i] in buscarCade:
            contarCaracter+=1
    if contarCaracter==len(buscarCade):
        palabra=False
    return palabra

print(buscarCadenaEnCadena('hola', 'shybaoxlna'))