class Point(object):
	def __init__(self, point): #конструктор
		self.point = point;

	def show(self):	#self обязателен
		print(self.point);

class Location(object):
	def __init__(self, x, y, z):
		self.coord = (Point(x), Point(y), Point(z));
		# self.coord = (x, y, z);

	def show(self):
		print(self.coord); 

x = 10;
y = 20;
z = 30;

coord = Location(x, y, z);
coord.show();