import control1;
from random import randint;

def attack(issuer, damaged):
	if(randint(0, 1) == 0):
		damage = issuer.perk();
		if(damage is None): damage = issuer.attack();
	else:
		damage = issuer.attack();
	
	damaged.hp = damaged.hp - damage;
	if(damaged.hp <= 0): damaged.death();

def show_stats():
	print(f"{dragon.name} average damage:", sum(dragon.attack_damages) / len(dragon.attack_damages));
	print(f"{dragon.name} attacks counts:", len(dragon.attack_damages) + len(dragon.perk_damages));
	print(f"{dragon.name} perk damage:", sum(dragon.perk_damages));
	print("---------------------------------------------------------");
	print(f"{hero.name} average damage:", sum(hero.attack_damages) / len(hero.attack_damages));
	print(f"{hero.name} attacks counts:", len(hero.attack_damages) + len(hero.perk_damages));
	print(f"{hero.name} healed:", hero.heal_count);
	print(f"{hero.name} perk damage:", sum(hero.perk_damages));


hero = control1.Hero("Kolyan", 8, 18, 12, 14, 8, 10);
dragon = control1.Dragon("Dragon", 10, 20, 10, 16, 8, 20);

while dragon.hp > 0:
	if(hero.hp >= 11): attack(hero, dragon);
	else: hero.heal();

while hero.hp > 0:
	attack(dragon, hero);

show_stats();