text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

list = text.split();	# по умолчанию пробелы
#print(list);

file = open("text_3.txt", 'w');
for word in list: file.write(word + ' ');
file.close();

#open("text_3.txt", "w").write(text);


file = open("text_3.txt");
print(file.readline(5));
file.close();
