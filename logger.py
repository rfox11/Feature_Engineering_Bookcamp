import logging

# create logger
logger = logging.getLogger('Feature Engineering Log')
logger.setLevel(logging.INFO)

# create console handler and set level to INFO
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
consoleHandler.setFormatter(formatter)  # add formatter to ch
logger.addHandler(consoleHandler)  # add ch to logger