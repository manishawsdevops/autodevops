import logging


class Logger:
    def __init__(self):
        logging.basicConfig(filename="logs/autodevops.log",format='%(asctime)s %(message)s')
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

    def debug(self,msg):
        self.logger.debug(msg)

    def warn(self,msg):
        self.logger.warning(msg)

    def info(self,msg):
        self.logger.info(msg)

    def error(self,msg):
        self.logger.error(msg)

    def critical(self,msg):
        self.logger.critical(msg)

