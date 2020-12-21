import csv;

def to_writer(data, path):
	with open(path, "w") as csv_file:
		csv_writer = csv.writer(csv_file, delimiter=",");
		
		for line in data:
			csv_writer.writerow(line);	# line - список

data = ["first_name,last_name".split(','), 
		"Ivan,Ivanov".split(','), 
		"Petr,Petrov".split(','),
		"Klara,Korallova".split(',')];
path = "text.csv";

to_writer(data, path);
