import unittest
from control1_2 import Hero, Dragon

class TestCont(unittest.TestCase):
    def test_init_hero(self):
        self.hero = Hero(name="Hero", level=8, strength=18, dexterity=12, constitution=14, wisdom=10)
        self.assertIsNotNone(self.hero)

    def test_init_dragon(self):
        self.dragon = Dragon(name="Dragon", level=10, strength=20, dexterity=10, constitution=16, wisdom=20)
        self.assertIsNotNone(self.dragon)

    def test_empty_hero(self):
        self.hero = Hero(name="Hero")
        self.assertEqual(self.hero.name, "Hero")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.strength, 8)
        self.assertEqual(self.hero.dexterity, 8)
        self.assertEqual(self.hero.constitution, 8)
        self.assertEqual(self.hero.intelligence, 8)
        self.assertEqual(self.hero.wisdom, 8)
        self.assertEqual(self.hero.charisma, 8)
        self.assertIsNotNone(self.hero.max_hp)
        self.assertIsNotNone(self.hero.hp)
        self.assertEqual(self.hero.armour_class, 14)
        self.assertIsNotNone(self.hero.initiative)
        self.assertEqual(self.hero.slots, 1)

    def test_empty_dragon(self):
        self.dragon = Dragon(name="Dragon")
        self.assertEqual(self.dragon.name, "Dragon")
        self.assertEqual(self.dragon.level, 1)
        self.assertEqual(self.dragon.strength, 8)
        self.assertEqual(self.dragon.dexterity, 8)
        self.assertEqual(self.dragon.constitution, 8)
        self.assertEqual(self.dragon.intelligence, 8)
        self.assertEqual(self.dragon.wisdom, 8)
        self.assertEqual(self.dragon.charisma, 8)
        self.assertIsNotNone(self.dragon.max_hp)
        self.assertIsNotNone(self.dragon.hp)
        self.assertEqual(self.dragon.armour_class, 14)
        self.assertIsNotNone(self.dragon.initiative)
        self.assertEqual(self.dragon.slots, 1)

    def test_hero(self):
        self.hero = Hero(name="Hero", level=8, strength=18, dexterity=12, constitution=14, wisdom=10)
        self.assertIsNotNone(self.hero.name)
        self.assertEqual(self.hero.level, 8)
        self.assertEqual(self.hero.strength, 18)
        self.assertEqual(self.hero.dexterity, 12)
        self.assertEqual(self.hero.constitution, 14)
        self.assertEqual(self.hero.intelligence, 8)
        self.assertEqual(self.hero.wisdom, 10)
        self.assertEqual(self.hero.charisma, 8)
        self.assertIsNotNone(self.hero.max_hp)
        self.assertIsNotNone(self.hero.hp)
        self.assertEqual(self.hero.armour_class, 16)
        self.assertIsNotNone(self.hero.initiative)
        self.assertEqual(self.hero.slots, 1)

    def test_dragon(self):
        self.dragon = Dragon(name="Dragon", level=10, strength=20, dexterity=10, constitution=16, wisdom=20)
        self.assertIsNotNone(self.dragon.name)
        self.assertEqual(self.dragon.level, 10)
        self.assertEqual(self.dragon.strength, 20)
        self.assertEqual(self.dragon.dexterity, 10)
        self.assertEqual(self.dragon.constitution, 16)
        self.assertEqual(self.dragon.intelligence, 8)
        self.assertEqual(self.dragon.wisdom, 20)
        self.assertEqual(self.dragon.charisma, 8)
        self.assertIsNotNone(self.dragon.max_hp)
        self.assertIsNotNone(self.dragon.hp)
        self.assertEqual(self.dragon.armour_class, 15)
        self.assertIsNotNone(self.dragon.initiative)
        self.assertEqual(self.dragon.slots, 1)

    def test_hero_attack(self):
        self.hero = Hero(name="Hero", level=8, strength=18, dexterity=12, constitution=14, wisdom=10)
        self.assertIsNotNone(self.hero.attack())

    def test_dragon_attack(self):
        self.dragon = Dragon(name="Dragon", level=10, strength=20, dexterity=10, constitution=16, wisdom=20)
        self.assertIsNotNone(self.dragon.attack())

    def test_hero_save(self):
        self.hero = Hero(name="Hero", level=8, strength=18, dexterity=12, constitution=14, wisdom=10)
        self.assertIsNotNone(self.hero.save_throw(self.hero.dexterity))

    def test_dragon_save(self):
        self.dragon = Dragon(name="Dragon", level=10, strength=20, dexterity=10, constitution=16, wisdom=20)
        self.assertIsNotNone(self.dragon.save_throw(self.dragon.wisdom))

    def test_hero_perk(self):
        self.hero = Hero(name="Hero", level=8, strength=18, dexterity=12, constitution=14, wisdom=10)
        self.assertIsNotNone(self.hero.perk())

    def test_dragon_perk(self):
        self.dragon = Dragon(name="Dragon", level=10, strength=20, dexterity=10, constitution=16, wisdom=20)
        self.assertIsNotNone(self.dragon.perk())

    def test_several_hero_perk(self):
        self.hero = Hero(name="Hero", level=8, strength=18, dexterity=12, constitution=14, wisdom=10)
        self.assertIsNotNone(self.hero.perk())
        self.assertIsNone(self.hero.perk())

    def test_several_dragon_perk(self):
        self.dragon = Dragon(name="Dragon", level=10, strength=20, dexterity=10, constitution=16, wisdom=20)
        self.assertIsNotNone(self.dragon.perk())
        self.assertIsNone(self.dragon.perk())

if __name__ == '__main__':
    unittest.main()