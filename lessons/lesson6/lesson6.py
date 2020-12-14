class A:
	def _print_prviate(self): 	# псевдо приватный!?  
		print("Это приватный метод");

a = A();
a._print_prviate();


class B:
	def __print_very_private(self): # приватный метод (начинается с __)
		print("Это очень приватный метод");

b = B();
#b.__print_very_private();	#error
b._B__print_very_private();	# доступ
