class Stack(object):
	def __init__(self):
		self.stack = [];

	def push(self, element):
		self.stack.append(element);

	def remove(self):
		if(not self.is_empty()):
			self.stack.pop();
	
	def is_empty(self):
		#return (len(self.stack) == 0);
		return not self.stack;
	def show(self):
		print(self.stack);



		


