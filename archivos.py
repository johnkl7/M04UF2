#!/usr/bin/python3



try:
	archivo = open("numeritos.txt", "r")
	#print(archivo.read())
	#print(archivo.readline())
	linea = archivo.readline()
	lista = linea.split(";")
	print(lista[2])
	archivo.close()
except:
	print("Error al abrir el archivo")

archivo = open("textitos.txt", "w")
archivo.write("ola k ase")
archivo.close


diccionario = {
	"nombre": "John",
	"apellido": "Largao",
	"altura": 1.1 
}

print(diccionario["altura"])
