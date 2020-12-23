import csv;

path = "data.csv";
data = (
	"id,username,email,ip_address",
	"1,root,root@example.com,192.168.0.1",
	"2,admin,admin@example.com,192.168.0.2", 
	"3,test_user,test_user@example.com,192.168.0.3",
	"4,second_user,second_user@example.com,192.168.0.4"
);

def write_to_file(file_path, data):
	with open(file_path, 'w', newline='') as csv_file:
		csv_writer = csv.writer(csv_file);
		csv_writer.writerows([row.split(',') for row in data]);

def read_file(file_path):
	with open(file_path, 'r') as csv_file:
		csv_reader = csv.reader(csv_file);
		for row in csv_reader: print(",".join(row));



write_to_file(path, data);
read_file(path);



