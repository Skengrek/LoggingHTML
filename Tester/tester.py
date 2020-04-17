
from loginit import get_logger
from Tester import othermodules

logger = get_logger()


if __name__ == "__main__":
    logger.debug("A debug message")
    logger.info('Test info 2')
    othermodules.test()

    for i in range(40):
        logger.info(f'For step number: {i}')
