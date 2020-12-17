FILE_NAME = "text.txt";

lorem = ("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod " +
	"tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, " +
	"quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo " +
	"consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse " +
	"cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non " +
	"proident, sunt in culpa qui officia deserunt mollit anim id est laborum.");


file = open(FILE_NAME, "w");
for i in range(5): 
	file.write(lorem);
	if(i < 4): file.write("\n\n");
file.close();


file = open(FILE_NAME);
print(file.read());
file.close();