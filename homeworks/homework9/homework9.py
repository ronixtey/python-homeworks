import json;
import datetime;

json_file = "data.json";
data = [
	{
		"id": None, 
		"username": "admin",
		"email": "admin@example.com",
		"registered_at": None
	},
	{
		"id": None, 
		"username": "first_user",
		"email": "first_user@example.com",
		"registered_at": None
	},
	{
		"id": None, 
		"username": "second_user",
		"email": "second_user@example.com",
		"registered_at": None
	}
];


with open(json_file, "w") as file:
	for i in data:
		i["id"] = data.index(i) + 1;
		i["registered_at"] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S");
	json.dump(data, file, indent=4);

with open(json_file) as file:
	print(json.load(file));