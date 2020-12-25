import datetime;

date_time1 = datetime.datetime.today().strftime("%d-%m-%Y %H:%M:%S");

now = datetime.datetime.now();
then = datetime.datetime(2020, 12, 26);

delta = then - now;
# print(now);
# print(then);
# print(delta.days);
# print(delta.seconds);
# print(type(delta));	#type - timedelta

seconds = delta.total_seconds();
hours = seconds // 3600;
minutes = (seconds % 3600) // 60;

print(hours);  
print(minutes);  


