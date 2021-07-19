from util.logger import Logger

if __name__ == '__main__':

    logger = Logger()

    logger.info('This is info message')
    logger.warn('This is warning message')
    logger.error('This is a error message')
    logger.debug('This is a debug message')
    logger.critical('This is a critical message')


