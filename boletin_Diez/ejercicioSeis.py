'''
6. Realizar una función que busque una palabra escondida dentro de un texto. Por ejemplo, si
la cadena es “shybaoxlna” y la palabra que queremos buscar es “hola”, entonces si se
encontrará y deberá devolver True, en caso contrario deberá devolver False.

Rafael García Benítez
'''

def buscarPalabraEnCadena (buscarCade,cade):
    palabra=False
    contarCaracter=0
    contarLetras=0
    while contarLetras < (len(cade)):
        if contarCaracter<len(buscarCade) and buscarCade[contarCaracter]==cade[contarLetras]:
            contarCaracter+=1
        contarLetras+=1
    if contarCaracter==len(buscarCade):
        palabra=True
    return palabra

print(buscarPalabraEnCadena('hola', 'shyboaxlnaa'))