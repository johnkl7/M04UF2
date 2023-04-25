#!/usr/bin/python3

import xmltodict
import random

fin = 0

def obten_datos():
	description = input("Description: ")
	strenght = int(input("Fuerza: "))
	health = int(input("Salud: "))

	return {

		"description": description,
		"strenght": strenght,
		"health": health

	}

def escribe_datos (export):
	enemy_xml = xmltodict.unparse(export, pretty=True)
	print(enemy_xml)
	xml_file = open("enemy.xml", "w")
	xml_file.write(enemy_xml)
	xml_file.close()

salir = False
enemigos = []
while not salir:
	opcion = input("¿Quieres añadir un enemigo?[s/N]")

	if opcion != "s":
		salir = True
		continue

	enemigo = obten_datos()
	enemigos.append(enemigo)

enemies_export = {
	"enemies": {
		"enemy": enemigos
		}
}

escribe_datos(enemies_export)

#array = []
#while fin == 0:

#	sino = input("Quieres crear un enemigo? Escribe si o no: ")
	 

#	if sino == "si":
#			print("Crea un enemigo")
#			print("---------------")

#			description = input("Descripcion: ")
#			strenght = int(input("Fuerza: "))
#			health = int(input("Salud: "))

#			enemy =  {
#				"enemy": {
#					"description": description,
#					"health": health,
#					"strenght": strenght
#				}
#			}
#		
#			array.append(enemy)
#			print(array)
	#		enemy_xml = xmltodict.unparse(array, pretty = True)
	#		print(enemy_xml)

		#	xml_file = open("enemy3.xml", "w")
		#	xml_file.write(enemy_xml)
		#	xml_file.close()

#	elif sino == "no":
#		fin = 1
	
#	else:
#		print("Opcion incorrecta")
