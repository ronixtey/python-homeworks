import json;
import datetime;

# 	"dog": {

json_file = "data.json";
# data = [
# 	{"username": "admin", "email": "admin@example.com"},
# 	{"username": "first_user", "email": "first_user@example.com"},
# 	{"username": "second_user", "email": "second_user@example.com"},
# ];
data = [
	{
		"id": 1, 
		"username": "admin",
		"email": "admin@example.com",
		"registered_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	},
	{
		"id": 2, 
		"username": "first_user",
		"email": "first_user@example.com",
		"registered_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	},
	{
		"id": 3, 
		"username": "second_user",
		"email": "second_user@example.com",
		"registered_at": datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	}
];


with open(json_file, "a") as file:
	for i in data:
		data[i]["id"] = 0;
		print(i);
	# json.dump(data, file, indent=4);


# with open(json_file, "w") as file:
# 	json.dump(data, file, indent=4);

with open(json_file) as file:
	print(json.load(file));