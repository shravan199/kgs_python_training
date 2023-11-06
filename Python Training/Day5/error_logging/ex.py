import logging
import os
os.chdir(r'D:\Python\Python Training\Day5\error_logging')

_file_path = r'D:\Python\Python Training\Day5\error_logging'
log_fname = r'log_file.txt'

log_file_obj = open(os.path.join(_file_path, log_fname), 'a')

name = 'CFG'

# Create and configure logger
logging.basicConfig(
    filename=log_fname,
                    filemode='a')

# create logging obj
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

#Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

logging.error(f'{name} raised an error')
#log_file_obj.write(logging.error(f'{name} raised an error'))
