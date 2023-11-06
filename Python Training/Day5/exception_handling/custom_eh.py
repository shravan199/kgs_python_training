import os
os.chdir(r'D:\Python\Python Training\Day5\exception_handling')

def main(file_name):
    try:
        fh = read_file(file_name)
        print(fh.read(50))
    except ValueError as ve:
        print(f'Error Name: {ve.__class__.__name__}')
        print(f'Error Msg: {ve} Extension should be .txt')
    except IOError as ioe:
        print(f'Error Name: {ioe.__class__.__name__}')
        print(f'Error Msg: {ioe}')
    except Exception as e:
        print(f'Error: {e.__class__.__name__}')
        print(f'Error Msg: {e}')
    else:
        print('This is else block')
    finally:
        print(f'This is finally block')
        try:
            fh.close()
        except:
            pass


def read_file(file_name):
   if file_name.endswith('.txt'):
       fh = open(file_name, 'r')
       return fh
   else:
       raise ValueError('Bad Extn.')

main('lines.ttrxt')