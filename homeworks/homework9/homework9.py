import json;
import datetime;


json_file = "data.json";
data = [
	{
		"id": 1, 
		"username": "admin",
		"email": "admin@example.com",
		"registerd_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	},
	{
		"id": 2, 
		"username": "first_user",
		"email": "first_user@example.com",
		"registerd_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	},
	{
		"id": 3, 
		"username": "second_user",
		"email": "second_user@example.com",
		"registerd_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	}
];


with open(json_file, "w") as file:
	json.dump(data, file, indent=4);

with open(json_file) as file:
	print(json.load(file));