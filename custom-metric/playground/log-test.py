import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename="example.log", encoding="utf-8", level=logging.DEBUG)
logging.debug("This message should go to the log file")
logger.info("So shoould this")
logger.warning("And this, too")
logger.error("And non-ASCII stuff, too, like Øresund and Malmö")
