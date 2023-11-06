from datetime import datetime,date
import time
now=datetime.now()
print(now)
print(type(now))
print(now.year,now.month,now.day,now.hour)

g=datetime(datetime.now().year,datetime.now().month,datetime.now().day,17,55)
print(g)
m=date.today()
h=date(2023,8,12)

h=now.strftime("%Y-%m-%d %H:%M:%S") #24Hrs
h=now.strftime("%y-%m-%d %I:%M:%S %A %p") #24Hrs
print(h,type(h))








while True:
    if datetime(datetime.now().year,datetime.now().month,datetime.now().day,14,1)<=datetime.now()<=datetime(datetime.now().year,datetime.now().month,datetime.now().day,18,1):
        print("Learning Hours")
    else:
        print("Family Hours")
    time.sleep(2)