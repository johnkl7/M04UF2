#!/usr/bin/python3

import xmltodict
from enemy_class import Enemy




class Enemies:
	def __init__(self):
		xml_file = open("enemies.xml","r")
		enemies_tmp = xmltodict.parse(xml_file.read())
		enemies_list = enemies_tmp["enemies"]["enemy"]


		self.enemies = []

		for e in enemies_list:
			self.enemies.append(Enemy(e["name"], e["health"], e["strenght"], e["description"]))		

	def show_info(self,enemy_counter):
		self.enemies[enemy_counter].show_info()

	def hurt(self, damage):
		dead = self.enemies[self.enemy_counter].hurt(damage)

		if dead:
			print("Lo has matado!")
			self.enemy_counter += 1

			return True

		return False

	def attack(self):
		return self.enemies[self.enemy_counter].attack()
	
	
if __name__ == "__main__":
	enemies = Enemies();

