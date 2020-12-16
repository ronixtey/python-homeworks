list = [str(i) + str(i - 1) for i in range(10)];

file = open("text2.txt", 'w');

for i in list: file.write(i + '\n');
file.close();

#print(open("text2.txt").read());

file = open("text2.txt", 'r');
list = [line.strip() for line in file]	# strip() - убирает лишние символы
#print(list);
file.close();


file = open("text2.txt", 'r');
#print(file.readline());
file.close();


# список всех строк
file = open("text2.txt", 'r');
#print(file.readlines());


file.readline();
file.readline();
# print(file.tell());
	
file.seek(1);		# перемещение к определнному байту
#print(file.readline());
print(file.tell());





