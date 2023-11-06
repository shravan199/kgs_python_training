import os

file_path = r"D:\Python\Python Training\Day5\file_handling"
file_name = r'line.txt'

try:
    #with open(os.path.join(file_path, file_name)) as fh:     
    fh=open(os.path.join(file_path, file_name),'r')
    for line in fh:
        print(line.strip())
        
    #a=1/0
except ZeroDivisionError as zde:
    print("X/0 Error", zde)

except IOError as ioe:
    print(ioe.__class__.__name__," Msg:- ",ioe)
    gh=open(os.path.join(file_path, 'out.txt'),'r')
    for line in gh:
        print(line.strip())    
except Exception as e: #General Exception
    print("Error Handled!")
    print("Error NAme:-",e.__class__.__name__)
    print("Error Msg:-",e)
else:
    print(f'This is else block.')
finally:
    print("This is finally block.")
    # if isinstance(fh):
    #     print(f'fh object exists')
    # else:
    #     print(f'fh object doesn\'t exist')
    try:
        fh.close()
    except:
        pass

print("=========i am running ============")
import datetime as dt 
now=dt.datetime.now()
print(now)