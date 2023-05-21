#!/usr/bin/python3

import json
import xmltodict
from enemy_class import Enemy
import random



class Enemies:
	def __init__(self,jsonorxml):
		
		global health
		global health1
		global health2
		global jsonorxml2

		
		self.jsonorxml2 = jsonorxml
		self.enemies = []
		size = len(self.enemies)
		#global jsonorxml2
	
		
		
		if self.jsonorxml2 == 1:
			with open("enemies.json") as f:
				data = json.load(f)
				self.enemies_list = data["enemies"]["enemy"]

			for e in self.enemies_list:
				self.enemies.append(Enemy(e["name"], e["health"], e["strenght"], e["description"]))		
#				print("json")			
		

		elif self.jsonorxml2 == 2:
			xml_file = open("enemies.xml","r")
			enemies_tmp = xmltodict.parse(xml_file.read())
			self.enemies_list = enemies_tmp["enemies"]["enemy"]

			for e in self.enemies_list:
				self.enemies.append(Enemy(e["name"],e["health"], e["strenght"], e["description"]))
#				print("xml")
		

		health = self.enemies[0].health
		health1 = self.enemies[1].health
		health2 = self.enemies[2].health


	def show_info(self, current_enemy):
		self.enemies[current_enemy].show_info()
	
	def gameover (self,enemy_counter):
		if self.enemies[enemy_counter] > size:
			return True
	
	def dead (self, enemy_counter):
		health = int(self.enemies[enemy_counter].health)
		if health <= 0:
			return True

	def count (self):
		return len(self.enemies)

	
	def start (self):
		self.enemies[0].health = health
		self.enemies[1].health = health1
		self.enemies[2].health = health2


	def saving(self, enemy_counter):
		
		health = self.enemies[enemy_counter].health
		description = self.enemies[enemy_counter].strenght
		name = self.enemies[enemy_counter].name
		
    

	def hurt(self, playerdamage,enemy_counter):
		current_hp = self.enemies[enemy_counter].health = int(self.enemies[enemy_counter].health) - int(playerdamage)
		current_hp
		return current_hp
		
		print("El enemigo ahora tiene los siguientes puntos de vida: {}".format(self.enemies[enemy_counter].health))
		print()

	def attack(self,enemy_counter):
		enemy = self.enemies[enemy_counter]
		strength = int(enemy.strength)		
		
#		if self.jsonorxml2 == 1:
#			print("json")
#		if self.jsonorxml2 == 2:
#			print("xml")
		return random.randint(0, strength)
	
	
if __name__ == "__main__":
	enemies = Enemies();
  
