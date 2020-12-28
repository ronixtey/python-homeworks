"""s
try:
	for i in range(3):
		print(3 / i);

except:	# без конкретного указания
	print("Деление на 0");
	print("Исключение обработано");


a, b = 1, 0;	#!!!

try:
	print(a / b);
	print("Это будет напечатано");
	print("10 " + 10);
except TypeError:
	print("Вы сложили значения несовместимых типов");
except ZeroDivisionError:
	print("Деление на 0");

print("Будет ли это напечатано?");
"""

"""
try:
	print("1" + 1);
	print(1 / 0);
except(TypeError, ZeroDivisionError):
	print("Неправильный ввод");
"""

"""
try:
	print("1" + 1);	# не обработна TypeErro
	print(sums);
	print(1 / 0);
except NameError:
	print("sum не существует");
except ZeroDivisionError:
	print("Вы не можете делить на нуль");
except:
	print("Что-то пошло не так");
"""

"""
try:
	print(1 / 0);
except:		# error, общий except должен быть в конце
	raise;	# просто показать пойманное исключение
except:
	print("Исключение поймано");
finally:
	print("Хорошо");
"""

"""
try:
	print(1 / 0);
except ZeroDivisionError:
	try:
		print(2 / 0);
	except ZeroDivisionError:
		print("Caught!");
finally:
	print("Ничего не происходит");	
"""

"""
a, b = int(input()), int(input());
try:
	if b == 0:
		raise ZeroDivisionError;
except:	# поймает ZeroDivisionError
	print("Деление на ноль");	
print("Будет ли это напечатано");
"""

try:
	print(1 / 0);
except:
	raise ZeroDivisionError("Деление на ноль");

