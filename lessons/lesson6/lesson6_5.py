class A:
	def hello(self):
		print("Hello");

	# статический метод	- в чем разница от обычного метода класса !?
	@staticmethod	
	def hi():		# без self
		print("Hi");

a = A();
a.hello();
a.hi();

