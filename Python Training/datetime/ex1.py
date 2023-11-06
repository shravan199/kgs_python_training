from datetime import datetime as dt
import time

now = dt.now()
print(now, type(now))

print(dt.now(), now.year, now.month, now.day, now.hour, now.minute, now.second)

st =dt(now.year, now.month, now.day, 14, 00)
print(st)

et = dt(now.year, now.month, now.day, 18, 00)
# 2-6pm
while True:
    if st <= now <= et:
        print('Learning Hours!')
    else:
        print('Family Hours!')
         
    time.sleep(5)        