'''
6. Juan recibe dos tipos de regalos de cumpleaños según el año en el que esté: si el
año es para su familia le regala un puzzle; si es impar, recibe dinero.
Cada nuevo cumpleaños recibe más regalos: así, cada año que recibe puzzles
obtiene el doble que el anterior; sin embargo, si se trata de dinero recibe 15€ más
que en la anterior ocasión.
Elabora un programa que calcule cuántos regalos ha recibido en total Juan, para una
edad determinada sabiendo que en el primer cumpleaños le regalaron un puzzle y
en el segundo 20€.
Ejemplo: 1 año ⇒ 1 puzzle
Ejemplo: 2 años ⇒ 1 puzzle y 20€ (tenía un puzzle y recibe 20€)
…..
…..
Ejemplo: 7 años ⇒ 15 puzzles y 105€ (tenía 105€ y recibe 8 puzzles)

Rafael Garcia Benitez
'''

año = int(input("Introduce numero de años: "))
puzzle = 1
dinero = 0
acumulaDinero=20
acumula2Puzzle=1
for i in range(1, año):
    if i%2==0:
        dinero+=acumulaDinero
        acumulaDinero+=15
    else:
        acumula2Puzzle*=2
        puzzle+=acumula2Puzzle
print(f"{año} años => {puzzle} puzzles y {dinero}€ (tenia {acumulaDinero} y recibe {acumula2Puzzle} puzzles)")