import logging
logger = logging.getLogger(__name__)
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')
#leve and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)
formatter=logging.Formatter('%(name)s - %(level)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)
logger.addHandler(stream_h)
logger.addHandler(file_h)
logger.warning('WARNING MESSAGE')
logger.error('ERROR MESSAGE')
