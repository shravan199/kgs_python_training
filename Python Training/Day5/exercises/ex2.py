# WAP to create a file with 10 names vertically
import os
import logging

os.chdir(r'D:\Python\Python Training\Day5\exercises')

logging.basicConfig(filename='logs.txt', filemode='a')
logger = logging.getLogger('shravan_logger')

lines= []
try:
    with open('names.txt', 'rb') as fo:
        try:
           lines =  fo.readlines()
           print(lines)
        except IOError as ioe:
                logger.exception(f'\nError name: {ioe.__class__.__name__}, Error Msg: {ioe}')
        except Exception as e:
            logger.exception(f'\nError name: {e.__class__.__name__}, Error Msg: {e}')
except Exception as e:
        logger.exception(f'\nError name: {e.__class__.__name__}, Error Msg: {e}')
# Read these names
try:
    with open('names2.txt', 'wb') as fo:
         if lines.__len__  != 0:
               # deleleting/ignoring last 4 names
               lines = lines[: len(lines)-4]
               for line in lines:
                     fo.write(line)
except IOError as ioe:
                logger.exception(f'\nError name: {ioe.__class__.__name__}, Error Msg: {ioe}')
except Exception as e:
     logger.exception(f'\nError name: {e.__class__.__name__}, Error Msg: {e}')