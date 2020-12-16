from abc import ABC, abstractmethod;
import math;

class Figure(ABC):
	@abstractmethod
	def draw(self):
		print("Квадрат нарисован");

class Square(Figure):
	def draw(self):
		super().draw();

	@staticmethod
 	def square(a):
		return a ** 2;

class Round(Figure):
	def draw(self):
		print("Круг нарисован");

	def __square(self, a):
		return math.pi * (a ** 2);


square = Square();
square.draw();
print(square.square(3));

round = Round();
round.draw();
#print(round._Round__square(4));


