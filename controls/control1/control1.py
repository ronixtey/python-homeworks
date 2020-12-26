from abc import ABC, abstractmethod;
from random import randint;
from math import floor;

class Character(ABC):
	
	def __init__(self, name, level=1, strength=8, dexterity=8, constitution=8, intelligence=8, wisdom=8, charisma=8):
		self.name = name
		self.level = level
		self.strength = strength
		self.dexterity = dexterity	# ловкость
		self.constitution = constitution	# телосложение
		self.intelligence = intelligence
		self.wisdom = wisdom	# мудрость
		self.charisma = charisma
		self.max_hp = 10 + floor((self.constitution - 10) / 2) + randint(1, 11) * self.level
		self.hp = self.max_hp
		self.armour_class = 15 + floor((self.dexterity - 10) / 2)
		self.initiative = randint(1, 21) + floor(((self.dexterity - 10) / 2))
		self.slots = 2 + floor((self.charisma - 10) / 2);

		self.attack_damages = [];
		self.perk_damages = []
		self.heal_count = 0;

	def attack(self):
		damage = randint(1, 13) + floor(((self.strength - 10) / 2));
		self.attack_damages.append(damage);
		return damage;
		
	def save_throw(self, attribute):
		return randint(1, 21) + floor(((attribute - 10) / 2))
	
	def heal(self):
		self.hp = self.max_hp;
		self.heal_count = self.heal_count + 1;

	def death(self):
		return self.name + " is dead";

	@abstractmethod
	def perk(self):
		pass;

		
class Hero(Character):
	def perk(self):
		if(self.slots <= 0):
			return None;
		else:
			self.slots = self.slots - 1;
			
			damage = randint(1, 17) + floor(((self.wisdom - 10) / 2));
			self.perk_damages.append(damage);	
			return damage;

class Dragon(Character):
	def perk(self):
		if(self.slots <= 0):
			return None;
		else:
			self.slots = self.slots - 1;
		
			damage =  randint(1, 17) + floor(((self.strength - 10) / 2))
			self.perk_damages.append(damage);
			return damage;