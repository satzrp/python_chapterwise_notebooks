import logging

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)

#logger = logging.getLogger()
logger = logging.getLogger("sample-logger")

logger.debug("this is a debug log")
logger.info("this is a info log")
logger.warning("this is a warning log")
logger.critical("this is a critical log")
