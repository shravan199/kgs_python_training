import os

def get_file(file_name):
    if not file_name.endswith('.txt'):
        raise ValueError('file extension should be .txt or file name should be lines.')
    elif file_name.split('.')[0] != 'lines':
        raise NameError('File name should be lines.')
    else:
        raise IOError('file not found.')

os.chdir('D:\Python\Python Training\Exception Handling')
print(f'Current working directory: {os.getcwd()}')
try:
    with open(get_file('lin.txt'), 'r') as file:
        print(file)
    
    div = 4/2
except ValueError as ve:
    print('Error name:', ve.__class__.__name__ , 'and error message: ', ve)
except NameError as ne:
    print( ne)
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
else:
    print('This is else block. There is no exception found in code')   
finally:
    print('This is finally block.')
    try:
        fh.close()
        file.close()    
    except Exception as e:
        pass
        print(e.__class__.__name__)
        pass