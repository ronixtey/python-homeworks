import datetime;


#(year, month, day)
date = datetime.date(2020, 12, 23);
print("Year: " + str(date.year));
print("Month: " + str(date.month));
print("Day: " + str(date.day));
#print(datetime.date.today().year);	# текущее число


#(year, month, day, hour, minute, second)
date_time = datetime.datetime(2020, 12, 23, 20, 46, 50);
#print(date_time);

print(datetime.datetime.today());
print(datetime.datetime.now());