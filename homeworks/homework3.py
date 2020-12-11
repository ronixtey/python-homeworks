def calc(a, b, c):
	return eval(a + c + b);

while True:
	a = input("Первое число: ");
	b = input("Второе число: ");

	# проверка операндов
	if(not a.isdigit() or not b.isdigit()):
		print("Введите числа в качестве операндов!");
		continue;
	
	c = input("Оператор (+ - * /): ");
	#проверка оператора
	if(c not in ['+', '-', '*', '/']):
		print("Неправильный оператор. Используйте: + - * /");
		continue;

	try:
		print(calc(a, b, c));
	except ZeroDivisionError:
		print("На ноль делить нельзя!");

