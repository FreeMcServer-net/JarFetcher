import logging
from logging import Logger

logger: Logger

new_installs = []

def init_logger():
    global logger
    logger = logging.getLogger('JarFetcher')
    ch = logging.StreamHandler()
    logger.setLevel(logging.DEBUG)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.info('Logger ready!')


def versiontuple(v):
    return tuple(map(int, (v.split("."))))
