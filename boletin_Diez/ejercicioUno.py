'''
1. Design a function called charactersInString that has a character string and a character as
input parameters and returns how many times that character appears in the string.

Rafael García Benítez
'''

def contarCaracteresEnCadena (c,cade):
    contarCaracter=0
    for i in range(len(cade)):
        if cade[i].upper()==c.upper():
            contarCaracter+=1
    return contarCaracter

print(contarCaracteresEnCadena('z','jaosZdjiszdjoaZpghafpzZdjifz'))