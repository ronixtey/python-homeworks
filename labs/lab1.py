from abc import ABC, abstractmethod;
from random import randint;
from math import floor;

class Character(ABC):
	strength = 8;	
	dexterit = 8;		# ловкость
	constitution = 8;	#телосложение
	intelligence = 8;
	wisdom = 8; 		# мудрость
	charisma = 8;		

	def __init__(self, name, level):
		self.name = name;
		self.level = level;

		self.max_hp = 10 + self.constitution + (randint(1, 10) * self.level);	
		self.hp = self.max_hp;
		self.armor_class = 15 + self.dexterit;
		self.initiative = randint(1, 20) + self.dexterit;

	def attack(self):
		return randint(1, 12) + self.strength;
		
	def save_throw(self, attribute):
		return randint(1, 20) + floor((attribute - 10) / 2);
	
	@abstractmethod
	def perk(self):
		pass;
		
class Hero(Character):
	strength = 18;
	dexterit = 12;
	constitution = 14;
	wisdom = 10;

	def perk(self):
		self.hp = self.hp + (randint(1, 16) + self.wisdom);
		dragon.hp = dragon.hp - (randint(1, 16) + self.wisdom);

class Dragon(Character):
	strength = 20;
	dexterit = 10;
	constitution = 16;
	wisdom = 20;

	def perk(self):
		hero.hp = hero.hp - randint(1, 16) + self.strength;


# hero = Hero(name="Kolyan", level=8);
# dragon = Dragon(name="Aria", level=10);




