'''
Rafael García Benítez  1º DAW B
'''

jugador1 = input("Introduce el 1º jugador piedra/papel/tijera/lagarto/spot: ")
jugador2 = input("Introduce el 2º jugador piedra/papel/tijera/lagarto/spot: ")
while jugador1!='spock' or jugador2!='spock':
    while jugador1!='piedra' and jugador1!='papel' and jugador1!='tijera' and jugador1!='lagarto' and jugador1!='spock':
        jugador1 = input("Error: Introduce el 1º jugador piedra/papel/tijera/lagarto/spot: ")
    while jugador2!='piedra' and jugador2!='papel' and jugador2!='tijera' and jugador2!='lagarto' and jugador2!='spock':
        jugador2 = input("Error: Introduce el 2º jugador piedra/papel/tijera/lagarto/spot: ")
    if ((jugador1=='tijera') and (jugador2=='papel' or jugador2=='lagarto')) or ((jugador1=='papel') and (jugador2=='spock' or jugador2=='piedra')) or ((jugador1=='piedra') and (jugador2=='tijera' or jugador2=='lagarto')) or ((jugador1=='lagarto') and (jugador2=='papel' or jugador2=='spock')) or ((jugador1=='spock') and (jugador2=='tijera' or jugador2=='piedra')):
        print("Jugador1 gana.")
    elif ((jugador2=='tijera') and (jugador1=='papel' or jugador1=='lagarto')) or ((jugador2=='papel') and (jugador1=='spock' or jugador1=='piedra')) or ((jugador2=='piedra') and (jugador1=='tijera' or jugador1=='lagarto')) or ((jugador2=='lagarto') and (jugador1=='papel' or jugador1=='spock')) or ((jugador2=='spock') and (jugador1=='tijera' or jugador1=='piedra')):
        print("Jugador2 gana.")
    else:
        print("Los jugadores empatan")
    jugador1 = input("Introduce el 1º jugador piedra/papel/tijera/lagarto/spot: ")
    jugador2 = input("Introduce el 2º jugador piedra/papel/tijera/lagarto/spot: ")
print("Partida terminada.")