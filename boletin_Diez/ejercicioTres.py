'''
3. Design a function called upperCaseInString that has a string of characters as parameter
and the method should return how many are uppercase letters.

Rafael García Benítez
'''

def contarMayuscolasCadena (cade):
    contarMayusculas=0
    for i in range(len(cade)):
        if cade[i]==cade[i].upper():
            contarMayusculas+=1
    return contarMayusculas

print(contarMayuscolasCadena('TasTasdjTasjdTasjdTdadT'))