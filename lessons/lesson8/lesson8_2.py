import csv;

def csv_dict_reader(file, delimiter=","):
	# первая строка в файле используется как набор ключей
	# последующие строки как значения
	reader = csv.DictReader(file, delimiter=delimiter);	
	for line in reader:
		print(line['first_name']);
		print(line['last_name']);


with open("text.csv", "r") as file:
	csv_dict_reader(file);




