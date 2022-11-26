'''
5. Design a function called palindrome that has a string of characters as parameter, and return
true if it is a palindrome or false in other case. A word is a palindrome, if it is reads the
same from left to right as from right to left, ignoring whites,. For example: "anilina" or "el
abad le dio arroz al zorro" To simplify the problem, you can assume that simple characters
are used, that is, without tildes or diresis.

Rafael García Benítez
'''

def esPalindromo (cade):
    palindromo=True
    for i in range(len(cade)):
        if cade[i]!=cade[-i-1]:
            palindromo=False
    return palindromo

print(esPalindromo('girafarig'))