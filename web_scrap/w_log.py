import logging

def set_custom_log_info(filename):
    logging.basicConfig(filename=filename)
    level = logging.INFO


def report(e:Exception):   #e parameter optional
    logging.exception(str(e))
