import logging.config

from settings import logger_config


logging.config.dictConfig(logger_config)

logger = logging.getLogger('app_logger')

words = ['one word', 'two words', 'three', 6]


def main():
    for item in words:
        try:
            print(item.split(' '))
        except:
            # logger.debug('Exception here', exc_info=True)
            logger.exception('Exception here')
            pass
            


if __name__ == "__main__":
    main()
