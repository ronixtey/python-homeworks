def countdown(num):
	print("Starting");
	while num > 0:
		yield num;
		num -= 1;
	

"""
val = countdown(5);

# print(next(val));
# print(next(val));
# print(next(val));
# print(next(val));
# print(next(val));
# print(next(val));

a = [1, 2, 3];	# простой список
b = [i + 10 for i in a];	# генератор списка
	b2 = [i for i in range(0, 10)];

c = {i:i**2 for i in range(11, 15)}; # генератор словаря
d = {i for i in range(11, 15)};

e = (i for i in range(2, 8)); # генератор-выражение !?

for i in range(3, 16):	# с шагом 3
	if (i % 3 == 0):
		print(f"{i} делится на 3, результат: {i // 3}");	#форматирование
"""






