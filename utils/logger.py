import logging

class Logger:
    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_error(message):
        logging.error(message)
