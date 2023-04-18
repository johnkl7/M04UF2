#!/usr/bin/python3

import xmltodict
import pprint

xml_file = open("clashroyale.xml", "r")
diccionario = xmltodict.parse(xml_file.read())


#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(diccionario)
#print(diccionario)
#print(diccionario["characters"]["character"][0]["name"])

numero = int(input("Elije un numero del 0 al 2: "))
print(diccionario["characters"]["character"][numero])

#character = diccionario["characters"]["character"][int(character)]

#print("Name: "+ character["name"])
#print("Health: "+character["health"])
#print("Damage: "+characer["damage"])
#print("Level: "+level["level"])
