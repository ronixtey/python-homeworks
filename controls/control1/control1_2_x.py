# Полная боевка, герой и дракон атакую друг друга в одном цикле

import control1;
from random import randint;

class Battle:
	def __init__(self, hero, dragon):
		self.hero = hero;
		self.dragon = dragon;
	
	def start(self):
		print("Well, the fight is gonna be started");
		print(f"{hero.name}'s hp = {hero.hp}, Dragon's hp = {dragon.hp}");
		print(f"{hero.name}'s perks = {hero.slots}, Dragon's perks = {dragon.slots}");
		print("Fight...");
		
		while (hero.hp > 0 and dragon.hp > 0):
			if(randint(0, 1) == 0):
				# hero's action
				if(hero.hp >= 11): 
					self.__attack__(hero, dragon); 
				else:
					hero.heal();
					print(f"{hero.name} heals, now his hp =", hero.hp);
			else: 
				#dragon's action	
				self.__attack__(dragon, hero);

		# if loop ends, finish battle
		self.__finish__();


	def __finish__(self):
		print();
		self.__show_stats__()


	def __attack__(self, issuer, damaged):
		if(randint(0, 1) == 0):
			print(f"{issuer.name} uses perks..");
			damage = issuer.perk();
			if(damage is None):
				print(f"out of perks, {issuer.name} attacks..");
				damage = issuer.attack();
		else:
			print(f"{issuer.name} attacks..");
			damage = issuer.attack();
		
		damaged.hp = damaged.hp - damage;
		if(damaged.hp <= 0): 
			return print(damaged.death());
		else:
			print(f"now {damaged.name}'s hp =",damaged.hp);
	
	def __show_stats__(self):
		try:
			print(f"{dragon.name} average damage:", sum(dragon.attack_damages) / len(dragon.attack_damages));
		except ZeroDivisionError:
			print(f"{dragon.name} average damage: 0");
		print(f"{dragon.name} attacks counts:", len(dragon.attack_damages) + len(dragon.perk_damages));
		print(f"{dragon.name} perk damage:", sum(dragon.perk_damages));
		print("---------------------------------------------------------");
		try:
			print(f"{hero.name} average damage:", sum(hero.attack_damages) / len(hero.attack_damages));
		except ZeroDivisionError:
			print(f"{hero.name} average damage: 0");
		print(f"{hero.name} attacks counts:", len(hero.attack_damages) + len(hero.perk_damages));
		print(f"{hero.name} healed:", hero.heal_count);
		print(f"{hero.name} perk damage:", sum(hero.perk_damages));
		print("---------------------------------------------------------");
		print(f"{dragon.name} attack damages:", dragon.attack_damages);
		print(f"{dragon.name} perk damages:", dragon.perk_damages);
		print(f"{hero.name} attack damages: {hero.attack_damages}");
		print(f"{hero.name} perk damages: {hero.perk_damages}");

# create players
hero = control1.Hero("Kolyan", 8, 18, 12, 14, 8, 10);
dragon = control1.Dragon("Dragon", 10, 20, 10, 16, 8, 20);

#start battle
Battle(hero, dragon).start();