import time;

# print(time.gmtime(1));	#unixtime
# print(time.ctime());
# print(time.ctime(1342411211));

# print("I got asleep");
# time.sleep(2);
# print("I woke up))"); 

print(time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()));
print(time.time());
print(time.ctime(time.time()));

