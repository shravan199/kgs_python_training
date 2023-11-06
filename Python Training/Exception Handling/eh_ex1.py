import os

os.chdir('D:\Python\Python Training\Exception Handling')
print(f'Current working directory: {os.getcwd()}')
try:
    with open('lines.txt', 'r') as file:
        print(file)
    
    div = 4/0

except IOError as ioe:
    print('Error name:', ioe.__class__.__name__, ', Error message:', ioe)
    fh = open('demo.txt')
    for line in fh:
        print(line.strip()) 
except ZeroDivisionError as zde:
    print(f'Error name: {zde.__class__.__name__} and error message:  {zde}')    
except Exception as e:
    print('Error Name:', e.__class__.__name__)    
    print('Error Message:', e)