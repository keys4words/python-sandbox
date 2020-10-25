import logging.config

from settings2 import logger_config


logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')


def main():
    logger.debug('Enter in to the Main()')


if __name__ == "__main__":
    main()
