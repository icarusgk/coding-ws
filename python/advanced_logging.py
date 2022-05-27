import logging

# STEP 1
# create a logger object instance
logger = logging.getLogger('log')

# STEP 2
# specify the lowest boundary for logging
logger.setLevel(logging.DEBUG)

# STEP 3
# set a destination for your logs or a handler
# here, we choose to print on console (a console handler)
console_handler = logging.StreamHandler()
file_log_handler = logging.FileHandler('log')


# STEP 4
# set the logging format for your handler
log_format = '%(asctime)s | %(name)s | %(levelname)s | %(message)s'

console_handler.setFormatter(logging.Formatter(log_format))
file_log_handler.setFormatter(logging.Formatter(log_format))


# finally, add the handler to the logger
logger.addHandler(console_handler)
logger.addHandler(file_log_handler)


# start the logging and show the messages
logger.debug('Here you have some information for debugging.')
logger.info('Everything is OK. Keep going!')
logger.warning("Something strange has happened, but it's not critical.")
logger.error('Something unexpected and critical has happened.')
logger.critical('A critical error! The code cannot run!')
