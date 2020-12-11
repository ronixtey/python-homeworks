def create_stack():
	return [];

def push(element, stack):
	stack.append(element);

def remove(stack):
	if(not is_empty(stack)):
		stack.pop();

def is_empty(stack):
	return (len(stack) == 0);

def calc(stack):
	i = 0;
	while i < len(stack) - 1:
		yield stack[i] * stack[i + 1];
		i += 1;

		
