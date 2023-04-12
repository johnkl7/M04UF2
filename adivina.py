import random
#import math

#print(math.floor(random.random()*100)+1)

random = random.randint(0,100)
print(random)
respuesta = ""




while respuesta != random:
	respuesta = int(input("Introduce un numero del 1 al 100: "))
	if random < respuesta:
		print("El numero que buscas es menor")
	elif random > respuesta:
		print("El numero que buscas es mayor")
	else:
		print("Lo adivinaste! El numero era el: "+ str(random))

		
