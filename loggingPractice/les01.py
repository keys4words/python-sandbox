import logging
import requests

logging.basicConfig(level='DEBUG', filename='testLog.log')
logger = logging.getLogger()
# logger.setLevel('DEBUG')
# print(logger.handlers)
# for key in logging.Logger.manager.loggerDict:
#     print(key)

logging.getLogger('urllib3').setLevel('ERROR')


def main(param):
    logger.debug(f'hello from main #{param}')
    r = requests.get('https://www.google.com/')



if __name__ == "__main__":
    main('XO')
