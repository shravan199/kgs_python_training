import os
import datetime as dt
file_path = r"D:\Python\Python Training\Day5\file_handling"
file_name = r'line.txt'

try:
    with open(os.path.join(file_path, file_name)) as fo:
        print(fo.read(50))
        #name
except Exception as e:
     print(f'\nError handled')
     print(f'Error name: {e.__class__.__name__}, \nError msg: {e}')

print(f'####### I am running... #######')
now = dt.datetime.now()
print(now)