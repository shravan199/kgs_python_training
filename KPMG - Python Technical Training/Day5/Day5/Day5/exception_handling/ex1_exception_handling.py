try:
    fh=open('line.txt','r')
    for line in fh:
        print(line.strip())
except: 
    print("Error Handled!")
    
    
print("=========i am running ============")
import datetime as dt 
now=dt.datetime.now()
print(now)