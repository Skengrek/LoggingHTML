# coding: utf-8

"""

"""


import logging


format_ = '[%(asctime)s] %(levelname)s from %(name)s line %(lineno)d' \
          '.: %(message)s'

h = logging.StreamHandler()
f = logging.Formatter(format_, datefmt='%H:%M:%S')
h.setFormatter(f)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = 0  # To avoid calling parent handlers of the logger.
logger.addHandler(h)

if logging.getLogger().handlers:
    # Special case where the main handler does not root to STDERR but
    # somewhere else.
    h.stream = logging.getLogger().handlers[0].stream

