# coding: utf-8

"""
This file will be used to improve logging
"""

import os
import time
import logging
from html import START, END, MSG

# * HTML fileHandler
# * ##########################################################################


class HTMLFileHandler(logging.FileHandler):
    """
    File handler specialised to write the start of doc as html and to close it
    properly.
    """

    def __init__(self, title, version, *args):
        super().__init__(*args)
        assert self.stream is not None
        # Write header
        self.stream.write(START % {"title": title, "version": version})

    def close(self):
        # finish document
        self.stream.write(END)
        super().close()


class HTMLFormatter(logging.Formatter):
    """
    Formats each record in html
    """
    CSS_CLASSES = {'WARNING': 'warning',
                   'INFO': 'info',
                   'DEBUG': 'debug',
                   'CRITICAL': 'error',
                   'ERROR': 'error'}

    def __init__(self):
        super().__init__()
        self._start_time = time.time()

    def format(self, record):
        try:
            class_name = self.CSS_CLASSES[record.levelname]
        except KeyError:
            class_name = "info"

        t = time.time() - self._start_time

        # handle '<' and '>' (typically when logging %r)
        msg = record.msg
        msg = msg.replace("<", "&#60")
        msg = msg.replace(">", "&#62")

        mouse_over = f"line : {record.lineno}"

        return MSG % {"class": class_name, "time": "%.4f" % t, "msg": msg,
                      "origin": record.module, "mouseover": mouse_over,
                      "line": record.lineno}


class HTMLLogger(logging.Logger):
    """
    Log records to html using a custom HTML formatter and a specialised
    file stream handler.
    """

    def __init__(self,
                 name="html_logger",
                 level=logging.DEBUG,
                 filename="log.html", mode='w',
                 title="HTML Logger", version="1.0.0"):
        super().__init__(name, level)
        f = HTMLFormatter()
        h = HTMLFileHandler(title, version, filename, mode)
        h.setFormatter(f)
        self.addHandler(h)


def setup(title, version, level=logging.DEBUG, dir='log'):
    """
    Setup the logger
    Args:
        title:
        version:
        level:
        dir:

    Returns:

    """
    loc_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = os.path.join(loc_path, dir)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    filename = os.path.join(dir_path, 'log.html')

    _logger = HTMLLogger(filename=filename, mode='w', title=title,
                         version=version, level=level)
    return _logger


_logger = None


def get_logger():
    global _logger
    if _logger is None:
        _logger = setup('Test', '2.0')
        _logger.info('Start logging')
    return _logger


