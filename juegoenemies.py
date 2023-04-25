#!/usr/bin/python3

import xmltodict
import pprint
import random

def fin (hpjugador,hpenemigo):
	if hpjugador > hpenemigo:
		print("Has ganado! Te has quedado con: " + str(hpjugador) + " puntos de vida.")
	if hpenemigo > hpenemigo:
		print("Has perdido! El enemigo ha sobrevivido con: " + str(hpenemigo) + " puntos de vida.")

xml_enemy = open("enemy1.xml", "r")
enemy = xmltodict.parse(xml_enemy.read())

randomindex = random.randint(0,2)
contador = 0

enemigo1 = enemy["enemies"]["enemy"][contador]
enemigo1health = enemigo1["health"]
enemigo1description = enemigo1["description"]
enemigo1damage = enemigo1["strenght"]


jugadorhealth = 30

while jugadorhealth != 0 or enemigo1health != 0:

	print("HP del enemigo inicial: " + str(enemigo1health))
	print("HP inicial del jugador: " + str(jugadorhealth))

	daño = str(input("Quieres atacar?, escribe ataca: "))
	print()
	randomdaño = random.randint(5,7)

	if daño == "ataca":
		enemigo1health = int(enemigo1health) - randomdaño
		print("Le has quitado: " + str(randomdaño) + " al jugador, ahora tiene: " + str(enemigo1health) + " puntos de vida.")
		print()
		randomdañoplayer = random.randint(1,4)
		jugadorhealth = jugadorhealth - randomdañoplayer
		print("El enemigo te ha atacado, te ha quitado: " + str(randomdañoplayer) + " puntos de vida, ahora tienes: " + str(jugadorhealth) + " puntos de vida.")
	if jugadorhealth <= 0 and str(enemigo1health) <= "0":
		print("ESTO ACABA EN EMPATE")
		break
	
	if jugadorhealth <= 0:
		print("Has sido eliminado")
		break
	
	if daño != "ataca":
		print("Input incorrecto, escribe ataca")

	if str(jugadorhealth) <= "0" or str(enemigo1health) <= "0":
		contador = contador + 1
		if contador == 3:
			fin(jugadorhealth,enemigo1health);
			break
		else:
			enemigo1 = enemy["enemies"]["enemy"][contador]
			enemigo1health = enemigo1["health"]
			enemigo1description = enemigo1["description"]
			enemigo1damage = enemigo1["strenght"]
			print()
			print("Ahora a por el siguiente enemigo...")


