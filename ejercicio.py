#!/usr/bin/python3

import xmltodict
import random


print("Crea un enemigo")
print("---------------")

description = input("Descripcion: ")
strenght = int(input("Fuerza: "))
health = int(input("Salud: "))

enemy =  {
	"enemy": {
		"description": description,
		"health": health,
		"strenght": strenght
	}
}

enemy_xml = xmltodict.unparse(enemy, pretty = True)
print(enemy_xml)

xml_file = open("enemy3.xml", "w")
xml_file.write(enemy_xml)
xml_file.close()
