# WAP to create a file with 10 names vertically
import os
import logging

os.chdir(r'D:\Python\Python Training\Day5\exercises')

logging.basicConfig(filename='logs.txt', filemode='a')
logger = logging.getLogger('shravan_logger')

try:
    with open('names.txt', 'wb') as fo:
        try:
            for i in range(10):
                inp = input('Enter Name:')
                inp = str(i+1) + ': ' + inp + '\n'
                fo.write(inp.encode())
        except IOError as ioe:
                logger.exception(f'\nError name: {ioe.__class__.__name__}, Error Msg: {ioe}')
        except Exception as e:
            logger.exception(f'\nError name: {e.__class__.__name__}, Error Msg: {e}')
except Exception as e:
        logger.exception(f'\nError name: {e.__class__.__name__}, Error Msg: {e}')
# Read these names
try:
    with open('names.txt', 'r') as fo:
         for line in fo.readlines():
              print(line.strip())
except IOError as ioe:
                logger.exception(f'\nError name: {ioe.__class__.__name__}, Error Msg: {ioe}')
except Exception as e:
     logger.exception(f'\nError name: {e.__class__.__name__}, Error Msg: {e}')