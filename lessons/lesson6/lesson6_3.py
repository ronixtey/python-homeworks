from abc import ABC, abstractmethod;

class ChessPiece(ABC):	# объявление абстрактного класса
	def draw(self):
		print("Drew a chess piece");

	@abstractmethod
	def move(self):	# не реализованный метод
		pass;

#a = ChessPiece(); # error - нельзя создать экземпляр объекта с абстрактным методом


class Queen(ChessPiece):
	def move(self):
		print("Moved Queen to e2e4");

q = Queen();
q.draw();
q.move();


