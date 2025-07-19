import inspect
import logging
import os




def getLogger():
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    path = os.path.abspath(os.curdir) + '\\logs\\logfile.log'
    file_handler = logging.FileHandler(path)
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)  # filehandler object

    logger.setLevel(logging.DEBUG)
    return logger



