import logging

# this module provides a flexible framework for outputting log messages.
# logging.warning("Your %s was executed successfully, but the %s is wrong!", "script", "output")
# By default, the output message has the following format: 
# {LEVEL}:{LOGGER}:{MESSAGE}


# This format can be changed by using the format attribute when 
# configuring the logger. To do it, we need to call 
# the basicConfig() method:
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level='DEBUG',
                    filename='log_file.txt',
                    filemode='w',
                    )

logging.critical("It is critical to understand logs!")
logging.error("Running this line will result in an error message!")
logging.warning("You must catch that bug! It is a warning!")
logging.info("My info is that you are here!")
logging.debug("I'm debugging!")

