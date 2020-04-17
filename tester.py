
from loginit import get_logger
import othermodules

logger = get_logger()


if __name__ == "__main__":
    logger.debug("A debug message")
    logger.info('Test info 2')
    othermodules.test()
