
import random

print ("BIENVENIDO A PIEDRA PAPEL TIJERA")

print ("JUGADOR-1 escoga entre: piedra, papel, tijera:")
jugador1 = input().lower()

print (f"JUGADOR-1 escoge: {jugador1}")

opciones = ["piedra", "papel", "tijera"]
jugador2 =random.choice(opciones)
print (f"La maquina escoge: {jugador2}")

if (jugador1 == "piedra" or jugador1 == "papel" or jugador1 == "tijera") and (jugador2 == "piedra" or jugador2 == "papel" or jugador2 == "tijera"):
    if jugador1 == jugador2:
        print ("hubo un empate ambos escojieron: ", jugador2)
    elif jugador1 == "piedra" and jugador2 == "tijera":
        print ("JUGADOR-1 GANA: " + jugador1  + " GANA A " + jugador2)
    elif jugador1 == "papel" and jugador2 == "piedra":
            print ("JUGADOR-1 GANA: " + jugador1  + " GANA A " + jugador2)
    elif jugador1 == "tijera" and jugador2 == "papel":
            print ("JUGADOR-1 GANA: " + jugador1  + " GANA A " + jugador2)
    else:
         print ("Maquina GANA: " + jugador2 + " GANA A " + jugador1)

else:
    print ("No se escogio una opcion valida")






