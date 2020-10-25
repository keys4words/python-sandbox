import logging.config

from settings import logger_config


logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')


def new_func():
    name = 'maxim'
    logger.debug('Enter in to the New_func()', extra={'my_name': name})

def main():
    logger.debug('Enter in to the Main()')


if __name__ == "__main__":
    new_func()
    main()
