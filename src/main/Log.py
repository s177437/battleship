import logging


class Log:
    def __init__(self):
        pass

    logging.basicConfig(filename="battleship.log", level=logging.INFO)

    @staticmethod
    def print_log(content):
        logging.info(content)
