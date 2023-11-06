try:
    fh=open('lines.txt','r')
    for line in fh:
        print(line.strip())
        

    
except Exception as e: #General Exception 
    print("Error Handled!")
    print("Error NAme:-",e.__class__.__name__)
    print("Error Msg:-",e)
    
    
print("=========i am running ============")
import datetime as dt 
now=dt.datetime.now()
print(now)