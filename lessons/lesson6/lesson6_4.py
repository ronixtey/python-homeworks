from abc import ABC, abstractmethod;

class Basic(ABC):
	@abstractmethod # надо обязательно дополнить или переопределить
	def hello(self):
		print("Hello from Basic class");

class Advanced(Basic):
	def hello(self): # дополняем метод
		super().hello();	# выполняем родительский код, обратившись к родительскому методу
		print("hello");

class Second(Advanced):
	def hello(self):
		super().hello();	# вызов метода из Advanced


# a = Advanced();
# a.hello();
Second().hello();




