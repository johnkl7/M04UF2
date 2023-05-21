#!/usr/bin/python3

import random


class Enemy:


#constructor
	def __init__ (self,name,health,strength,description = ""):
		self.name = name
		self.health = health
		self.strength = strength
		self.description = description

#		print(self.name + ": " + self.description)


	def attack (self):
		return random.randint(0,self.strength)


	def show_info (self):
		print("Name: " + self.name)
		print("Health: " + str(self.health))
		print("Strength: " + str(self.strength))
		print("Description: " + self.description)	
#		if self.description != "":
#			print("Description: " + self.description)
	
	def hurt (self,damage):
		self.health = self.health - damage
		if self.health > 0:
			return False
		if self.health <= 0:
			return True



if __name__ == "__main__":
	enemigo = Enemy("Jacinto",33,10,"op")
	

	print(enemigo.hurt(enemigo.attack()))
	enemigo.show_info()
	
