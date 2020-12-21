import csv;

def csv_read(file):	
	reader = csv.reader(file);	# принимает открытый файл

	#join() - соединяет все элементы списка в одну строку 
	for row in reader:
		print(" ".join(row));	# str(" ").join
		#print(row);

csv_path = "text1.csv";

with open(csv_path, "r") as file:
	csv_read(file);




