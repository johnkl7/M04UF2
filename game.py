
#!/usr/bin/python3

import pyfiglet
import time
from enemies_class import Enemies
from player_class import Player
import os


file_type = 0
player = Player(0)
enemies = Enemies(1)
enemies2 = Enemies(2)
current_enemy = 0
restart = 0


def game (saved_enemy,reinicio):
	global file_type
	file_type = 1
	global current_enemy
	global restart
	global jsonorxml
	count = enemies.count()

	if reinicio == 0:
		enemies.start()

	restart = 1
	current_enemy = saved_enemy
	salir = False

	while not salir:
			
		end = enemies.dead(current_enemy)
		end2 = player.dead()
			
		if end2 <= 0:
			print("\033[91mGAME OVER\033[0m")
			time.sleep(3)
			os.system('clear')
			break

		if end:
			current_enemy = current_enemy + 1
			print("\033[32mHas acabado con el enemigo, felicitaciones!\033[0m")	
			print()
			
			if current_enemy >= count:		
				print("\033[32mDERROTASTE A TODOS LOS ENEMIGOS Y GANASTE LA PARTIDA, FELICIDADES!!\033[0m")
				time.sleep(3)
				os.system('clear')
				break
		
		print()
		print("Te ataca un enemigo, estos son sus estadisticas atuales: ")
		enemies.show_info(current_enemy)
		print("Escribe ataca para atacar al enemigo")
		print()

		opc = input("¿Que quieres hacer? ")
	
		if opc == "G":
			print("Guardando partida..")
			os.system('clear')
			break

		if opc == "ataca":
			
			playerdamage = player.attack()
			print()
		
			print("Has atacado al enemigo y le has quitado \033[31m" + str(playerdamage)+ "\033[0m puntos de vida.")

			dead = enemies.hurt(playerdamage,current_enemy)
			enemydamage = enemies.attack(current_enemy)
			
			print("El enemigo te ha quitado \033[31m" + str(enemydamage) + "\033[0m puntos de vida.")
			player.hurt(enemydamage)	 	
	

def game2 (saved_enemy,reinicio):
	
	global file_type
	file_type = 2	
	count = enemies2.count()
	global current_enemy
	global restart
	global jsonorxml
	
	if reinicio == 0:
		enemies2.start()
												
	restart = 1
	current_enemy = saved_enemy
	salir = False
																
	while not salir:
																			
		end = enemies2.dead(current_enemy)
		end2 = player.dead()

		if end2 <= 0:
			print("\033[91mGAME OVER\033[0m")
			time.sleep(3)
			os.system('clear')
			break

																																							
		if end:
			current_enemy = current_enemy + 1
			print("\033[32mHas acabado con el enemigo, felicitaciones!\033[0m")		
			print()			 
		
			if current_enemy >= count:
				print("\033[32mDERROTASTE A TODOS LOS ENEMIGOS Y GANASTE LA PARTIDA, FELICIDADES!!\033[0m")
				time.sleep(3)
				os.system('clear')
				break
			
		print()
		print("Te ataca un enemigo, estos son sus estadisticas atuales: ")
		enemies2.show_info(current_enemy)
		print("Escribe ataca para atacar al enemigo.")
		print()

		opc = input("¿Que quieres hacer? ")

		if opc == "G":
			print("Guardando partida..")
			os.system('clear')
			break

		if opc == "ataca":
			playerdamage = player.attack()				
			print()
			print("Has atacado al enemigo y le has quitado \033[#1m" + str(playerdamage)+ "\033[0m puntos de vida.")

			dead = enemies2.hurt(playerdamage,current_enemy)
			enemydamage = enemies2.attack(current_enemy)
			
			print("El enemigo te ha quitado \033[31m" + str(enemydamage) + "\033[0m puntos de vida.")
			player.hurt(enemydamage)
		
		if opc != "ataca":
			print("Debes escribir ataca para hacer daño al enemigo")

if __name__ == "__main__":
	title = pyfiglet.figlet_format("Empieza el juego", width=120)
	print("            ____")
	print("           / . .\\")
	print("           \\  ---<")
	print("            \\   /")
	print("  __________/  /")
	print("-=:___________/")

	print(title)

		

	
	opc = ""

	while True:
		print()
		print("1. - Juego nuevo")
		print("2. - Cargar juego")
		print("S. - Salir")
		opc = input("Introduce una opción: ")
		print()
		

		if opc == "s":
			print(pyfiglet.figlet_format("Saliendo del juego...", width=120))
			time.sleep(2)
			break

		if opc == "1":
			tipo = input("Pulsa 1 para jugar con JSON, pulsa 2 para jugar con XML: ")
			if tipo == "1":
				print("La partida esta apunto de empezar...")
				print("\033[32mPuedes guardar la partida en cualquier momento utilizando la tecla G\033[0m")
				time.sleep(1.2)
				print()
				restart = 0
				current_enemy = 0
				player.input_info()
				player.write_info()
				game(current_enemy,restart)

			if tipo == "2":
				print("La partida esta apunto de empezar...")
				print("\033[32mPuedes guardar la partida en cualquier momento utilizando la tecla G\033[0m")
				time.sleep(1.2)
				print()
				restart = 0
				current_enemy = 0
				player.input_info()
				player.write_info()
				game2(current_enemy,restart)

		if opc == "2":
						
			print("Cargando última partida guardada..")
			time.sleep(0.2)
			print("Cargando stats del último enemigo...")
			time.sleep(0.2)
			print("Cargando stats de tu personaje...")
			time.sleep(0.2)

			if file_type == 2:
				restart = 1
				game2(current_enemy,restart)

			if file_type== 1:
				restart = 1
				game(current_enemy,restart)
			

		if opc != "2" and "1" and "s":
			print("Opcion incorrecta")
