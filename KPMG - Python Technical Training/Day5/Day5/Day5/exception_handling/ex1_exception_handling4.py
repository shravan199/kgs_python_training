try:
    fh=open('lines.txt','r')
    for line in fh:
        print(line.strip())
        
    a=1/0

except IOError as o:
    print(o.__class__.__name__," Msg:- ",o)
    gh=open('demo.txt','r')
    for line in gh:
        print(line.strip())    

except ZeroDivisionError as z:
    print("X/0 Error",z)
      

except Exception as e: #General Exception
    print("Error Handled!")
    print("Error NAme:-",e.__class__.__name__)
    print("Error Msg:-",e)
else:
    print("This else block.")    
finally:
    print("This is finally block.")
    try:
        fh.close()
    except Exception as e :
        print(e.__class__.__name__,e)
    
    
    
print("=========i am running ============")
import datetime as dt 
now=dt.datetime.now()
print(now)