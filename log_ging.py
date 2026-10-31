import logging
"""
DEBUG, INFO, WARNING, ERROR, CRITICAL
"""
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


#logger is to create handler for seperate things
logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)
logger.debug("for my_app")

#streamhandler is to 
console = logging.StreamHandler()
console.setLevel(logging.INFO)

#filehandler is to
file_handler = logging.FileHandler("errors.log")
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file_handler)

logger.debug("Debug message")
logger.info("Application started")
logger.warning("Memory usage high")
logger.error("Database connection failed")
