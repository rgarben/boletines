'''
2. Design a function called lowCaseInString that has a string of characters as parameter, the
method should return how many of those characters are lowcase letters.

Rafael García Benítez
'''

def contarMinuscolasCadena (cade):
    contarMinusculas=0
    for i in range(len(cade)):
        if cade[i]==cade[i].lower():
            contarMinusculas+=1
    return contarMinusculas

print(contarMinuscolasCadena('TasTasdjTasjdTasjdTdadT'))