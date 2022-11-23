'''
14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga.
Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá la
que tenga el mayor número de caracteres repetidos .

Rafael García Benítez
'''

frase="No te olvides. Intenta siempre ser eeeeeeeee con los demas."
frase1="No te olvides. Intenta siempre ser agradable con los demas."

def devolverCadenaMasGrandeComparandoCaracteres(frase, frase1):
    frase
    lista=[]
    lista1=[]
    if len(frase)<len(frase1):
        frase=frase1
    elif len(frase)==len(frase1):
        for i in range(len(frase)):
            if frase[i] not in lista:
                lista.append(frase[i])
            if frase1[i] not in lista1:
                lista1.append(frase1[i])
        if len(lista)>len(lista1):
            frase=frase1
    return frase

print(f"es mas larga la cadena: {devolverCadenaMasGrandeComparandoCaracteres(frase, frase1)}")