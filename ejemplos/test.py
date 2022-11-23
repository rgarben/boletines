'''
Entrega 21 Noviembre

Rafael García Benítez
'''

def anioBisiesto(year):
    bisiesto = year%4==0 and (year%100!=0 or year%400==0)
    return (bisiesto)

year=2004

assert anioBisiesto(year)

assert not anioBisiesto(2003)

assert anioBisiesto(0)

assert not anioBisiesto(-1)

assert(anioBisiesto(2000))

assert(anioBisiesto(2004))

print("OK")