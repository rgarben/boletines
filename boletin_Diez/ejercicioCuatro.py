'''
4. Design a function called numberInString that has a string of characters as parameter, the
method should return how many of those characters are numbers.

Rafael García Benítez
'''

def contarNumeroEnCadena (cade):
    contarNumero=0
    listaNumeros=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(cade)):
        if cade[i] in listaNumeros:
            contarNumero+=1
    return contarNumero

print(contarNumeroEnCadena('9djvu4vcjnsj8'))