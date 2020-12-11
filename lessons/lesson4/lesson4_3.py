import time;

def countdown(num):
	print("Starting");
	while num > 0:
		yield num;
		num -= 1;

def calc(exp: str):	# тип аргумента - строго строка
	return eval(exp);
	
def connect_wifi():
	for i in range(0, 101, 10):
		print(str(i) + "% connected");
		time.sleep(0.5);	# приостановка выполнения
	print("Connection failed");