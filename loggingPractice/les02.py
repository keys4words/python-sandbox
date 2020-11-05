import logging

# logging.basicConfig()
logger = logging.getLogger('app')
handler = logging.StreamHandler()
handler.setLevel('DEBUG')

f = logging.Formatter(fmt='%(levelname)s - %(name)s -%(message)s')
handler.setFormatter(f)
logger.addHandler(handler)

loggerChild = logging.getLogger('logger.child')
# print(logger.handlers)
loggerChild.setLevel('DEBUG')
# print(loggerChild.handlers)
# print(logger.parent)
# loggerChild.propagate = False

def main(param):
    logger.debug(f'hello from main #{param}')


if __name__ == "__main__":
    main('XO')
