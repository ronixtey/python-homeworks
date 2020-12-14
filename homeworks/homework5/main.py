import stack, random;

stack = stack.Stack();
stack.show();

stack.push(random.randint(0, 100));
stack.push(random.randint(0, 100));
stack.push(random.randint(0, 100));
stack.show();

stack.remove();
stack.show();

print(f"Is stack empty? {stack.is_empty()}");

