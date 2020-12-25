import json;

# data = {
# 	"dog": {
# 		"name": "Pushok",
# 		"color": "Grey",
# 	},
# 	"cat": {
# 		"name": input("input name: "),	#!!!!
# 		"color": input("inpit color: ")
# 	}
# };

# with open("data.json", "w") as file:
# 	json.dump(data, file);

# with open("data.json") as file:
# 	print(json.load(file));



x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

#data - str; . - separate objects (fields), = - separate key&value;  
data = json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True);	
print(data);
