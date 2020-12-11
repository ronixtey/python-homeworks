from stack import *;
from random import randint;

a = create_stack();
print(a);

push(2, a);
push(3, a);
push(4, a);

print(a);
# remove(a);
# print(a);

# print(is_empty(a));


for x in calc(a):
 	print(x);
