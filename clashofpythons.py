#!/usr/bin/python3

import xmltodict
import pprint
import random


def fin (hpjugador,hpenemigo):
	if hpjugador > hpenemigo:
		print("Has ganado! Te has quedado con: " + str(hpjugador) + " puntos de vida.")
	if hpenemigo > hpjugador:
		print("Has perdido! El enemigo ha sobrevivido con: " + str(hpenemigo) + " puntos de vida.")


xml_file = open("clashroyale.xml", "r")
diccionario = xmltodict.parse(xml_file.read())

xml_enemy = open("enemy1.xml", "r")
enemy = xmltodict.parse(xml_enemy.read())


randomindex = random.randint(0,2)


enemigo1 = enemy["enemies"]["enemy"][randomindex]
enemigo1health = enemigo1["health"]
enemigo1description = enemigo1["description"]
enemigo1damage = enemigo1["strenght"]

jugadorhealth = 30
print("HP del enemigo inicial: "+ enemigo1health)
print("HP inicial del jugador: " + str(jugadorhealth))


while jugadorhealth != 0 or enemigo1health != 0:
	

	damage = str(input("Quieres atacar?, escribe ataca: "))
	print()
	randomdaño = random.randint(0,5)

	if damage == "ataca":

		enemigo1health = int(enemigo1health) - randomdaño

		print("Le has quitado: " + str(randomdaño) + " al jugador, ahora tiene: " + str(enemigo1health) + " puntos de vida.")
		print()
	
		randomdañoplayer = random.randint(0,2)
		jugadorhealth = jugadorhealth - randomdañoplayer
		print("El enemigo te ha atacado, te ha quitado: " + str(randomdañoplayer) + " puntos de vida, ahora tienes: " + str(jugadorhealth) + " puntos de vida.")
 
	
	if damage != "ataca":
		print("Input incorrecto, escribe ataca")
	

	if str(jugadorhealth) <= "0" or str(enemigo1health) <= "0":
		fin(jugadorhealth,enemigo1health);		
		break


#if daño == "ataca":

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(diccionario)
#print(diccionario)
#print(diccionario["characters"]["character"][0]["name"])

#numero = int(input("Elije un numero del 0 al 2: "))
#print(diccionario["characters"]["character"][numero])

#character = diccionario["characters"]["character"][int(character)]

#print("Name: "+ character["name"])
#print("Health: "+character["health"])
#print("Damage: "+characer["damage"])
#print("Level: "+level["level"])
