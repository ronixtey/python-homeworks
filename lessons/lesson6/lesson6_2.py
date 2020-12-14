"""
class MyDict(dict):
	def get(self, key, default = 0):
			return dict.get(self, key, default);	# обращаемся к родительскому методу !?

a = dict(a = 1, b = 2);
b = MyDict(a = 3, b = 4);	

b['c'] = 5;
print(b);

print();
print(a.get("v"));
print(b.get("v"));
"""


# наследование
class Donkey:
	def say(self):
		print("I'm a donkey");

	def walk(self):
		print("Tygydyc - Tygydyc - Dyg");

class Horse:
	def say(self):
		print("I'm a horse")

class Moul(Donkey, Horse):	# если есть одинаковые методы, используется метод первого родителя
	def hi(self):
		print("Hi");

	def say(self):
		print("I'm a moul");	



donkey = Donkey();
horse = Horse();
moul = Moul();

donkey.say();
horse.say();
moul.hi();
moul.say();
moul.walk();

