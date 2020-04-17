from loginit import get_logger

logger = get_logger()


def test():
    logger.warning('Success')
    logger.error('File handler specialised to write the start of doc as html '
                 'and to close it properly. HTML logger for python start from'
                 ' the github project : '
                 'https://gist.github.com/ColinDuquesnoy/8296508')
